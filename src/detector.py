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
    # 1. meta generator
    meta = soup.find('meta', attrs={'name': 'generator', 'content': lambda c: c and 'docusaurus' in c.lower()})
    if meta:
        return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    # 2. html data-theme
    if soup.find('html', attrs={'data-theme': True}) and soup.find('div', class_='theme-doc-sidebar-container'):
        return FrameworkInfo('docusaurus', confidence=0.9)

    # 3. classes
    if soup.find(class_=['theme-doc-sidebar-menu', 'docusaurus']):
        return FrameworkInfo('docusaurus', confidence=0.9)

    # 4. scripts
    for script in soup.find_all('script'):
        if 'docusaurus' in script.text.lower() or 'docusaurus' in script.get('src', '').lower():
            return FrameworkInfo('docusaurus', confidence=0.9)

    return None

def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    # 1. classes
    if soup.find(class_=['theme-default-content', 'sidebar-links', 'vp-doc', 'VPSidebar']):
        return FrameworkInfo('vuepress', confidence=0.85)

    # 2. div app
    if soup.find('div', id='app') and soup.find('div', class_='theme-container'):
        return FrameworkInfo('vuepress', confidence=0.85)
    
    # 3. scripts
    for script in soup.find_all('script'):
        src = script.get('src', '')
        text = script.text or ''
        if 'vuepress' in src.lower() or 'vuepress' in text.lower():
            return FrameworkInfo('vuepress', confidence=0.8)

    return None

def detect_mkdocs(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 MkDocs 框架"""
    # 1. classes
    if soup.find(class_=['md-content', 'md-sidebar', 'md-nav', 'wy-nav-content']):
        version = None
        meta = soup.find('meta', attrs={'name': 'generator'})
        if meta and 'mkdocs' in meta.get('content', '').lower():
            version = meta.get('content')
        return FrameworkInfo('mkdocs', version, confidence=0.9)

    # 2. meta generator
    meta = soup.find('meta', attrs={'name': 'generator', 'content': lambda c: c and 'mkdocs' in c.lower()})
    if meta:
        return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    return None

def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    # 1. classes
    if soup.find(class_=['book-summary', 'page-inner', 'gitbook-root']):
        return FrameworkInfo('gitbook', confidence=0.85)

    # 2. meta generator
    meta = soup.find('meta', attrs={'name': 'generator', 'content': lambda c: c and 'gitbook' in c.lower()})
    if meta:
        return FrameworkInfo('gitbook', confidence=0.85)

    # 3. link
    if soup.find('link', href=lambda x: x and 'gitbook' in x.lower()):
        return FrameworkInfo('gitbook', confidence=0.7)

    return None

def detect_docsify(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 Docsify 框架"""
    # 1. scripts
    for script in soup.find_all('script'):
        src = script.get('src', '')
        text = script.text or ''
        if 'docsify' in src.lower() or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)

    # 2. class
    if soup.find(class_='sidebar-toggle'):
        body = soup.find('body')
        if body and 'ready' in body.get('class', []):
            return FrameworkInfo('docsify', confidence=0.8)

    return None

def detect_framework(html: str) -> FrameworkInfo:
    """
    检测页面使用的文档框架
    """
    soup = BeautifulSoup(html, 'lxml')
    
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
