import sys
from pathlib import Path

# 将项目根目录添加到 Python 路径，确保能找到 src 模块
root_dir = str(Path(__file__).parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

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
