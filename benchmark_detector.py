import time
from bs4 import BeautifulSoup
from src.detector import detect_framework

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
</body>
</html>
""" * 100

start = time.time()
for _ in range(100):
    detect_framework(html)
end = time.time()
print(f"Time taken: {end - start:.4f} seconds")
