"""Docusaurus 框架适配器 - 占位文件，Task 4 实现"""

from .base import FrameworkAdapter


class DocusaurusAdapter(FrameworkAdapter):
    name = "docusaurus"
    
    @classmethod
    def detect(cls, soup):
        # TODO: Task 4 实现
        return False
    
    def get_sidebar_links(self, soup, base_url):
        # TODO: Task 4 实现
        return []
    
    def get_content_selector(self):
        return "article.markdown, .markdown"
