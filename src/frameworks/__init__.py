"""框架适配器模块"""

from .base import FrameworkAdapter
from .docusaurus import DocusaurusAdapter
from .vuepress import VuePressAdapter
from .mkdocs import MkDocsAdapter
from .gitbook import GitBookAdapter
from .generic import GenericAdapter

__all__ = [
    "FrameworkAdapter",
    "DocusaurusAdapter", 
    "VuePressAdapter",
    "MkDocsAdapter",
    "GitBookAdapter",
    "GenericAdapter",
]
