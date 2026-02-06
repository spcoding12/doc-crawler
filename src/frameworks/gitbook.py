"""GitBook 框架适配器 - 占位文件，Task 5 实现"""

from .base import FrameworkAdapter


class GitBookAdapter(FrameworkAdapter):
    name = "gitbook"
    
    @classmethod
    def detect(cls, soup):
        # TODO: Task 5 实现
        return False
    
    def get_sidebar_links(self, soup, base_url):
        # TODO: Task 5 实现
        return []
    
    def get_content_selector(self):
        return ".page-inner .normal"
