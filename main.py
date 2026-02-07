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
    GenericAdapter,
)


# 框架适配器映射
ADAPTERS = {
    'docusaurus': DocusaurusAdapter,
    'vuepress': VuePressAdapter,
    'mkdocs': MkDocsAdapter,
    'gitbook': GitBookAdapter,
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
    print(f"\n🔍 正在分析: {start_url}")
    
    # 1. 获取起始页面
    try:
        result = fetch_with_requests(start_url)
    except FetchError as e:
        return {"success": False, "error": str(e)}
    
    # 2. 检测框架
    framework = detect_framework(result.html)
    print(f"📦 检测到框架: {framework.name} (置信度: {framework.confidence})")
    
    # 根据URL路径生成唯一的站点目录名，避免同一域名下不同文档相互覆盖
    parsed_url = urlparse(start_url)
    site_name = parsed_url.netloc + parsed_url.path.rstrip('/')
    
    # 3. 获取适配器并解析侧边栏链接
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(result.html, 'lxml')
    
    adapter_class = ADAPTERS.get(framework.name, GenericAdapter)
    adapter = adapter_class()
    links = adapter.get_sidebar_links(soup, start_url)
    
    # 如果检测到的适配器找不到足够链接，回退到GenericAdapter
    if len(links) < 5 and adapter_class != GenericAdapter:
        print(f"  ⚠️ {framework.name}适配器只找到{len(links)}个链接，尝试通用适配器...")
        adapter = GenericAdapter()
        links = adapter.get_sidebar_links(soup, start_url)
    
    if not links:
        # 如果仍没有找到链接，至少包含当前页面
        links = [{"url": start_url, "title": "Index", "level": 0}]
    
    print(f"📄 发现 {len(links)} 个页面")
    
    # 5. 爬取所有页面
    pages = []
    failed_pages = []
    
    for i, link in enumerate(links, 1):
        url = link['url']
        title = link['title']
        
        print(f"  [{i}/{len(links)}] {title[:40]}...", end=" ", flush=True)
        
        try:
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
        
        # 避免请求过快
        time.sleep(0.5)
    
    print(f"\n✅ 成功爬取 {len(pages)} 个页面")
    if failed_pages:
        print(f"❌ 失败 {len(failed_pages)} 个页面")
    
    # 6. 导出
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
