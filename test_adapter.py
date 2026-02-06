"""测试P0内容清理效果"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from src.fetcher import fetch_with_requests
from src.extractor import extract_content

# 测试SonarQube
print("=== Testing SonarQube ===")
result = fetch_with_requests("https://docs.sonarsource.com/sonarqube-server/try-out-sonarqube")
content = extract_content(result.html, result.url)
print(f"Title: {content.title}")
print(f"Markdown preview (first 500 chars):")
print(content.markdown[:500])
print("\n" + "="*50)

# 测试Docker
print("\n=== Testing Docker ===")
result2 = fetch_with_requests("https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/")
content2 = extract_content(result2.html, result2.url)
print(f"Title: {content2.title}")
print(f"Markdown preview (first 500 chars):")
print(content2.markdown[:500])
