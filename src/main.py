"""
Doc Crawler - 通用技术文档爬取工具

交互式命令行入口
"""

import sys
import time
from pathlib import Path
from urllib.parse import urlparse

# 确保UTF-8输出
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from src.fetcher import fetch_with_requests, FetchError
from src.detector import detect_framework
from src.extractor import extract_content
from src.exporter import PageContent, export_content
from src.images import process_images
from src.frameworks import (
    DocusaurusAdapter,
    VuePressAdapter,
    MkDocsAdapter,
    GitBookAdapter,
    DocsifyAdapter,
    GenericAdapter,
)


# 框架适配器映射
ADAPTERS = {
    'docusaurus': DocusaurusAdapter,
    'vuepress': VuePressAdapter,
    'mkdocs': MkDocsAdapter,
    'gitbook': GitBookAdapter,
    'docsify': DocsifyAdapter,
    'generic': GenericAdapter,
    'unknown': GenericAdapter,
}


def print_banner():
    """打印欢迎信息"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║                     Doc Crawler v1.0                           ║
║              通用技术文档爬取工具                                 ║
╚════════════════════════════════════════════════════════════════╝
""")


def get_user_input(prompt: str, default: str = "") -> str:
    """获取用户输入"""
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    return input(f"{prompt}: ").strip()


def get_choice(prompt: str, options: list[str], default: int = 1) -> int:
    """获取用户选择"""
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    
    while True:
        choice = input(f"请选择 [{default}]: ").strip()
        if not choice:
            return default
        try:
            num = int(choice)
            if 1 <= num <= len(options):
                return num
        except ValueError:
            pass
        print("  无效选择，请重新输入")


def crawl_docs(
    start_url: str,
    output_format: str = "single",
    download_images: bool = True,
    output_dir: Path = Path("./output"),
    max_pages: int = None,
    skip_export: bool = False,
) -> dict:
    """
    爬取文档的主函数
    
    Args:
        start_url: 起始URL
        output_format: 输出格式 (single/multiple/json)
        download_images: 是否下载图片
        output_dir: 输出目录
    
    Returns:
        dict: 爬取结果
    """
    # --- Docsify / Hash URL 预处理 ---
    # 如果 URL 包含 # （Hash 路由），去掉 # 及其后面的部分
    # 例如: https://example.com/docs#/openapi -> https://example.com/docs
    has_hash = '#' in start_url
    if has_hash:
        start_url = start_url.split('#', 1)[0]
        print(f"  🔗 检测到 Hash 路由，实际请求: {start_url}")

    # 归一化初始 URL
    # 如果路径不以 / 结尾且不包含 . (即不是文件)，则补齐 / 以便 adapter 正确处理相对路径
    if not start_url.endswith('/'):
        p = urlparse(start_url)
        if not p.path or (not p.path.endswith('/') and '.' not in p.path.split('/')[-1]):
            start_url += '/'
    
    print(f"\n🔍 正在分析站点: {start_url}")

    # 根据URL路径生成唯一的站点目录名，避免同一域名下不同文档相互覆盖
    parsed_url = urlparse(start_url)
    site_name = parsed_url.netloc + parsed_url.path.rstrip('/')

    # --- Docsify 快速路径 ---
    # 对于 Hash URL，先尝试直接请求 _sidebar.md，如果成功则确认为 Docsify 站点
    # 这样可以完全绕过首页 404 的问题
    adapter = None
    links = []
    
    if has_hash:
        docsify_adapter = DocsifyAdapter()
        sidebar_url = docsify_adapter._build_sidebar_url(start_url)
        try:
            sidebar_result = fetch_with_requests(sidebar_url, timeout=10)
            # _sidebar.md 请求成功，确认是 Docsify 站点
            print(f"📦 检测到框架: docsify (置信度: 0.95)")
            adapter = docsify_adapter
            adapter.config['root_path'] = parsed_url.path
            if not adapter.config['root_path'].endswith('/'):
                adapter.config['root_path'] += '/'
            # 解析侧边栏获取链接
            from bs4 import BeautifulSoup
            dummy_soup = BeautifulSoup("<html></html>", "lxml")
            links = adapter.get_sidebar_links(dummy_soup, start_url)
        except FetchError:
            print("  ℹ️ _sidebar.md 不可访问，尝试常规路径...")

    # --- 常规路径（非 Docsify 或 Docsify 快速路径失败）---
    if adapter is None:
        # 1. 获取起始页面
        try:
            result = fetch_with_requests(start_url)
        except FetchError as e:
            return {"success": False, "error": str(e)}
        
        # 2. 检测框架
        framework = detect_framework(result.html)
        print(f"📦 检测到框架: {framework.name} (置信度: {framework.confidence})")
        
        # 3. 初始化爬取池
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(result.html, 'lxml')
        
        adapter_class = ADAPTERS.get(framework.name, GenericAdapter)
        adapter = adapter_class()
        # 锁定根路径，确保递归发现时不会缩减范围
        adapter.config['root_path'] = urlparse(start_url).path
        if not adapter.config['root_path'].endswith('/'):
            adapter.config['root_path'] += '/'
            
        links = adapter.get_sidebar_links(soup, start_url)
        
        # 如果检测到的适配器找不到足够链接，回退到GenericAdapter
        if len(links) < 5 and adapter_class != GenericAdapter:
            adapter = GenericAdapter()
            links = adapter.get_sidebar_links(soup, start_url)
    
    if not links:
        links = [{"url": start_url, "title": "Index", "level": 0}]

    # --- 第一阶段：并发全站扫描 (Concurrent discovery) ---
    # Docsify 站点：_sidebar.md 已给出完整链接，跳过扫描阶段
    is_docsify = isinstance(adapter, DocsifyAdapter)
    
    if is_docsify:
        to_crawl = links.copy()
        html_cache = {}
        print(f"📦 Docsify 站点，已从 _sidebar.md 获取 {len(to_crawl)} 个页面链接")
    else:
        print("🔍 正在进行高速并发扫描...")
        from concurrent.futures import ThreadPoolExecutor, as_completed
        from threading import Lock
        
        to_crawl = links.copy()
        seen_urls = {l['url'].rstrip('/') for l in links}
        html_cache = {}
        lock = Lock()
        
        # 扫描函数
        def scan_page(link_item):
            url = link_item['url']
            if url in html_cache: return []
            try:
                res = fetch_with_requests(url, timeout=10)
                with lock:
                    html_cache[url] = res
                
                soup = BeautifulSoup(res.html, 'lxml')
                return adapter.get_sidebar_links(soup, url)
            except:
                return []

        # 我们根据站点动态调整并发数，SonarSource 这类商业站点可以承受较高并发
        max_workers = 10
        
        idx = 0
        while idx < len(to_crawl):
            # 批量获取当前已知的待爬取项
            batch = to_crawl[idx : idx + max_workers]
            if not batch: break
            
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_link = {executor.submit(scan_page, link): link for link in batch}
                for future in as_completed(future_to_link):
                    new_links = future.result()
                    
                    with lock:
                        for nl in new_links:
                            norm_url = nl['url'].rstrip('/')
                            if norm_url not in seen_urls:
                                seen_urls.add(norm_url)
                                to_crawl.append(nl)
                
            idx += len(batch)
            print(f"\r  📡 已扫描 {idx} 页，发现 {len(to_crawl)} 页...", end="", flush=True)

        # 扫描后按URL路径做一次基础排序，确保内容的逻辑性
        to_crawl.sort(key=lambda x: urlparse(x['url']).path)

        print(f"\n✨ 并发扫描完成！共发现 {len(to_crawl)} 个页面。")

    print("📖 开始执行内容提取与图片处理...\n")

    # --- 第二阶段：正式爬取与内容处理 ---
    pages = []
    failed_pages = []
    
    for i, link in enumerate(to_crawl, 1):
        url = link['url']
        title = link['title']
        
        if max_pages and i > max_pages:
            print(f"  🛑 已达到最大爬取页面数 ({max_pages})")
            break
            
        print(f"  [{i}/{len(to_crawl)}] {title[:40]}...", end=" ", flush=True)
        
        try:
            # --- Docsify 特殊处理：直接请求 .md 文件 ---
            if link.get('is_docsify_md'):
                from src.extractor import clean_markdown
                md_result = fetch_with_requests(url, timeout=10)
                markdown = md_result.html  # .md 文件的内容就是纯 Markdown
                markdown = clean_markdown(markdown)
                
                # 提取图片（从 Markdown 中解析）
                import re as _re
                images = _re.findall(r'!\[.*?\]\((.*?)\)', markdown)
                
                # 处理图片
                if download_images and images:
                    images_dir = output_dir / site_name
                    markdown, img_results = process_images(
                        markdown, images, images_dir, download=True
                    )
                
                pages.append(PageContent(
                    url=url,
                    title=title,
                    markdown=markdown,
                    images=images,
                    level=link.get('level', 0),
                    order=i,
                ))
                print("✅")
            else:
                # --- 标准处理流程 ---
                page_result = html_cache.get(url)
                if not page_result:
                    page_result = fetch_with_requests(url)
                
                content = extract_content(page_result.html, url)
                
                # 处理图片
                markdown = content.markdown
                if download_images and content.images:
                    images_dir = output_dir / site_name
                    markdown, img_results = process_images(
                        markdown, content.images, images_dir, download=True
                    )
                
                pages.append(PageContent(
                    url=url,
                    title=content.title or title,
                    markdown=markdown,
                    images=content.images,
                    level=link.get('level', 0),
                    order=i,
                ))
                print("✅")
            
        except Exception as e:
            print(f"❌ {str(e)[:30]}")
            failed_pages.append({"url": url, "error": str(e)})
        
        # 频率控制
        time.sleep(0.3)
    
    print(f"\n✅ 成功爬取 {len(pages)} 个页面 (动态发现共 {len(to_crawl)} 个)")
    if failed_pages:
        print(f"❌ 失败 {len(failed_pages)} 个页面")
    
    # 6. 导出
    if skip_export:
        return {
            "success": True,
            "pages_found": len(to_crawl),
            "pages_crawled": len(pages),
            "pages": pages,
        }

    export_result = export_content(
        pages, output_dir, format=output_format, site_name=site_name
    )
    
    print(f"\n📁 输出目录: {export_result['output_dir']}")
    print(f"📝 生成文件: {len(export_result['files'])} 个")
    
    return {
        "success": True,
        "pages_crawled": len(pages),
        "pages_failed": len(failed_pages),
        "failed_pages": failed_pages,
        "output": export_result,
    }


def main():
    """主入口"""
    print_banner()
    
    # 1. 获取URL
    url = get_user_input("请输入文档起始URL")
    if not url:
        print("❌ URL不能为空")
        return
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # 2. 选择输出格式
    format_choice = get_choice(
        "选择输出格式:",
        [
            "单个Markdown文件 (all.md) - 适合导入NotebookLM",
            "多个Markdown文件 (按章节) - 适合本地阅读",
            "JSON文件 - 适合程序处理",
        ],
        default=1
    )
    format_map = {1: "single", 2: "multiple", 3: "json"}
    output_format = format_map[format_choice]
    
    # 3. 是否下载图片
    img_choice = get_choice(
        "是否下载图片到本地?",
        ["是 - 下载图片并更新链接", "否 - 保留原始URL"],
        default=1
    )
    download_images = (img_choice == 1)
    
    # 4. 输出目录
    output_dir = Path(get_user_input("输出目录", "./output"))
    
    # 5. 确认
    print("\n" + "="*50)
    print("配置确认:")
    print(f"  URL: {url}")
    print(f"  输出格式: {output_format}")
    print(f"  下载图片: {'是' if download_images else '否'}")
    print(f"  输出目录: {output_dir}")
    print("="*50)
    
    confirm = input("\n开始爬取? (Y/n): ").strip().lower()
    if confirm == 'n':
        print("已取消")
        return
    
    # 6. 执行爬取
    result = crawl_docs(
        start_url=url,
        output_format=output_format,
        download_images=download_images,
        output_dir=output_dir,
    )
    
    if result["success"]:
        print("\n" + "="*50)
        print("🎉 爬取完成!")
        print(f"   成功: {result['pages_crawled']} 页")
        if result['pages_failed'] > 0:
            print(f"   失败: {result['pages_failed']} 页")
        print("="*50)
    else:
        print(f"\n❌ 爬取失败: {result.get('error')}")


if __name__ == "__main__":
    main()
