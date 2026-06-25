import time
from bs4 import BeautifulSoup
from typing import Optional
from src.detector import detect_framework as detect_framework_orig

class FrameworkInfo:
    def __init__(self, name: str, version: Optional[str] = None, confidence: float = 1.0):
        self.name = name
        self.version = version
        self.confidence = confidence

def detect_docusaurus(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'docusaurus' in meta.get('content', '').lower():
        return FrameworkInfo('docusaurus', meta.get('content'), confidence=0.9)

    if soup.find(class_=['theme-doc-sidebar-menu', 'docusaurus']):
        return FrameworkInfo('docusaurus', confidence=0.9)

    if soup.find('html', attrs={'data-theme': True}) and soup.find('div', class_='theme-doc-sidebar-container'):
        return FrameworkInfo('docusaurus', confidence=0.9)

    for script in soup.find_all('script'):
        if 'docusaurus' in (script.get('src', '').lower() + script.text.lower()):
            return FrameworkInfo('docusaurus', confidence=0.9)
    return None

def detect_vuepress(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    if soup.find(class_=['theme-default-content', 'sidebar-links', 'vp-doc', 'VPSidebar']):
        return FrameworkInfo('vuepress', confidence=0.85)

    if soup.find('div', id='app') and soup.find('div', class_='theme-container'):
        return FrameworkInfo('vuepress', confidence=0.85)

    for script in soup.find_all('script'):
        src = script.get('src', '').lower()
        text = script.text.lower()
        if 'vuepress' in src or 'vuepress' in text:
            return FrameworkInfo('vuepress', confidence=0.8)
    return None

def detect_mkdocs(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'mkdocs' in meta.get('content', '').lower():
        return FrameworkInfo('mkdocs', meta.get('content'), confidence=0.9)

    if soup.find(class_=['md-content', 'md-sidebar', 'md-nav', 'wy-nav-content']):
        return FrameworkInfo('mkdocs', confidence=0.9)
    return None

def detect_gitbook(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    meta = soup.find('meta', attrs={'name': 'generator'})
    if meta and 'gitbook' in meta.get('content', '').lower():
        return FrameworkInfo('gitbook', confidence=0.85)

    if soup.find(class_=['book-summary', 'page-inner', 'gitbook-root']):
        return FrameworkInfo('gitbook', confidence=0.85)

    if soup.find('link', href=lambda x: x and 'gitbook' in x.lower()):
        return FrameworkInfo('gitbook', confidence=0.7)
    return None

def detect_docsify(soup: BeautifulSoup) -> Optional[FrameworkInfo]:
    for script in soup.find_all('script'):
        src = script.get('src', '').lower()
        text = script.text
        if 'docsify' in src or '$docsify' in text:
            return FrameworkInfo('docsify', confidence=0.9)

    if soup.find(class_='sidebar-toggle'):
        body = soup.find('body')
        if body:
            body_class = body.get('class', [])
            if isinstance(body_class, list) and 'ready' in body_class:
                return FrameworkInfo('docsify', confidence=0.8)
            elif isinstance(body_class, str) and 'ready' in body_class.split():
                return FrameworkInfo('docsify', confidence=0.8)
    return None

def detect_framework_opt(html: str) -> FrameworkInfo:
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

html_docusaurus = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Page</title>
</head>
<body>
    <div>Nothing here</div>
    <script src="/js/docusaurus.js"></script>
""" + "<div>Random content</div>" * 1000 + """
</body>
</html>
"""

html_unknown = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Page</title>
</head>
<body>
    <div>Nothing here</div>
""" + "<script>console.log('test');</script><div>Random content</div>" * 1000 + """
</body>
</html>
"""

print("Testing orig Docusaurus...")
start = time.time()
for _ in range(50):
    detect_framework_orig(html_docusaurus)
end = time.time()
print(f"Orig Docusaurus Time taken: {end - start:.4f} seconds")

print("Testing opt Docusaurus...")
start = time.time()
for _ in range(50):
    detect_framework_opt(html_docusaurus)
end = time.time()
print(f"Opt Docusaurus Time taken: {end - start:.4f} seconds")

print("Testing orig Unknown (worst case)...")
start = time.time()
for _ in range(50):
    detect_framework_orig(html_unknown)
end = time.time()
print(f"Orig Unknown Time taken: {end - start:.4f} seconds")

print("Testing opt Unknown (worst case)...")
start = time.time()
for _ in range(50):
    detect_framework_opt(html_unknown)
end = time.time()
print(f"Opt Unknown Time taken: {end - start:.4f} seconds")
