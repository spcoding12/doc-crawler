import pytest
from bs4 import BeautifulSoup
from src.detector import detect_framework, FrameworkInfo

def test_detect_docusaurus():
    html = """
    <html data-theme="light">
    <body>
        <div class="theme-doc-sidebar-container"></div>
    </body>
    </html>
    """
    result = detect_framework(html)
    assert result.name == 'docusaurus'

def test_detect_vuepress():
    html = """
    <html>
    <body>
        <div class="theme-default-content"></div>
    </body>
    </html>
    """
    result = detect_framework(html)
    assert result.name == 'vuepress'

def test_detect_mkdocs():
    html = """
    <html>
    <body>
        <div class="md-content"></div>
    </body>
    </html>
    """
    result = detect_framework(html)
    assert result.name == 'mkdocs'

def test_detect_gitbook():
    html = """
    <html>
    <body>
        <div class="book-summary"></div>
    </body>
    </html>
    """
    result = detect_framework(html)
    assert result.name == 'gitbook'

def test_detect_docsify():
    html = """
    <html>
    <body class="ready">
        <div class="sidebar-toggle"></div>
    </body>
    </html>
    """
    result = detect_framework(html)
    assert result.name == 'docsify'

def test_detect_unknown():
    html = """
    <html>
    <body>
        <div>Just some random page</div>
    </body>
    </html>
    """
    result = detect_framework(html)
    assert result.name == 'unknown'

if __name__ == '__main__':
    pytest.main(['tests/test_detector.py'])
