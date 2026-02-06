"""测试Docusaurus适配器"""
from src.fetcher import fetch_with_requests
from src.frameworks import DocusaurusAdapter, GenericAdapter
from bs4 import BeautifulSoup

# 测试React.dev
print("=== Testing React.dev ===")
html = fetch_with_requests('https://react.dev/learn').html
soup = BeautifulSoup(html, 'lxml')

adapter = DocusaurusAdapter()
print(f"Docusaurus detect: {adapter.detect(soup)}")

links = adapter.get_sidebar_links(soup, 'https://react.dev/learn')
print(f"Links found: {len(links)}")
for l in links[:5]:
    print(f"  {l['title'][:40]}: {l['url']}")

# 测试通用适配器
print("\n=== Testing GenericAdapter on Docker ===")
html2 = fetch_with_requests('https://docs.docker.com/get-started/').html
soup2 = BeautifulSoup(html2, 'lxml')

generic = GenericAdapter()
links2 = generic.get_sidebar_links(soup2, 'https://docs.docker.com/get-started/')
print(f"Links found: {len(links2)}")
for l in links2[:5]:
    print(f"  {l['title'][:40]}: {l['url']}")
