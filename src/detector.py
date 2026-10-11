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
    # ⚡ Bolt Optimization: Use direct .find() with class lists and attribute lookups
    # instead of expensive CSS selectors (.select) and str() conversions to speed up traversal.
    
    # Check meta tags first as they are quick and give exact version
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'docusaurus' in meta.get('content', '').lower():
        return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    # Check classes with single-pass OR
    if soup.find(class_=['theme-doc-sidebar-container', 'theme-doc-sidebar-menu', 'docusaurus']):
        return FrameworkInfo('docusaurus', confidence=0.9)

    # Check scripts without str(tag) serialization overhead
    for script in soup.find_all('script'):
        if script.get('id') == '__docusaurus':
            return FrameworkInfo('docusaurus', confidence=0.9)
        text = script.string or ''
        if 'docusaurus' in text.lower():
            return FrameworkInfo('docusaurus', confidence=0.9)

    return None


def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 VuePress 框架"""
    # ⚡ Bolt Optimization: Replace multiple .select() CSS queries with a single-pass
    # .find(class_=[...]) for O(1) attribute checks per node during traversal.
    
    classes = ['theme-default-content', 'sidebar-links', 'vp-doc', 'VPSidebar', 'theme-container']
    if soup.find(class_=classes):
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
    # ⚡ Bolt Optimization: Use direct meta tag retrieval first (prevent redundant searches)
    # and single-pass class OR logic instead of array of CSS selector evaluation.
    
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'mkdocs' in meta.get('content', '').lower():
        return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    classes = ['md-content', 'md-sidebar', 'md-nav', 'wy-nav-content']
    if soup.find(class_=classes):
        return FrameworkInfo('mkdocs', confidence=0.9)

    return None


def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 GitBook 框架"""
    # ⚡ Bolt Optimization: Replaced multiple .select() calls with native .find() and
    # list of classes for single-pass existence check. Evaluates meta directly.
    
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'gitbook' in meta.get('content', '').lower():
        return FrameworkInfo('gitbook', confidence=0.85)

    classes = ['book-summary', 'page-inner', 'gitbook-root']
    if soup.find(class_=classes):
        return FrameworkInfo('gitbook', confidence=0.85)

    # 检查链接特征
    if soup.find('link', href=lambda x: x and 'gitbook' in x.lower()):
        return FrameworkInfo('gitbook', confidence=0.7)
    
    return None


def detect_docsify(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    """检测 Docsify 框架"""
    # ⚡ Bolt Optimization: Removed .select_one() for CSS parsing in favor of native .find().

    # 检查 script 标签中是否引用了 docsify
    for script in soup.find_all('script'):
        src = script.get('src', '')
        text = script.string or ''
        if 'docsify' in src.lower() or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)
    
    # 检查特征元素
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
