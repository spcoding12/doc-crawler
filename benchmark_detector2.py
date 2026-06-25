import time
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="generator" content="docusaurus v2.0.0">
    <title>Test Page</title>
</head>
<body>
    <div class="theme-doc-sidebar-container">
        <ul class="theme-doc-sidebar-menu">
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </div>
    <div class="docusaurus">Main Content</div>
    <script src="/js/docusaurus.js"></script>
""" + "<script>console.log('test');</script>" * 1000 + """
</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

start = time.time()
for _ in range(100):
    elements = soup.select('script')
    for el in elements:
        'docusaurus' in str(el)
end = time.time()
print(f"soup.select + str(tag) Time taken: {end - start:.4f} seconds")

start = time.time()
for _ in range(100):
    elements = soup.find_all('script')
    for el in elements:
        'docusaurus' in (el.get('src', '') + el.text)
end = time.time()
print(f"find_all + get/text Time taken: {end - start:.4f} seconds")
