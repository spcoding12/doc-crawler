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
    # ⚡ Bolt Optimization: Fast attribute extraction first, avoids redundant DOM traversal
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'docusaurus' in meta.get('content', '').lower():
        return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    # ⚡ Bolt Optimization: Combine class checks into single pass
    if soup.find(class_=['theme-doc-sidebar-menu', 'docusaurus']):
        return FrameworkInfo('docusaurus', confidence=0.9)

    if soup.find('html', attrs={'data-theme': True}) and soup.find('div', class_='theme-doc-sidebar-container'):
        return FrameworkInfo('docusaurus', confidence=0.9)

    # ⚡ Bolt Optimization: Avoid str(tag) serialization which is extremely slow on large scripts
    for script in soup.find_all('script'):
        src = script.get('src', '')
        text = script.text or ''
        script_id = script.get('id', '')
        if 'docusaurus' in src.lower() or 'docusaurus' in text.lower() or 'docusaurus' in script_id.lower():
            return FrameworkInfo('docusaurus', confidence=0.9)

    return None


def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    # ⚡ Bolt Optimization: Combine class checks into single pass, avoid repetitive soup.select
    if soup.find(class_=['theme-default-content', 'sidebar-links', 'vp-doc', 'VPSidebar']):
        return FrameworkInfo('vuepress', confidence=0.85)

    app_div = soup.find('div', id='app')
    if app_div and soup.find('div', class_='theme-container'):
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
    # ⚡ Bolt Optimization: Extract generator first, avoiding early return bypass issues
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'mkdocs' in meta.get('content', '').lower():
        return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    # ⚡ Bolt Optimization: Combine class checks into single pass
    if soup.find(class_=['md-content', 'md-sidebar', 'md-nav', 'wy-nav-content']):
        return FrameworkInfo('mkdocs', confidence=0.9)
    
    return None


def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    # ⚡ Bolt Optimization: Check generator directly
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'gitbook' in meta.get('content', '').lower():
        return FrameworkInfo('gitbook', confidence=0.85)

    # ⚡ Bolt Optimization: Combine class checks into single pass
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
        text = script.string or ''
        if 'docsify' in src.lower() or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)
    
    # ⚡ Bolt Optimization: Avoid .select_one which forces CSS parsing overhead
    if soup.find(class_='sidebar-toggle'):
        body = soup.find('body')
        if body:
            body_class = body.get('class', [])
            if isinstance(body_class, list):
                body_class = ' '.join(body_class)
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
