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
    
    # 转为Markdown
    markdown = html_to_markdown(content_html)
    
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
    
    # 转为Markdown
    content_html = str(content_element)
    markdown = html_to_markdown(content_html)
    
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
