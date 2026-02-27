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
from collections import OrderedDict
from dataclasses import dataclass, asdict
from urllib.parse import urlparse
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


def _get_directory_key(url: str) -> str:
    """
    从 URL 中提取第一级目录作为分组键。
    例如: https://docs.example.com/guide/getting-started -> 'guide'
         https://docs.example.com/api/v2/users -> 'api'
    """
    path = urlparse(url).path.strip('/')
    parts = path.split('/')
    # 取第一级目录；如果只有一级（即根页面），用 '_root' 作为键
    return parts[0] if parts and parts[0] else '_root'


def _group_pages_by_directory(pages: list[PageContent]) -> OrderedDict:
    """
    按 URL 第一级目录对页面进行分组，保持原始顺序。
    
    Returns:
        OrderedDict: {directory_key: [PageContent, ...]}
    """
    groups = OrderedDict()
    for page in pages:
        key = _get_directory_key(page.url)
        if key not in groups:
            groups[key] = []
        groups[key].append(page)
    return groups


def _render_pages_to_markdown(pages: list[PageContent]) -> str:
    """将页面列表渲染为 Markdown 文本"""
    lines = []
    for page in pages:
        heading_level = min(page.level + 1, 6)
        lines.append(f"{'#' * heading_level} {page.title}\n")
        lines.append(page.markdown)
        lines.append("\n---\n")
    return '\n'.join(lines)


def _generate_part_header(part_index: int, total_parts: int, group_keys: list[str]) -> str:
    """
    为每个分片生成头部信息（包含分片编号和该分片包含的章节目录）。
    """
    lines = [
        f"> 📖 本文件为第 {part_index} / {total_parts} 部分\n",
        "**本文件包含以下章节：**\n",
    ]
    for key in group_keys:
        lines.append(f"- {key}")
    lines.append("\n---\n")
    return '\n'.join(lines)


def _split_groups_into_parts(
    groups: OrderedDict,
    max_chars: int,
) -> list[list[tuple[str, list[PageContent]]]]:
    """
    根据字符数阈值，将分组拆分为多个分片。
    
    策略：
    - 依次将分组加入当前分片
    - 如果加入后超出阈值，则开启新分片
    - 如果单个分组本身就超出阈值，仍作为独立分片（不强行拆散同一目录）
    
    Args:
        groups: 按目录分组的 OrderedDict
        max_chars: 每个分片的最大字符数
    
    Returns:
        list of parts, 每个 part 是 [(group_key, [pages]), ...]
    """
    parts = []
    current_part = []
    current_chars = 0
    
    for key, pages in groups.items():
        group_text = _render_pages_to_markdown(pages)
        group_chars = len(group_text)
        
        # 如果当前分片为空，直接加入（即使超出阈值也不能把一个组拆散）
        if not current_part:
            current_part.append((key, pages))
            current_chars = group_chars
            continue
        
        # 如果加入后超出阈值，先保存当前分片，开启新分片
        if current_chars + group_chars > max_chars:
            parts.append(current_part)
            current_part = [(key, pages)]
            current_chars = group_chars
        else:
            current_part.append((key, pages))
            current_chars += group_chars
    
    # 别忘了最后一个分片
    if current_part:
        parts.append(current_part)
    
    return parts


def export_single_markdown(
    pages: list[PageContent],
    output_dir: Path,
    filename: str = "all.md",
    max_chars: int = 400_000,
) -> list[Path]:
    """
    导出为单个或多个Markdown文件（自动根据字符数拆分）。
    
    当总字符数未超过 max_chars 时，输出单个文件（行为不变）。
    当总字符数超出 max_chars 时，按目录分组拆分为多个 part 文件。
    
    Args:
        pages: 页面列表
        output_dir: 输出目录
        filename: 基础文件名
        max_chars: 单个文件最大字符数，默认 400,000
    
    Returns:
        list[Path]: 输出文件路径列表
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 先渲染完整内容，判断是否需要拆分
    full_content = _render_pages_to_markdown(pages)
    
    if len(full_content) <= max_chars:
        # 不需要拆分，保持原有行为
        filepath = output_dir / filename
        filepath.write_text(full_content, encoding='utf-8')
        return [filepath]
    
    # --- 需要拆分 ---
    print(f"\n⚠️  合并文档共 {len(full_content):,} 字符，超出单文件阈值 ({max_chars:,})，将自动拆分...")
    
    groups = _group_pages_by_directory(pages)
    parts = _split_groups_into_parts(groups, max_chars)
    
    total_parts = len(parts)
    print(f"📦 按目录结构拆分为 {total_parts} 个文件")
    
    # 生成文件名：将 xxx_all.md -> xxx_all_part1.md, xxx_all_part2.md, ...
    stem = Path(filename).stem   # e.g. "site_all"
    suffix = Path(filename).suffix  # e.g. ".md"
    
    created_files = []
    for i, part in enumerate(parts, 1):
        part_filename = f"{stem}_part{i}{suffix}"
        group_keys = [key for key, _ in part]
        all_pages = []
        for _, pages_in_group in part:
            all_pages.extend(pages_in_group)
        
        # 组装内容：头部 + 正文
        header = _generate_part_header(i, total_parts, group_keys)
        body = _render_pages_to_markdown(all_pages)
        content = header + body
        
        filepath = output_dir / part_filename
        filepath.write_text(content, encoding='utf-8')
        created_files.append(filepath)
        print(f"  📝 {part_filename} ({len(content):,} 字符, {len(all_pages)} 页)")
    
    return created_files


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
        filepaths = export_single_markdown(pages, site_dir, filename=filename)
        result["files"] = [str(f) for f in filepaths]
    
    elif format == "multiple":
        filepaths = export_multiple_markdown(pages, site_dir)
        result["files"] = [str(f) for f in filepaths]
    
    elif format == "json":
        filepath = export_json(pages, site_dir)
        result["files"] = [str(filepath)]
    
    else:
        raise ValueError(f"不支持的输出格式: {format}")
    
    return result
