import sys
from unittest.mock import MagicMock

class MockHtml2Text:
    def handle(self, html):
        return "mocked markdown"

class MockHtml2TextModule:
    def HTML2Text(self):
        return MockHtml2Text()

sys.modules['bs4'] = MagicMock()
sys.modules['requests'] = MagicMock()
sys.modules['html2text'] = MockHtml2TextModule()
sys.modules['readability'] = MagicMock()
