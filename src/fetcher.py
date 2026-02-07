"""
页面获取模块

提供两种获取方式：
1. requests（轻量，默认）
2. Playwright（JS渲染页面，可选）
"""

import requests
from typing import Optional
import re


# 请求头，模拟浏览器
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# 请求超时
DEFAULT_TIMEOUT = 30


class FetchError(Exception):
    """获取页面失败"""
    pass


class FetchResult:
    """获取结果"""
    def __init__(self, html: str, url: str, status_code: int = 200):
        self.html = html
        self.url = url
        self.status_code = status_code
        self.is_js_rendered = False  # 标记是否通过JS渲染获取


def fetch_with_requests(url: str, timeout: int = DEFAULT_TIMEOUT, session: Optional[requests.Session] = None) -> FetchResult:
    """
    使用 requests 获取页面
    
    Args:
        url: 要获取的URL
        timeout: 超时时间（秒）
        session: 可选的 requests.Session 实例
    
    Returns:
        FetchResult: 获取结果
    
    Raises:
        FetchError: 获取失败时抛出
    """
    try:
        fetcher = session if session else requests
        response = fetcher.get(
            url, 
            headers=DEFAULT_HEADERS, 
            timeout=timeout,
            allow_redirects=True
        )
        response.raise_for_status()
        
        # 尝试检测编码
        response.encoding = response.apparent_encoding or 'utf-8'
        
        return FetchResult(
            html=response.text,
            url=response.url,  # 可能有重定向
            status_code=response.status_code
        )
    except requests.Timeout:
        raise FetchError(f"请求超时: {url}")
    except requests.HTTPError as e:
        raise FetchError(f"HTTP错误 {e.response.status_code}: {url}")
    except requests.RequestException as e:
        raise FetchError(f"请求失败: {url} - {str(e)}")


def is_js_rendered_page(html: str) -> bool:
    """
    检测页面是否需要JavaScript渲染
    
    通过检查HTML特征来判断：
    1. body内容很少（可能是SPA占位）
    2. 包含React/Vue等框架的挂载点
    3. 大量script标签但正文内容少
    
    Args:
        html: HTML内容
    
    Returns:
        bool: True表示可能需要JS渲染
    """
    # 检查是否有足够的文本内容
    # 移除script和style标签后检查
    text_content = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text_content = re.sub(r'<style[^>]*>.*?</style>', '', text_content, flags=re.DOTALL | re.IGNORECASE)
    text_content = re.sub(r'<[^>]+>', '', text_content)
    text_content = text_content.strip()
    
    # 如果去除标签后文本太少，可能是SPA
    if len(text_content) < 500:
        # 检查是否有React/Vue等框架特征
        spa_indicators = [
            'id="root"',
            'id="app"',
            'id="__next"',
            'id="__nuxt"',
            'data-reactroot',
            'ng-app',
            '__NEXT_DATA__',
            '__NUXT__',
        ]
        for indicator in spa_indicators:
            if indicator in html:
                return True
    
    return False


def fetch_with_playwright(url: str, timeout: int = DEFAULT_TIMEOUT * 1000) -> FetchResult:
    """
    使用 Playwright 获取页面（支持JS渲染）
    
    Args:
        url: 要获取的URL
        timeout: 超时时间（毫秒）
    
    Returns:
        FetchResult: 获取结果
    
    Raises:
        FetchError: 获取失败或Playwright未安装时抛出
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise FetchError(
            "需要安装 Playwright 来获取此页面。\n"
            "请运行: pip install playwright && playwright install chromium"
        )
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_default_timeout(timeout)
            
            response = page.goto(url, wait_until="networkidle")
            
            if response is None:
                raise FetchError(f"无法获取页面: {url}")
            
            html = page.content()
            final_url = page.url
            status = response.status
            
            browser.close()
            
            result = FetchResult(html=html, url=final_url, status_code=status)
            result.is_js_rendered = True
            return result
            
    except Exception as e:
        if "playwright" in str(e).lower():
            raise FetchError(
                "Playwright 浏览器未安装。\n"
                "请运行: playwright install chromium"
            )
        raise FetchError(f"Playwright获取失败: {url} - {str(e)}")


def check_playwright_available() -> bool:
    """检查 Playwright 是否可用"""
    try:
        from playwright.sync_api import sync_playwright
        return True
    except ImportError:
        return False


def fetch_page(url: str, force_js: bool = False) -> FetchResult:
    """
    智能获取页面
    
    1. 首先尝试 requests
    2. 如果检测到需要JS渲染，提示用户使用 Playwright
    
    Args:
        url: 要获取的URL
        force_js: 强制使用Playwright
    
    Returns:
        FetchResult: 获取结果
    """
    if force_js:
        return fetch_with_playwright(url)
    
    # 先用 requests 尝试
    result = fetch_with_requests(url)
    
    # 检查是否需要JS渲染
    if is_js_rendered_page(result.html):
        result.is_js_rendered = True  # 标记需要JS渲染
    
    return result
