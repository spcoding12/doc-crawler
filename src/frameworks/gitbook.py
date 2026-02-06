"""
GitBook 框架适配器

支持 GitBook 文档网站
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from .base import FrameworkAdapter


class GitBookAdapter(FrameworkAdapter):
    """GitBook 文档框架适配器"""
    
    name = "gitbook"
    
    # 侧边栏选择器
    SIDEBAR_SELECTORS = [
        '.book-summary a',
        '.summary a',
        'nav.book-summary a',
        '.gitbook-root aside a',
        '[data-testid="page.desktopTableOfContents"] a',
    ]
    
    # 内容选择器
    CONTENT_SELECTORS = [
        '.page-inner .normal',
        '.page-inner',
        '.markdown-section',
        '.book-body .body-inner',
        '[data-testid="page.contentEditor"]',
        'main',
    ]
    
    @classmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """检测是否为 GitBook 网站"""
        # 检查 meta generator
        meta = soup.find('meta', {'name': 'generator'})
        if meta and 'gitbook' in meta.get('content', '').lower():
            return True
        
        # 检查特征类名
        indicators = [
            '.book-summary',
            '.gitbook-root',
            '.page-inner',
            '.markdown-section',
        ]
        for selector in indicators:
            if soup.select_one(selector):
                return True
        
        # 检查链接
        for link in soup.find_all('link'):
            href = link.get('href', '')
            if 'gitbook' in href.lower():
                return True
        
        return False
    
    def get_sidebar_links(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """提取侧边栏导航链接"""
        links = []
        seen_urls = set()
        
        for selector in self.SIDEBAR_SELECTORS:
            elements = soup.select(selector)
            if elements:
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
                    if not title:
                        continue
                    
                    # 计算层级
                    level = 0
                    parent = link.parent
                    while parent:
                        if parent.name in ('ul', 'ol', 'li'):
                            level += 1
                        parent = parent.parent
                        if level > 5:
                            break
                    
                    links.append({
                        'url': full_url,
                        'title': title,
                        'level': max(0, level // 2),
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
