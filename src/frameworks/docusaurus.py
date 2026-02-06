"""
Docusaurus 框架适配器

支持 Docusaurus v2/v3 文档网站
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from .base import FrameworkAdapter


class DocusaurusAdapter(FrameworkAdapter):
    """Docusaurus 文档框架适配器"""
    
    name = "docusaurus"
    
    # 侧边栏选择器（按优先级）
    SIDEBAR_SELECTORS = [
        '.theme-doc-sidebar-menu a',
        '.menu__list a',
        '.sidebar-menu a',
        'nav.sidebar a',
    ]
    
    # 内容选择器（按优先级）
    CONTENT_SELECTORS = [
        'article.markdown',
        '.markdown',
        '.theme-doc-markdown',
        'main article',
        '.docMainContainer article',
    ]
    
    @classmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """检测是否为 Docusaurus 网站"""
        # 检查 meta generator
        meta = soup.find('meta', {'name': 'generator'})
        if meta and 'docusaurus' in meta.get('content', '').lower():
            return True
        
        # 检查特征类名
        indicators = [
            '.theme-doc-sidebar-container',
            '.docusaurus',
            '.theme-doc-markdown',
            '[data-theme]',
        ]
        for selector in indicators:
            if soup.select_one(selector):
                return True
        
        # 检查脚本中是否包含 docusaurus
        for script in soup.find_all('script'):
            if 'docusaurus' in (script.get('src', '') + (script.string or '')).lower():
                return True
        
        return False
    
    def get_sidebar_links(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """
        提取侧边栏导航链接
        
        Returns:
            list[dict]: [{url, title, level}, ...]
        """
        links = []
        seen_urls = set()
        
        # 尝试不同的选择器
        sidebar_element = None
        for selector in self.SIDEBAR_SELECTORS:
            elements = soup.select(selector)
            if elements:
                # 找到侧边栏容器
                sidebar_element = elements
                break
        
        if not sidebar_element:
            # 尝试找通用的侧边栏
            sidebar_element = soup.select('aside a, nav a')
        
        for link in sidebar_element or []:
            href = link.get('href', '')
            if not href or href.startswith('#') or href.startswith('javascript:'):
                continue
            
            # 构建完整URL
            full_url = urljoin(base_url, href)
            
            # 只保留同域名的链接
            base_domain = urlparse(base_url).netloc
            link_domain = urlparse(full_url).netloc
            if link_domain != base_domain:
                continue
            
            # 去重
            normalized_url = full_url.rstrip('/')
            if normalized_url in seen_urls:
                continue
            seen_urls.add(normalized_url)
            
            # 获取标题
            title = link.get_text(strip=True)
            if not title:
                continue
            
            # 计算层级（基于嵌套深度）
            level = 0
            parent = link.parent
            while parent:
                if parent.name in ('ul', 'ol'):
                    level += 1
                parent = parent.parent
                if level > 5:  # 防止无限循环
                    break
            
            links.append({
                'url': full_url,
                'title': title,
                'level': max(0, level - 1),  # 调整层级
            })
        
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
    
    def extract_title(self, soup: BeautifulSoup) -> str:
        """提取页面标题"""
        # 优先使用 h1
        h1 = soup.select_one('article h1, .markdown h1, main h1')
        if h1:
            return h1.get_text(strip=True)
        
        # 尝试 title 标签
        title = soup.find('title')
        if title:
            text = title.get_text(strip=True)
            # 移除网站名称后缀
            if ' | ' in text:
                text = text.split(' | ')[0]
            elif ' - ' in text:
                text = text.split(' - ')[0]
            return text
        
        return "Untitled"
