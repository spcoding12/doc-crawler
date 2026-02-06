"""通用工具函数"""

from urllib.parse import urljoin, urlparse
from pathlib import Path
import re


def normalize_url(url: str) -> str:
    """标准化URL，去除末尾斜杠"""
    return url.rstrip("/")


def get_domain(url: str) -> str:
    """获取URL的域名"""
    parsed = urlparse(url)
    return parsed.netloc


def get_path_prefix(url: str) -> str:
    """获取URL的路径前缀"""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    # 获取路径的目录部分
    if path:
        parts = path.rsplit("/", 1)
        return parts[0] if len(parts) > 1 else path
    return ""


def make_absolute_url(base_url: str, relative_url: str) -> str:
    """将相对URL转为绝对URL"""
    return urljoin(base_url, relative_url)


def sanitize_filename(name: str) -> str:
    """清理文件名，移除非法字符"""
    # 替换非法字符
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    # 移除首尾空格和点
    name = name.strip(" .")
    return name or "unnamed"


def ensure_dir(path: Path) -> Path:
    """确保目录存在"""
    path.mkdir(parents=True, exist_ok=True)
    return path
