import time
from bs4 import BeautifulSoup

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
""" * 10

soup = BeautifulSoup(html, 'lxml')

start = time.time()
for _ in range(1000):
    soup.select('meta[name="generator"]')
    soup.select('html[data-theme]')
    soup.select('.theme-doc-sidebar-menu')
    soup.select('.docusaurus')
    soup.select('script')
end = time.time()
print("Time taken select:", end - start)

start = time.time()
for _ in range(1000):
    soup.find_all('meta', attrs={'name': 'generator'})
    soup.find_all('html', attrs={'data-theme': True})
    soup.find_all(class_='theme-doc-sidebar-menu')
    soup.find_all(class_='docusaurus')
    soup.find_all('script')
end = time.time()
print("Time taken find_all:", end - start)
