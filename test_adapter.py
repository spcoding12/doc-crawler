"""测试所有适配器"""
from src.fetcher import fetch_with_requests
from src.frameworks import VuePressAdapter, MkDocsAdapter
from bs4 import BeautifulSoup

# 测试 VuePress (Vue.js)
print("=== Testing VuePress (vuejs.org) ===")
html = fetch_with_requests('https://vuejs.org/guide/introduction.html').html
soup = BeautifulSoup(html, 'lxml')
adapter = VuePressAdapter()
print(f"Detect: {adapter.detect(soup)}")
links = adapter.get_sidebar_links(soup, 'https://vuejs.org/guide/introduction.html')
print(f"Links found: {len(links)}")
for l in links[:5]:
    print(f"  {l['title'][:40]}")

# 测试 MkDocs (FastAPI)
print("\n=== Testing MkDocs (fastapi.tiangolo.com) ===")
html2 = fetch_with_requests('https://fastapi.tiangolo.com/tutorial/').html
soup2 = BeautifulSoup(html2, 'lxml')
adapter2 = MkDocsAdapter()
print(f"Detect: {adapter2.detect(soup2)}")
links2 = adapter2.get_sidebar_links(soup2, 'https://fastapi.tiangolo.com/tutorial/')
print(f"Links found: {len(links2)}")
for l in links2[:5]:
    print(f"  {l['title'][:40]}")
