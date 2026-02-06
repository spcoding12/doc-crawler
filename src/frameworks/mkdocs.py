"""
MkDocs 框架适配器

支持 MkDocs 和 Material for MkDocs 主题
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from .base import FrameworkAdapter


class MkDocsAdapter(FrameworkAdapter):
    """MkDocs 文档框架适配器"""
    
    name = "mkdocs"
    
    # 侧边栏选择器
    SIDEBAR_SELECTORS = [
        # Material for MkDocs
        '.md-nav--primary a',
        '.md-nav a',
        '.md-sidebar a',
        # ReadTheDocs theme
        '.wy-menu a',
        '.toctree-wrapper a',
        # 标准 MkDocs
        'nav a',
    ]
    
    # 内容选择器
    CONTENT_SELECTORS = [
        # Material for MkDocs
        '.md-content article',
        '.md-content',
        # ReadTheDocs theme
        '.wy-nav-content',
        '.document',
        # 标准 MkDocs
        'article',
        '.content',
    ]
    
    @classmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """检测是否为 MkDocs 网站"""
        # 检查 meta generator
        meta = soup.find('meta', {'name': 'generator'})
        if meta and 'mkdocs' in meta.get('content', '').lower():
            return True
        
        # 检查特征类名
        indicators = [
            '.md-content',
            '.md-sidebar',
            '.md-nav',
            '.wy-nav-content',
        ]
        for selector in indicators:
            if soup.select_one(selector):
                return True
        
        return False
    
    def get_sidebar_links(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """提取侧边栏导航链接"""
        links = []
        seen_urls = set()
        
        for selector in self.SIDEBAR_SELECTORS:
            elements = soup.select(selector)
            if len(elements) > 3:  # 至少几个链接
                for link in elements:
                    href = link.get('href', '')
                    if not href or href.startswith('#') or href.startswith('javascript:'):
                        continue
                    
                    full_url = urljoin(base_url, href)
                    
                    base_domain = urlparse(base_url).netloc
                    if urlparse(full_url).netloc != base_domain:
                        continue
                    
                    normalized_url = full_url.rstrip('/')
                    if normalized_url in seen_urls:
                        continue
                    seen_urls.add(normalized_url)
                    
                    title = link.get_text(strip=True)
                    if not title or len(title) > 100:
                        continue
                    
                    # 计算层级
                    level = 0
                    parent = link.parent
                    while parent:
                        if parent.name in ('ul', 'ol') or 'md-nav' in ' '.join(parent.get('class', [])):
                            level += 1
                        parent = parent.parent
                        if level > 5:
                            break
                    
                    links.append({
                        'url': full_url,
                        'title': title,
                        'level': max(0, level - 1),
                    })
                
                if links:
                    break
        
        return links
    
    def get_content_selector(self) -> str:
        """返回正文内容的CSS选择器"""
        return ', '.join(self.CONTENT_SELECTORS)
    
    def extract_content(self, soup: BeautifulSoup) -> BeautifulSoup | None:
        """提取正文内容元素"""
        for selector in self.CONTENT_SELECTORS:
            content = soup.select_one(selector)
            if content:
                return content
        return None
