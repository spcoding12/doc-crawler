import time
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>Test</title>
        <script src="some-random-script.js"></script>
        <script>
            var a = 1;
            console.log("hello world");
            // some very long script content...
            """ + "a = 1; " * 5000 + """
        </script>
        <script src="docusaurus.js"></script>
    </head>
    <body>
        <div class="test">content</div>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

start = time.time()
for _ in range(100):
    for tag in soup.select('script'):
        if 'docusaurus' in str(tag):
            pass
end = time.time()
print("Time taken str(tag):", end - start)

start = time.time()
for _ in range(100):
    for tag in soup.select('script'):
        if 'docusaurus' in tag.get('src', '').lower() or 'docusaurus' in tag.text.lower():
            pass
end = time.time()
print("Time taken get('src') + .text:", end - start)
