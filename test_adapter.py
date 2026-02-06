"""测试main.py的导入和crawl_docs函数"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from main import crawl_docs

# 测试爬取FastAPI文档（只爬取前5个页面作为测试）
print("=== Testing crawl_docs with FastAPI ===")
result = crawl_docs(
    start_url="https://fastapi.tiangolo.com/tutorial/",
    output_format="single",
    download_images=False,  # 测试时不下载图片
    output_dir=Path("./test_output"),
)

print(f"\nResult: {result['success']}")
print(f"Pages crawled: {result.get('pages_crawled', 0)}")
