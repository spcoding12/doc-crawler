import pytest
from bs4 import BeautifulSoup
from src.detector import detect_framework

def test_detect_docusaurus():
    html = '<html><head><meta name="generator" content="Docusaurus v3"></head><body><div class="theme-doc-sidebar-container"></div></body></html>'
    info = detect_framework(html)
    assert info.name == 'docusaurus'
    assert info.version == 'Docusaurus v3'

def test_detect_vuepress():
    html = '<html><body><div class="theme-default-content"></div></body></html>'
    info = detect_framework(html)
    assert info.name == 'vuepress'

def test_detect_mkdocs():
    html = '<html><head><meta name="generator" content="mkdocs-1.5.0"></head><body><div class="md-content"></div></body></html>'
    info = detect_framework(html)
    assert info.name == 'mkdocs'
    assert info.version == 'mkdocs-1.5.0'

def test_detect_gitbook():
    html = '<html><body><div class="book-summary"></div></body></html>'
    info = detect_framework(html)
    assert info.name == 'gitbook'

def test_detect_docsify():
    html = '<html><head></head><body class="ready"><div class="sidebar-toggle"></div><script src="docsify.js"></script></body></html>'
    info = detect_framework(html)
    assert info.name == 'docsify'

def test_detect_unknown():
    html = '<html><body><div>Just some content</div></body></html>'
    info = detect_framework(html)
    assert info.name == 'unknown'
