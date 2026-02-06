"""
VuePress 框架适配器

支持 VuePress 1.x/2.x 和 VitePress 文档网站
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from .base import FrameworkAdapter


class VuePressAdapter(FrameworkAdapter):
    """VuePress 文档框架适配器"""
    
    name = "vuepress"
    
    # 侧边栏选择器（按优先级）
    SIDEBAR_SELECTORS = [
        # VuePress 1.x
        '.sidebar-links a',
        '.sidebar a',
        # VuePress 2.x  
        '.vp-sidebar a',
        '.sidebar-link',
        # VitePress
        '.VPSidebar a',
        '.VPSidebarItem a',
    ]
    
    # 内容选择器（按优先级）
    CONTENT_SELECTORS = [
        # VuePress 1.x
        '.theme-default-content',
        '.page-content',
        # VuePress 2.x
        '.vp-doc',
        # VitePress
        '.VPDoc .content',
        'main .vp-doc',
    ]
    
    @classmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """检测是否为 VuePress 网站"""
        # 检查特征类名
        indicators = [
            '.theme-default-content',
            '.sidebar-links',
            '.vp-sidebar',
            '.VPSidebar',
            '.vp-doc',
            '#app.theme-container',
        ]
        for selector in indicators:
            if soup.select_one(selector):
                return True
        
        # 检查脚本
        for script in soup.find_all('script'):
            src = script.get('src', '') + (script.string or '')
            if 'vuepress' in src.lower() or 'vitepress' in src.lower():
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
                    
                    # 只保留同域名
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
                        if parent.name in ('ul', 'ol'):
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
