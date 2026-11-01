import time
import tracemalloc
from src.extractor import clean_markdown
from bs4 import BeautifulSoup
import html2text

def test_html2text_perf():
    html_content = "<h1>Title</h1>" + "<p>Some content</p>" * 1000

    start_time = time.time()
    for _ in range(100):
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0
        h.unicode_snob = True
        h.skip_internal_links = False
        h.handle(html_content)
    end_time = time.time()
    print(f"Time with instantiation: {end_time - start_time:.4f}s")

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = False

    start_time = time.time()
    for _ in range(100):
        h.handle(html_content)
    end_time = time.time()
    print(f"Time without instantiation: {end_time - start_time:.4f}s")

test_html2text_perf()
