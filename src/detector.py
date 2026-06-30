"""
框架检测模块

自动检测文档网站使用的框架类型：
- Docusaurus
- VuePress  
- MkDocs
- GitBook
- Docsify
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
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta:
        content = meta.get('content', '').lower()
        if 'docusaurus' in content:
            return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    if soup.find('html', attrs={'data-theme': True}):
        if soup.find('div', class_='theme-doc-sidebar-container'):
            return FrameworkInfo('docusaurus', confidence=0.9)

    if soup.find(class_=['theme-doc-sidebar-menu', 'docusaurus']):
        return FrameworkInfo('docusaurus', confidence=0.9)

    for script in soup.find_all('script'):
        src = script.get('src', '').lower()
        text = script.text.lower()
        if 'docusaurus' in src or 'docusaurus' in text:
            return FrameworkInfo('docusaurus', confidence=0.9)

    return None


def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    if soup.find(class_=['theme-default-content', 'sidebar-links', 'vp-doc', 'VPSidebar']):
        return FrameworkInfo('vuepress', confidence=0.85)

    app_div = soup.find('div', id='app')
    if app_div and soup.find('div', class_='theme-container'):
        return FrameworkInfo('vuepress', confidence=0.85)
    
    for script in soup.find_all('script'):
        src = script.get('src', '').lower()
        text = script.text.lower()
        if 'vuepress' in src or 'vuepress' in text:
            return FrameworkInfo('vuepress', confidence=0.8)
    
    return None


def detect_mkdocs(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 MkDocs 框架"""
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta:
        content = meta.get('content', '').lower()
        if 'mkdocs' in content:
            return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    if soup.find(class_=['md-content', 'md-sidebar', 'md-nav', 'wy-nav-content']):
        return FrameworkInfo('mkdocs', confidence=0.9)

    return None


def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'gitbook' in meta.get('content', '').lower():
        return FrameworkInfo('gitbook', confidence=0.85)

    if soup.find(class_=['book-summary', 'page-inner', 'gitbook-root']):
        return FrameworkInfo('gitbook', confidence=0.85)

    if soup.find('link', href=lambda x: x and 'gitbook' in x.lower()):
        return FrameworkInfo('gitbook', confidence=0.7)
    
    return None


def detect_docsify(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 Docsify 框架"""
    for script in soup.find_all('script'):
        src = script.get('src', '').lower()
        text = script.text.lower()
        if 'docsify' in src or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)
    
    if soup.find(class_='sidebar-toggle'):
        body = soup.find('body')
        if body and 'ready' in body.get('class', []):
            return FrameworkInfo('docsify', confidence=0.8)
    
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
        detect_docsify,
    ]
    
    for detector in detectors:
        result = detector(soup)
        if result:
            return result
    
    return FrameworkInfo('unknown', confidence=0.0)


def get_framework_name(html: str) -> str:
    """简化接口：只返回框架名称"""
    return detect_framework(html).name
