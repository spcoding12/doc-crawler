"""测试内容提取模块"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from src.fetcher import fetch_with_requests
from src.extractor import extract_content

# 测试 FastAPI (MkDocs)
print("=== Testing FastAPI ===")
result = fetch_with_requests('https://fastapi.tiangolo.com/tutorial/')
content = extract_content(result.html, result.url)
print(f"Title: {content.title}")
print(f"Images: {len(content.images)}")
print(f"Markdown length: {len(content.markdown)}")
print(f"First 200 chars:\n{content.markdown[:200]}")

# 测试 Vue.js (VuePress)
print("\n=== Testing Vue.js ===")
result2 = fetch_with_requests('https://vuejs.org/guide/introduction.html')
content2 = extract_content(result2.html, result2.url)
print(f"Title: {content2.title}")
print(f"Images: {len(content2.images)}")
print(f"Markdown length: {len(content2.markdown)}")
