"""
输出生成模块

支持三种输出格式：
1. 单个Markdown文件 (all.md)
2. 多个Markdown文件（按目录结构带序号）
3. JSON文件
"""

import json
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict
import re


@dataclass
class PageContent:
    """页面内容"""
    url: str
    title: str
    markdown: str
    images: list[str]
    level: int = 0  # 目录层级
    order: int = 0  # 排序序号


def sanitize_filename(name: str) -> str:
    """清理文件名，移除非法字符"""
    # 替换非法字符
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    # 移除首尾空格和点
    name = name.strip(' .')
    # 限制长度
    if len(name) > 50:
        name = name[:50]
    return name or 'unnamed'


def generate_index_md(pages: list[PageContent], title: str = "目录") -> str:
    """
    生成目录索引 index.md
    
    Args:
        pages: 页面列表
        title: 标题
    
    Returns:
        str: Markdown内容
    """
    lines = [f"# {title}\n"]
    
    for page in pages:
        indent = "  " * page.level
        link = sanitize_filename(page.title) + ".md"
        lines.append(f"{indent}- [{page.title}]({link})")
    
    return '\n'.join(lines)


def export_single_markdown(
    pages: list[PageContent],
    output_dir: Path,
    filename: str = "all.md",
) -> Path:
    """
    导出为单个Markdown文件
    
    Args:
        pages: 页面列表
        output_dir: 输出目录
        filename: 文件名
    
    Returns:
        Path: 输出文件路径
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    lines = []
    for page in pages:
        # 添加标题
        heading_level = min(page.level + 1, 6)
        lines.append(f"{'#' * heading_level} {page.title}\n")
        lines.append(page.markdown)
        lines.append("\n---\n")
    
    content = '\n'.join(lines)
    
    filepath = output_dir / filename
    filepath.write_text(content, encoding='utf-8')
    
    return filepath


def export_multiple_markdown(
    pages: list[PageContent],
    output_dir: Path,
) -> list[Path]:
    """
    导出为多个Markdown文件（带序号目录结构）
    
    Args:
        pages: 页面列表
        output_dir: 输出目录
    
    Returns:
        list[Path]: 输出文件路径列表
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    created_files = []
    
    for i, page in enumerate(pages):
        # 生成带序号的文件名
        order = f"{i+1:02d}"
        safe_title = sanitize_filename(page.title)
        filename = f"{order}_{safe_title}.md"
        
        # 添加标题到内容
        content = f"# {page.title}\n\n{page.markdown}"
        
        filepath = output_dir / filename
        filepath.write_text(content, encoding='utf-8')
        created_files.append(filepath)
    
    # 生成目录索引
    index_content = generate_index_md(pages)
    index_path = output_dir / "index.md"
    index_path.write_text(index_content, encoding='utf-8')
    created_files.insert(0, index_path)
    
    return created_files


def export_json(
    pages: list[PageContent],
    output_dir: Path,
    filename: str = "pages.json",
) -> Path:
    """
    导出为JSON文件
    
    Args:
        pages: 页面列表
        output_dir: 输出目录
        filename: 文件名
    
    Returns:
        Path: 输出文件路径
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    data = {
        "total_pages": len(pages),
        "pages": [asdict(page) for page in pages],
    }
    
    filepath = output_dir / filename
    filepath.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    
    return filepath


def export_content(
    pages: list[PageContent],
    output_dir: Path,
    format: str = "single",  # single, multiple, json
    site_name: str = "docs",
) -> dict:
    """
    统一导出接口
    
    Args:
        pages: 页面列表
        output_dir: 输出目录
        format: 输出格式 (single/multiple/json)
        site_name: 站点名称（用于子目录）
    
    Returns:
        dict: 导出结果 {format, files, output_dir}
    """
    # 创建站点子目录
    site_dir = output_dir / sanitize_filename(site_name)
    
    result = {
        "format": format,
        "output_dir": str(site_dir),
        "files": [],
    }
    
    if format == "single":
        filename = f"{sanitize_filename(site_name)}_all.md"
        filepath = export_single_markdown(pages, site_dir, filename=filename)
        result["files"] = [str(filepath)]
    
    elif format == "multiple":
        filepaths = export_multiple_markdown(pages, site_dir)
        result["files"] = [str(f) for f in filepaths]
    
    elif format == "json":
        filepath = export_json(pages, site_dir)
        result["files"] = [str(filepath)]
    
    else:
        raise ValueError(f"不支持的输出格式: {format}")
    
    return result
