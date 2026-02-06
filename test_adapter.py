"""测试输出生成模块"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from src.exporter import PageContent, export_content

# 创建测试数据
pages = [
    PageContent(url="https://example.com/intro", title="Introduction", markdown="# Intro\nWelcome!", images=[], level=0, order=1),
    PageContent(url="https://example.com/getting-started", title="Getting Started", markdown="# Getting Started\nStep 1...", images=[], level=0, order=2),
    PageContent(url="https://example.com/api", title="API Reference", markdown="# API\n## Methods...", images=[], level=1, order=3),
]

output_dir = Path("./test_output")

# 测试单文件输出
print("=== Testing Single Markdown ===")
result = export_content(pages, output_dir, format="single", site_name="test-docs")
print(f"Output: {result['files']}")

# 测试多文件输出
print("\n=== Testing Multiple Markdown ===")
result2 = export_content(pages, output_dir, format="multiple", site_name="test-docs-multi")
print(f"Files created: {len(result2['files'])}")
for f in result2['files']:
    print(f"  {Path(f).name}")

# 测试JSON输出
print("\n=== Testing JSON ===")
result3 = export_content(pages, output_dir, format="json", site_name="test-docs-json")
print(f"Output: {result3['files']}")
