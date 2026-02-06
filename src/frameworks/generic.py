"""
通用框架适配器

用于处理无法识别框架的网站，使用通用算法提取内容
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from .base import FrameworkAdapter


class GenericAdapter(FrameworkAdapter):
    """通用文档框架适配器（兜底方案）"""
    
    name = "generic"
    
    # 常见的侧边栏选择器
    SIDEBAR_SELECTORS = [
        'nav a',
        'aside a',
        '.sidebar a',
        '.nav a',
        '.menu a',
        '[role="navigation"] a',
    ]
    
    # 常见的内容选择器
    CONTENT_SELECTORS = [
        'main',
        'article', 
        '.content',
        '.main-content',
        '#content',
        '.post-content',
        '.article-content',
        '.documentation',
        '.docs-content',
    ]
    
    @classmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """通用适配器始终返回True作为兜底"""
        return True
    
    def get_sidebar_links(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """
        尝试从常见位置提取导航链接
        """
        links = []
        seen_urls = set()
        
        # 尝试找侧边栏
        for selector in self.SIDEBAR_SELECTORS:
            elements = soup.select(selector)
            if len(elements) > 3:  # 至少有几个链接才认为是导航
                for link in elements[:50]:  # 限制数量
                    href = link.get('href', '')
                    if not href or href.startswith('#') or href.startswith('javascript:'):
                        continue
                    
                    full_url = urljoin(base_url, href)
                    
                    # 只保留同域名
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
                    
                    links.append({
                        'url': full_url,
                        'title': title,
                        'level': 0,
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
                # 检查内容是否足够
                text = content.get_text(strip=True)
                if len(text) > 200:  # 至少200字符
                    return content
        return None
