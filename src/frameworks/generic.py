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
        如果找不到侧边栏，则从所有内部链接中提取
        """
        links = []
        seen_urls = set()
        
        # 解析基础URL信息
        parsed_base = urlparse(base_url)
        base_domain = parsed_base.netloc
        base_path = parsed_base.path.rstrip('/')
        
        # 第一步：尝试从侧边栏选择器中提取
        for selector in self.SIDEBAR_SELECTORS:
            elements = soup.select(selector)
            if len(elements) > 3:
                for link in elements[:2000]:
                    href = link.get('href', '')
                    if not href or href.startswith('#') or href.startswith('javascript:'):
                        continue
                    
                    full_url = urljoin(base_url, href)
                    parsed_url = urlparse(full_url)
                    
                    # 只保留同域名的链接
                    if parsed_url.netloc != base_domain:
                        continue
                    
                    # 只保留同路径前缀的链接（限制在当前模块内）
                    if base_path and not parsed_url.path.startswith(base_path):
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
        
        # 第二步：如果侧边栏链接太少，从所有内部链接中提取（兜底）
        if len(links) < 10:
            links = []
            seen_urls = set()
            
            all_links = soup.find_all('a', href=True)
            for link in all_links:
                href = link.get('href', '')
                if not href or href.startswith('#') or href.startswith('javascript:'):
                    continue
                
                full_url = urljoin(base_url, href)
                parsed_url = urlparse(full_url)
                
                # 只保留同域名的链接
                if parsed_url.netloc != base_domain:
                    continue
                
                # 只保留同路径前缀的链接（避免跳到不相关的文档）
                if base_path and not parsed_url.path.startswith(base_path):
                    continue
                
                normalized_url = full_url.rstrip('/')
                if normalized_url in seen_urls:
                    continue
                seen_urls.add(normalized_url)
                
                title = link.get_text(strip=True)
                # 过滤无效标题
                if not title or len(title) > 100 or len(title) < 2:
                    continue
                # 过滤明显的非文档链接
                if any(x in title.lower() for x in ['login', 'sign in', 'register', 'search']):
                    continue
                
                links.append({
                    'url': full_url,
                    'title': title,
                    'level': 0,
                })
            
            # 限制数量
            links = links[:5000]
        
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
