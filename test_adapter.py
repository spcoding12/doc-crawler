"""测试图片下载模块"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from pathlib import Path
from src.images import download_image, download_images, replace_image_urls_in_markdown

# 测试单张图片下载
print("=== Testing single image download ===")
test_url = "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
output_dir = Path("./test_output/images")

result = download_image(test_url, output_dir, index=0)
print(f"Success: {result.success}")
print(f"Local path: {result.local_path}")
if result.error:
    print(f"Error: {result.error}")

# 测试Markdown替换
print("\n=== Testing Markdown URL replacement ===")
markdown = "![logo](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)"
updated = replace_image_urls_in_markdown(markdown, [result])
print(f"Original: {markdown}")
print(f"Updated: {updated}")
