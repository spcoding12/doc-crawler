"""
图片下载模块

下载页面中的图片到本地，并更新Markdown中的图片路径
"""

import requests
import re
import hashlib
from pathlib import Path
from urllib.parse import urlparse, urljoin
from typing import Optional
import mimetypes


# 请求超时
DOWNLOAD_TIMEOUT = 30

# 支持的图片格式
SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico', '.bmp'}

# 请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}


class ImageDownloadResult:
    """图片下载结果"""
    def __init__(
        self,
        original_url: str,
        local_path: Optional[Path] = None,
        success: bool = True,
        error: Optional[str] = None,
    ):
        self.original_url = original_url
        self.local_path = local_path
        self.success = success
        self.error = error
    
    def __repr__(self):
        if self.success:
            return f"ImageDownloadResult('{self.local_path}')"
        return f"ImageDownloadResult(failed: {self.error})"


def get_image_extension(url: str, content_type: Optional[str] = None) -> str:
    """
    获取图片扩展名
    
    Args:
        url: 图片URL
        content_type: HTTP Content-Type
    
    Returns:
        str: 扩展名（如 .png）
    """
    # 从URL获取
    parsed = urlparse(url)
    path = parsed.path
    if '.' in path:
        ext = '.' + path.rsplit('.', 1)[-1].lower()
        if ext in SUPPORTED_EXTENSIONS:
            return ext
    
    # 从Content-Type获取
    if content_type:
        ext = mimetypes.guess_extension(content_type.split(';')[0].strip())
        if ext:
            return ext
    
    # 默认png
    return '.png'


def generate_image_filename(url: str, index: int = 0) -> str:
    """
    生成图片文件名
    
    Args:
        url: 图片URL
        index: 序号
    
    Returns:
        str: 文件名
    """
    # 使用URL的hash作为唯一标识
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"img_{index:03d}_{url_hash}"


def download_image(
    url: str,
    output_dir: Path,
    index: int = 0,
    timeout: int = DOWNLOAD_TIMEOUT,
) -> ImageDownloadResult:
    """
    下载单张图片
    
    Args:
        url: 图片URL
        output_dir: 输出目录
        index: 序号
        timeout: 超时时间
    
    Returns:
        ImageDownloadResult: 下载结果
    """
    try:
        # 确保目录存在
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # 下载图片
        response = requests.get(url, headers=HEADERS, timeout=timeout, stream=True)
        response.raise_for_status()
        
        # 获取扩展名和文件名
        content_type = response.headers.get('Content-Type', '')
        ext = get_image_extension(url, content_type)
        filename = generate_image_filename(url, index) + ext
        
        # 保存文件
        filepath = output_dir / filename
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return ImageDownloadResult(
            original_url=url,
            local_path=filepath,
            success=True,
        )
    
    except requests.Timeout:
        return ImageDownloadResult(url, error="下载超时", success=False)
    except requests.HTTPError as e:
        return ImageDownloadResult(url, error=f"HTTP错误: {e.response.status_code}", success=False)
    except Exception as e:
        return ImageDownloadResult(url, error=str(e), success=False)


def download_images(
    image_urls: list[str],
    output_dir: Path,
) -> list[ImageDownloadResult]:
    """
    批量下载图片
    
    Args:
        image_urls: 图片URL列表
        output_dir: 输出目录
    
    Returns:
        list[ImageDownloadResult]: 下载结果列表
    """
    results = []
    for i, url in enumerate(image_urls):
        result = download_image(url, output_dir, index=i)
        results.append(result)
    return results


def replace_image_urls_in_markdown(
    markdown: str,
    download_results: list[ImageDownloadResult],
    relative_image_dir: str = "images",
) -> str:
    """
    替换Markdown中的图片URL为本地路径
    
    Args:
        markdown: 原始Markdown
        download_results: 下载结果列表
        relative_image_dir: 相对图片目录
    
    Returns:
        str: 替换后的Markdown
    """
    for result in download_results:
        if result.success and result.local_path:
            # 构建相对路径
            local_path = f"{relative_image_dir}/{result.local_path.name}"
            # 替换URL
            markdown = markdown.replace(result.original_url, local_path)
    
    return markdown


def process_images(
    markdown: str,
    image_urls: list[str],
    output_dir: Path,
    download: bool = True,
) -> tuple[str, list[ImageDownloadResult]]:
    """
    处理Markdown中的图片
    
    Args:
        markdown: 原始Markdown
        image_urls: 图片URL列表
        output_dir: 输出目录
        download: 是否下载图片
    
    Returns:
        tuple: (更新后的Markdown, 下载结果列表)
    """
    if not download or not image_urls:
        return markdown, []
    
    # 创建图片目录
    images_dir = output_dir / "images"
    
    # 下载图片
    results = download_images(image_urls, images_dir)
    
    # 替换URL
    updated_markdown = replace_image_urls_in_markdown(markdown, results)
    
    return updated_markdown, results
