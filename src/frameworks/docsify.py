"""
Docsify 框架适配器

Docsify 是一个纯前端文档框架，内容从 .md 文件动态加载。
核心特点：
1. 使用 Hash 路由（#/page）
2. 侧边栏定义在 _sidebar.md 中
3. 内容可直接请求原始 .md 文件获取（无需 JS 渲染）
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import requests
from .base import FrameworkAdapter


class DocsifyAdapter(FrameworkAdapter):
    """Docsify 文档框架适配器"""
    
    name = "docsify"
    
    # Docsify 的内容选择器（渲染后的 DOM）
    CONTENT_SELECTORS = [
        '.markdown-section',
        '#main',
        'section.content',
        'article',
    ]
    
    @classmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """检测是否为 Docsify 网站"""
        # 检查 script 标签中是否引用了 docsify
        for script in soup.find_all('script'):
            src = script.get('src', '')
            text = script.string or ''
            if 'docsify' in src.lower() or 'docsify' in text.lower():
                return True
        
        # 检查 window.$docsify 配置
        for script in soup.find_all('script'):
            text = script.string or ''
            if '$docsify' in text or 'window.docsify' in text.lower():
                return True
        
        # 检查特征元素
        indicators = [
            '#__app',           # Docsify 默认挂载点
            '.sidebar-toggle',  # Docsify 侧边栏开关
            'body.ready',       # Docsify body 类
        ]
        for selector in indicators:
            if soup.select_one(selector):
                return True
        
        # 检查 body class
        body = soup.find('body')
        if body:
            body_class = ' '.join(body.get('class', []))
            if 'ready' in body_class and 'sticky' in body_class:
                return True
        
        return False
    
    def get_sidebar_links(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """
        提取 Docsify 侧边栏导航链接。
        
        Docsify 的侧边栏通过 _sidebar.md 文件定义，
        我们直接请求该文件并解析 Markdown 链接。
        """
        # 从 base_url 构建 _sidebar.md 的 URL
        sidebar_url = self._build_sidebar_url(base_url)
        
        if sidebar_url:
            links = self._fetch_and_parse_sidebar(sidebar_url, base_url)
            if links:
                return links
        
        # 回退：从已渲染的 DOM 中提取侧边栏链接
        return self._extract_from_dom(soup, base_url)
    
    def _build_sidebar_url(self, base_url: str) -> str:
        """
        构建 _sidebar.md 的完整 URL。
        
        例如：
        - base_url = https://example.com/docs/ -> https://example.com/docs/_sidebar.md
        - base_url = https://example.com/docs#/openapi -> https://example.com/docs/_sidebar.md
        """
        parsed = urlparse(base_url)
        
        # 去掉 hash 部分，得到真实的服务器路径
        path = parsed.path
        if not path.endswith('/'):
            path += '/'
        
        sidebar_path = path + '_sidebar.md'
        
        return f"{parsed.scheme}://{parsed.netloc}{sidebar_path}"
    
    def _fetch_and_parse_sidebar(self, sidebar_url: str, base_url: str) -> list[dict]:
        """
        请求 _sidebar.md 并解析其中的链接。
        
        _sidebar.md 格式示例：
        - Getting Started
          - [OpenAPI](openapi.md)
          - [Guide](guide.md)
        - API Reference
          - [Users](api/users.md)
        """
        try:
            from src.fetcher import DEFAULT_HEADERS
            response = requests.get(sidebar_url, headers=DEFAULT_HEADERS, timeout=10)
            if response.status_code != 200:
                return []
            
            content = response.text
            return self._parse_sidebar_markdown(content, base_url)
        except Exception:
            return []
    
    def _parse_sidebar_markdown(self, markdown_content: str, base_url: str) -> list[dict]:
        """
        解析 _sidebar.md 中的 Markdown 链接。
        
        支持格式：
        - [Title](path.md)
        - [Title](path)
        """
        links = []
        seen = set()
        
        # 获取基础目录 URL（去除 hash 部分）
        parsed = urlparse(base_url)
        base_dir = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if not base_dir.endswith('/'):
            base_dir += '/'
        
        for line in markdown_content.split('\n'):
            # 匹配 Markdown 链接：[title](url)
            match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
            if not match:
                continue
            
            title = match.group(1).strip()
            href = match.group(2).strip()
            
            # 跳过纯锚点链接
            if href.startswith('#'):
                continue
            
            # 跳过外部链接
            if href.startswith(('http://', 'https://')):
                link_parsed = urlparse(href)
                if link_parsed.netloc != parsed.netloc:
                    continue
            
            # 计算缩进层级
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            level = indent // 2
            
            # 确保 href 以 .md 结尾（Docsify 内容文件）
            md_href = href
            if not md_href.endswith('.md'):
                md_href += '.md'
            
            # 构建完整的 .md 文件 URL（用于直接请求内容）
            full_md_url = urljoin(base_dir, md_href)
            
            if full_md_url in seen:
                continue
            seen.add(full_md_url)
            
            links.append({
                'url': full_md_url,
                'title': title,
                'level': level,
                'is_docsify_md': True,  # 标记为 Docsify 的 MD 文件，main.py 中会特殊处理
            })
        
        return links
    
    def _extract_from_dom(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """回退方案：从渲染后的 DOM 中提取侧边栏链接"""
        links = []
        seen = set()
        
        sidebar = soup.select_one('.sidebar-nav') or soup.select_one('.sidebar')
        if not sidebar:
            return links
        
        for a_tag in sidebar.find_all('a', href=True):
            href = a_tag.get('href', '')
            title = a_tag.get_text(strip=True)
            
            if not href or not title:
                continue
            
            # Docsify 的 hash 链接格式：#/page
            if href.startswith('#/'):
                # 转换为 .md 文件 URL
                md_path = href[2:]  # 去掉 #/
                if '?id=' in md_path:
                    md_path = md_path.split('?id=')[0]
                if not md_path.endswith('.md'):
                    md_path += '.md'
                
                parsed = urlparse(base_url)
                base_dir = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                if not base_dir.endswith('/'):
                    base_dir += '/'
                
                full_url = urljoin(base_dir, md_path)
            else:
                full_url = urljoin(base_url, href)
            
            if full_url in seen:
                continue
            seen.add(full_url)
            
            links.append({
                'url': full_url,
                'title': title,
                'level': 0,
                'is_docsify_md': True,
            })
        
        return links
    
    def get_content_selector(self) -> str:
        """返回正文内容的CSS选择器"""
        return ', '.join(self.CONTENT_SELECTORS)
