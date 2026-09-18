import time
from bs4 import BeautifulSoup
from src.detector import detect_framework

html = """
<html>
    <head>
        <meta name="generator" content="docusaurus">
        <title>Test</title>
        <script src="docusaurus.js"></script>
    </head>
    <body class="docusaurus">
        <div class="theme-doc-sidebar-menu">menu</div>
    </body>
</html>
""" * 100

start = time.time()
for _ in range(10):
    detect_framework(html)
end = time.time()
print("Time taken detect_framework (original):", end - start)
