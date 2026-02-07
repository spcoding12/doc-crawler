"""
内容提取模块

从HTML页面中提取：
- 标题
- 正文内容（转为Markdown）
- 图片URL列表
"""

from bs4 import BeautifulSoup
import html2text
from readability import Document
from typing import Optional
import re

from .frameworks import (
    FrameworkAdapter,
    DocusaurusAdapter,
    VuePressAdapter,
    MkDocsAdapter,
    GitBookAdapter,
    GenericAdapter,
)
from .detector import detect_framework


class ExtractedContent:
    """提取的页面内容"""
    def __init__(
        self,
        title: str,
        markdown: str,
        images: list[str],
        url: str = "",
    ):
        self.title = title
        self.markdown = markdown
        self.images = images  # 图片URL列表
        self.url = url
    
    def __repr__(self):
        return f"ExtractedContent(title='{self.title[:30]}...', images={len(self.images)})"


# 框架适配器映射
ADAPTERS = {
    'docusaurus': DocusaurusAdapter,
    'vuepress': VuePressAdapter,
    'mkdocs': MkDocsAdapter,
    'gitbook': GitBookAdapter,
    'generic': GenericAdapter,
    'unknown': GenericAdapter,
}


def get_adapter(framework_name: str) -> FrameworkAdapter:
    """获取对应框架的适配器实例"""
    adapter_class = ADAPTERS.get(framework_name, GenericAdapter)
    return adapter_class()


def extract_images(soup: BeautifulSoup, base_url: str = "") -> list[str]:
    """
    提取页面中的所有图片URL
    
    Args:
        soup: BeautifulSoup对象
        base_url: 用于转换相对URL
    
    Returns:
        list[str]: 图片URL列表
    """
    images = []
    seen = set()
    
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        if not src:
            continue
        
        # 跳过 data URI
        if src.startswith('data:'):
            continue
        
        # 转换为绝对URL
        if base_url and not src.startswith(('http://', 'https://')):
            from urllib.parse import urljoin
            src = urljoin(base_url, src)
        
        if src not in seen:
            seen.add(src)
            images.append(src)
    
    return images


def html_to_markdown(html_content: str) -> str:
    """
    将HTML转换为Markdown
    
    Args:
        html_content: HTML字符串
    
    Returns:
        str: Markdown字符串
    """
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # 不自动换行
    h.unicode_snob = True
    h.skip_internal_links = False
    
    markdown = h.handle(html_content)
    
    # 清理多余空行
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown.strip()


def clean_markdown(markdown: str) -> str:
    """
    清理Markdown内容中的噪音
    
    处理：
    - 图标/特殊字符（chevron-right, arrow-up-right等）
    - UI元素（Copy, Was this helpful等）
    - 重复标题
    - 导航面包屑
    
    Args:
        markdown: 原始Markdown
    
    Returns:
        str: 清理后的Markdown
    """
    # 1. 清理图标字符（GitBook/SonarSource风格）
    icon_patterns = [
        r'chevron-right',
        r'chevron-left',
        r'chevron-down',
        r'chevron-up',
        r'arrow-up-right',
        r'arrow-down',
        r'arrow-left',
        r'arrow-right',
        r'sparkleAsk',
        r'hashtag',
        r'house',
        r'server',
        r'cloud',
        r'terminal',
        r'users-between-lines',
    ]
    for pattern in icon_patterns:
        markdown = re.sub(pattern, '', markdown, flags=re.IGNORECASE)
    
    # 2. 清理UI按钮文本
    ui_patterns = [
        r'^Copy\s*$',
        r'^Copy as Markdown\s*$',
        r'^Back\s*$',
        r'Was this helpful\?.*$',
        r'^Table of contents\s*$',
        r'Open Markdown Ask Docs AI.*$',
        r'Open in Claude.*$',
        r'\[Edit this page\].*$',
        r'\[Request changes\].*$',
        # 页面底部导航
        r'\[Previous.*?\]\s*\(/.*?\)\s*\[Next.*?\]\s*\(/.*?\)',
        r'\[Previous.*?\]\s*\[Next.*?\]',
        # JS 碎片处理 (处理复制按钮残留)
        r'\]\\s\+/gm,.*$', 
        r'copying = (true|false).*$',
        r'setTimeout\(.*?2000\);\s*$',
    ]
    for pattern in ui_patterns:
        markdown = re.sub(pattern, '', markdown, flags=re.MULTILINE | re.IGNORECASE)
    
    # 2.1 修复常见编码问题（Windows-1252编码被误读为UTF-8）
    encoding_fixes = {
        'â€™': "'",      # 右单引号
        'â€œ': '"',      # 左双引号
        'â€': '"',       # 右双引号
        'â€"': '—',      # 破折号
        'â€"': '–',      # 短破折号
        'â€¦': '...',    # 省略号
        'Â ': ' ',       # 非断行空格
        '\xa0': ' ',     # 非断行空格
    }
    for wrong, right in encoding_fixes.items():
        markdown = markdown.replace(wrong, right)
    
    # 3. 清理空的标题（### 后面没内容）
    markdown = re.sub(r'^###\s*$', '', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s*$', '', markdown, flags=re.MULTILINE)
    
    # 4. 清理重复的主标题（连续两个相同的 # 标题）
    lines = markdown.split('\n')
    cleaned_lines = []
    prev_h1 = None
    for line in lines:
        if line.startswith('# ') and not line.startswith('## '):
            current_h1 = line.strip()
            if current_h1 == prev_h1:
                continue  # 跳过重复的H1
            prev_h1 = current_h1
        cleaned_lines.append(line)
    markdown = '\n'.join(cleaned_lines)
    
    # 5. 清理导航面包屑行（如 [Home](...) / [Get started](...) / ...）
    markdown = re.sub(r'^\s*\[Home\].*?/.*?/.*$', '', markdown, flags=re.MULTILINE)
    
    # 6. 清理开头的导航残留
    # 包括：纯链接列表、纯文本+链接列表（如Docker的侧边栏）
    lines = markdown.split('\n')
    content_start = 0
    consecutive_nav_lines = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # 跳过空行
        if not stripped:
            if consecutive_nav_lines > 0:
                consecutive_nav_lines += 1
            continue
        
        # 如果是标题行，从这里开始可能是正文
        if stripped.startswith('#'):
            # 但如果标题后面紧跟链接列表，可能还是导航
            if i + 1 < len(lines) and re.match(r'^\s*\*\s*\[.*?\]', lines[i + 1].strip()):
                consecutive_nav_lines += 1
                content_start = i + 1
                continue
            # 否则从标题开始是正文
            content_start = i
            break
        
        # 如果是纯链接行或列表项链接
        if re.match(r'^\s*\*?\s*\[.*?\]\(.*?\)\s*$', stripped):
            consecutive_nav_lines += 1
            content_start = i + 1
            continue
        
        # 如果是缩进的列表项（可能是子导航）
        if re.match(r'^\s{2,}\*\s+', line):
            consecutive_nav_lines += 1
            content_start = i + 1
            continue
        
        # 如果是短文本行（可能是导航分类标题如"Docker concepts"）
        if len(stripped) < 40 and not any(c in stripped for c in '.!?:'):
            # 短文本可能是导航类别
            consecutive_nav_lines += 1
            content_start = i + 1
            continue
        
        # 其他情况，认为是正文开始
        break
    
    # 如果连续导航行很多（超过10行），才清理
    if content_start > 0 and consecutive_nav_lines > 5:
        markdown = '\n'.join(lines[content_start:])
    
    # 7. 最终清理多余空行
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown.strip()


def extract_with_readability(html: str, url: str = "") -> ExtractedContent:
    """
    使用 readability 算法提取正文（兜底方案）
    
    Args:
        html: 完整HTML
        url: 页面URL
    
    Returns:
        ExtractedContent: 提取的内容
    """
    doc = Document(html)
    
    title = doc.title()
    content_html = doc.summary()
    
    # 解析提取的内容
    soup = BeautifulSoup(content_html, 'lxml')
    
    # 提取图片
    images = extract_images(soup, url)
    
    # 转为Markdown并清理
    markdown = html_to_markdown(content_html)
    markdown = clean_markdown(markdown)
    
    return ExtractedContent(
        title=title,
        markdown=markdown,
        images=images,
        url=url,
    )


def extract_with_adapter(
    html: str,
    adapter: FrameworkAdapter,
    url: str = "",
) -> ExtractedContent:
    """
    使用框架适配器提取内容
    
    Args:
        html: 完整HTML
        adapter: 框架适配器
        url: 页面URL
    
    Returns:
        ExtractedContent: 提取的内容
    """
    soup = BeautifulSoup(html, 'lxml')
    
    # 提取标题
    title = adapter.extract_title(soup)
    
    # 提取正文元素
    content_element = None
    if hasattr(adapter, 'extract_content'):
        content_element = adapter.extract_content(soup)
    
    if content_element is None:
        # 尝试用选择器
        selector = adapter.get_content_selector()
        for sel in selector.split(','):
            content_element = soup.select_one(sel.strip())
            if content_element:
                break
    
    if content_element is None:
        # 回退到 readability
        return extract_with_readability(html, url)
    
    # 提取图片
    images = extract_images(content_element, url)
    
    # 转为Markdown并清理
    content_html = str(content_element)
    markdown = html_to_markdown(content_html)
    markdown = clean_markdown(markdown)
    
    return ExtractedContent(
        title=title,
        markdown=markdown,
        images=images,
        url=url,
    )


def extract_content(
    html: str,
    url: str = "",
    framework: Optional[str] = None,
) -> ExtractedContent:
    """
    智能提取页面内容
    
    自动检测框架并使用对应适配器提取内容，
    如无法识别则使用通用算法。
    
    Args:
        html: 完整HTML
        url: 页面URL
        framework: 可选，指定框架名称跳过检测
    
    Returns:
        ExtractedContent: 提取的内容
    """
    # 检测或使用指定框架
    if framework is None:
        framework_info = detect_framework(html)
        framework = framework_info.name
    
    # 获取适配器
    adapter = get_adapter(framework)
    
    # 提取内容
    try:
        return extract_with_adapter(html, adapter, url)
    except Exception:
        # 出错时回退到 readability
        return extract_with_readability(html, url)
