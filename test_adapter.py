"""验证改进后的GenericAdapter"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from src.fetcher import fetch_with_requests
from src.frameworks import GenericAdapter
from bs4 import BeautifulSoup

url = "https://docs.sonarsource.com/sonarqube-server/"
print(f"Testing improved GenericAdapter on: {url}")

result = fetch_with_requests(url)
soup = BeautifulSoup(result.html, 'lxml')

adapter = GenericAdapter()
links = adapter.get_sidebar_links(soup, url)

print(f"\nFound {len(links)} links:")
for i, l in enumerate(links[:20], 1):
    print(f"  {i}. {l['title'][:40]}: {l['url']}")
