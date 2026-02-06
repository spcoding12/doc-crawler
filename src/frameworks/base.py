"""框架适配器基类"""

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


class FrameworkAdapter(ABC):
    """文档框架适配器基类"""
    
    name: str = "unknown"
    
    @classmethod
    @abstractmethod
    def detect(cls, soup: BeautifulSoup) -> bool:
        """检测页面是否使用此框架"""
        pass
    
    @abstractmethod
    def get_sidebar_links(self, soup: BeautifulSoup, base_url: str) -> list[dict]:
        """
        提取侧边栏导航链接
        
        Returns:
            list[dict]: [{url, title, level}, ...]
        """
        pass
    
    @abstractmethod
    def get_content_selector(self) -> str:
        """返回正文内容的CSS选择器"""
        pass
    
    def extract_title(self, soup: BeautifulSoup) -> str:
        """提取页面标题"""
        # 默认实现：尝试h1或title
        h1 = soup.find("h1")
        if h1:
            return h1.get_text(strip=True)
        title = soup.find("title")
        if title:
            return title.get_text(strip=True)
        return "Untitled"
