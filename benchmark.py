import timeit
from src.extractor import clean_markdown

test_str = """
# Header
chevron-right something
Copy
##
[Home] / something / another
* [link](url)
""" * 100

def test():
    clean_markdown(test_str)

print("Time taken:", timeit.timeit(test, number=100))
