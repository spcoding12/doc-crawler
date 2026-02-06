"""
框架检测模块

自动检测文档网站使用的框架类型：
- Docusaurus
- VuePress  
- MkDocs
- GitBook
"""

from bs4 import BeautifulSoup
from typing import Optional


class FrameworkInfo:
    """框架检测结果"""
    def __init__(self, name: str, version: Optional[str] = None, confidence: float = 1.0):
        self.name = name
        self.version = version
        self.confidence = confidence  # 检测置信度 0-1
    
    def __repr__(self):
        return f"FrameworkInfo(name='{self.name}', confidence={self.confidence})"


def detect_docusaurus(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 Docusaurus 框架"""
    indicators = [
        # Docusaurus v2/v3 特征
        ('meta[name="generator"]', lambda tag: 'docusaurus' in tag.get('content', '').lower()),
        ('html[data-theme]', lambda tag: soup.find('div', class_='theme-doc-sidebar-container') is not None),
        ('.theme-doc-sidebar-menu', lambda tag: True),
        ('.docusaurus', lambda tag: True),
        ('script', lambda tag: 'docusaurus' in str(tag)),
    ]
    
    for selector, check in indicators:
        elements = soup.select(selector)
        for el in elements:
            if check(el):
                # 尝试获取版本
                version = None
                meta = soup.find('meta', {'name': 'generator'})
                if meta and 'docusaurus' in meta.get('content', '').lower():
                    version = meta.get('content')
                return FrameworkInfo('docusaurus', version, confidence=0.9)
    
    return None


def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    indicators = [
        # VuePress 1.x
        ('.theme-default-content', lambda tag: True),
        ('.sidebar-links', lambda tag: True),
        # VuePress 2.x / VitePress
        ('.vp-doc', lambda tag: True),
        ('.VPSidebar', lambda tag: True),
        ('div[id="app"]', lambda tag: soup.find('div', class_='theme-container') is not None),
    ]
    
    for selector, check in indicators:
        elements = soup.select(selector)
        for el in elements:
            if check(el):
                return FrameworkInfo('vuepress', confidence=0.85)
    
    # 检查是否有 VuePress 特有的脚本
    scripts = soup.find_all('script')
    for script in scripts:
        src = script.get('src', '')
        text = script.string or ''
        if 'vuepress' in src.lower() or 'vuepress' in text.lower():
            return FrameworkInfo('vuepress', confidence=0.8)
    
    return None


def detect_mkdocs(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 MkDocs 框架"""
    indicators = [
        # Material for MkDocs
        ('.md-content', lambda tag: True),
        ('.md-sidebar', lambda tag: True),
        ('.md-nav', lambda tag: True),
        # 标准 MkDocs
        ('meta[name="generator"]', lambda tag: 'mkdocs' in tag.get('content', '').lower()),
        ('.wy-nav-content', lambda tag: True),  # ReadTheDocs theme
    ]
    
    for selector, check in indicators:
        elements = soup.select(selector)
        for el in elements:
            if check(el):
                version = None
                meta = soup.find('meta', {'name': 'generator'})
                if meta and 'mkdocs' in meta.get('content', '').lower():
                    version = meta.get('content')
                return FrameworkInfo('mkdocs', version, confidence=0.9)
    
    return None


def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    indicators = [
        # GitBook 特征
        ('.book-summary', lambda tag: True),
        ('.page-inner', lambda tag: True),
        ('.gitbook-root', lambda tag: True),
        ('meta[name="generator"]', lambda tag: 'gitbook' in tag.get('content', '').lower()),
    ]
    
    for selector, check in indicators:
        elements = soup.select(selector)
        for el in elements:
            if check(el):
                return FrameworkInfo('gitbook', confidence=0.85)
    
    # 检查链接特征
    if soup.find('link', href=lambda x: x and 'gitbook' in x.lower()):
        return FrameworkInfo('gitbook', confidence=0.7)
    
    return None


def detect_framework(html: str) -> FrameworkInfo:
    """
    检测页面使用的文档框架
    
    Args:
        html: HTML内容
    
    Returns:
        FrameworkInfo: 检测到的框架信息，如无法识别返回 'unknown'
    """
    soup = BeautifulSoup(html, 'lxml')
    
    # 按优先级检测
    detectors = [
        detect_docusaurus,
        detect_mkdocs,
        detect_vuepress,
        detect_gitbook,
    ]
    
    for detector in detectors:
        result = detector(soup)
        if result:
            return result
    
    return FrameworkInfo('unknown', confidence=0.0)


def get_framework_name(html: str) -> str:
    """简化接口：只返回框架名称"""
    return detect_framework(html).name
