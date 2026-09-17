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
    # ⚡ Bolt: Use .find() instead of .select() and check generator first to ensure version is extracted
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'docusaurus' in meta.get('content', '').lower():
        return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    # ⚡ Bolt: Single pass check for specific classes
    if soup.find(class_=['theme-doc-sidebar-menu', 'docusaurus']) or soup.find('div', class_='theme-doc-sidebar-container'):
        return FrameworkInfo('docusaurus', confidence=0.9)

    # ⚡ Bolt: Use .text instead of str(tag) to avoid serialization overhead
    for script in soup.find_all('script'):
        if 'docusaurus' in script.text.lower() or 'docusaurus' in script.get('src', '').lower():
             return FrameworkInfo('docusaurus', confidence=0.9)

    return None


def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    # ⚡ Bolt: Use find with class_ list for single pass fast traversal
    if soup.find(class_=['theme-default-content', 'sidebar-links', 'vp-doc', 'VPSidebar']):
        return FrameworkInfo('vuepress', confidence=0.85)

    if soup.find('div', id='app') and soup.find('div', class_='theme-container'):
        return FrameworkInfo('vuepress', confidence=0.85)

    # ⚡ Bolt: Use script.text instead of script.string
    scripts = soup.find_all('script')
    for script in scripts:
        src = script.get('src', '')
        text = script.text
        if 'vuepress' in src.lower() or 'vuepress' in text.lower():
            return FrameworkInfo('vuepress', confidence=0.8)
    
    return None


def detect_mkdocs(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 MkDocs 框架"""
    # ⚡ Bolt: Check generator first for early exit and version extraction
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'mkdocs' in meta.get('content', '').lower():
        return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    # ⚡ Bolt: Single pass check for specific classes
    if soup.find(class_=['md-content', 'md-sidebar', 'md-nav', 'wy-nav-content']):
        return FrameworkInfo('mkdocs', confidence=0.9)

    return None


def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    # ⚡ Bolt: Check generator first
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'gitbook' in meta.get('content', '').lower():
        return FrameworkInfo('gitbook', confidence=0.85)

    # ⚡ Bolt: Use find with class_ list for fast check
    if soup.find(class_=['book-summary', 'page-inner', 'gitbook-root']):
        return FrameworkInfo('gitbook', confidence=0.85)
    
    # 检查链接特征
    if soup.find('link', href=lambda x: x and 'gitbook' in x.lower()):
        return FrameworkInfo('gitbook', confidence=0.7)
    
    return None


def detect_docsify(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 Docsify 框架"""
    # 检查 script 标签中是否引用了 docsify
    for script in soup.find_all('script'):
        src = script.get('src', '')
        # ⚡ Bolt: Use script.text instead of script.string
        text = script.text
        if 'docsify' in src.lower() or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)
    
    # 检查特征元素
    # ⚡ Bolt: Replace select_one with find
    if soup.find(class_='sidebar-toggle'):
        body = soup.find('body')
        if body:
            body_class = ' '.join(body.get('class', []))
            if 'ready' in body_class:
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
