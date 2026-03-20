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
    # ⚡ Bolt Optimization: Use O(1) attribute lookup instead of slow CSS selection
    meta = soup.find('meta', {'name': 'generator'})
    if meta and 'docusaurus' in meta.get('content', '').lower():
        return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    # ⚡ Bolt Optimization: Replace soup.select with faster soup.find(class_=...)
    if soup.find(class_='theme-doc-sidebar-menu') or soup.find(class_='docusaurus'):
        return FrameworkInfo('docusaurus', None, confidence=0.9)

    html_tag = soup.find('html', {'data-theme': True})
    if html_tag and soup.find('div', class_='theme-doc-sidebar-container'):
        return FrameworkInfo('docusaurus', None, confidence=0.9)

    for script in soup.find_all('script'):
        if 'docusaurus' in str(script):
            return FrameworkInfo('docusaurus', None, confidence=0.9)
    
    return None


def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    # ⚡ Bolt Optimization: Replace soup.select with faster soup.find(class_=...)
    if (soup.find(class_='theme-default-content') or
        soup.find(class_='sidebar-links') or
        soup.find(class_='vp-doc') or
        soup.find(class_='VPSidebar')):
        return FrameworkInfo('vuepress', confidence=0.85)

    app_div = soup.find('div', id='app')
    if app_div and soup.find('div', class_='theme-container'):
        return FrameworkInfo('vuepress', confidence=0.85)
    
    # 检查是否有 VuePress 特有的脚本
    for script in soup.find_all('script'):
        src = script.get('src', '')
        text = script.string or ''
        if 'vuepress' in src.lower() or 'vuepress' in text.lower():
            return FrameworkInfo('vuepress', confidence=0.8)
    
    return None


def detect_mkdocs(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 MkDocs 框架"""
    # ⚡ Bolt Optimization: Check meta tag first
    meta = soup.find('meta', {'name': 'generator'})
    if meta and 'mkdocs' in meta.get('content', '').lower():
        return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    # ⚡ Bolt Optimization: Replace soup.select with faster soup.find(class_=...)
    if (soup.find(class_='md-content') or
        soup.find(class_='md-sidebar') or
        soup.find(class_='md-nav') or
        soup.find(class_='wy-nav-content')):
        return FrameworkInfo('mkdocs', None, confidence=0.9)
    
    return None


def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    # ⚡ Bolt Optimization: Check meta tag first
    meta = soup.find('meta', {'name': 'generator'})
    if meta and 'gitbook' in meta.get('content', '').lower():
        return FrameworkInfo('gitbook', confidence=0.85)

    # ⚡ Bolt Optimization: Replace soup.select with faster soup.find(class_=...)
    if (soup.find(class_='book-summary') or
        soup.find(class_='page-inner') or
        soup.find(class_='gitbook-root')):
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
        text = script.string or ''
        if 'docsify' in src.lower() or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)
    
    # ⚡ Bolt Optimization: Replace soup.select_one with faster soup.find(class_=...)
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
