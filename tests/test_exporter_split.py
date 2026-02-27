"""
测试 exporter 模块的拆分功能
"""
import sys
import tempfile
from pathlib import Path

root_dir = str(Path(__file__).parent.parent)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from src.exporter import (
    PageContent,
    export_single_markdown,
    _get_directory_key,
    _group_pages_by_directory,
    _split_groups_into_parts,
    _render_pages_to_markdown,
)


def _make_page(url, title, markdown, level=0):
    """辅助函数：创建 PageContent"""
    return PageContent(url=url, title=title, markdown=markdown, images=[], level=level)


class TestGetDirectoryKey:
    def test_normal_path(self):
        assert _get_directory_key("https://docs.example.com/guide/getting-started") == "guide"

    def test_deep_path(self):
        assert _get_directory_key("https://docs.example.com/api/v2/users") == "api"

    def test_root_path(self):
        assert _get_directory_key("https://docs.example.com/") == "_root"

    def test_single_segment(self):
        assert _get_directory_key("https://docs.example.com/index") == "index"


class TestGroupPagesByDirectory:
    def test_grouping(self):
        pages = [
            _make_page("https://example.com/guide/intro", "Intro", "content1"),
            _make_page("https://example.com/guide/setup", "Setup", "content2"),
            _make_page("https://example.com/api/users", "Users API", "content3"),
            _make_page("https://example.com/api/auth", "Auth API", "content4"),
        ]
        groups = _group_pages_by_directory(pages)
        keys = list(groups.keys())
        assert keys == ["guide", "api"]
        assert len(groups["guide"]) == 2
        assert len(groups["api"]) == 2

    def test_preserves_order(self):
        pages = [
            _make_page("https://example.com/a/1", "A1", "c"),
            _make_page("https://example.com/b/1", "B1", "c"),
            _make_page("https://example.com/a/2", "A2", "c"),
        ]
        groups = _group_pages_by_directory(pages)
        keys = list(groups.keys())
        # 'a' 先出现，所以排在前面
        assert keys == ["a", "b"]
        assert len(groups["a"]) == 2


class TestSplitGroupsIntoParts:
    def test_no_split_needed(self):
        """总字符数小于阈值，应只有1个分片"""
        pages_a = [_make_page("https://e.com/a/1", "A1", "x" * 100)]
        pages_b = [_make_page("https://e.com/b/1", "B1", "x" * 100)]
        from collections import OrderedDict
        groups = OrderedDict([("a", pages_a), ("b", pages_b)])
        parts = _split_groups_into_parts(groups, max_chars=100_000)
        assert len(parts) == 1

    def test_split_into_multiple(self):
        """两组各超 5000 字符，阈值设为 6000，应拆为2个分片"""
        pages_a = [_make_page("https://e.com/a/1", "A1", "x" * 5000)]
        pages_b = [_make_page("https://e.com/b/1", "B1", "y" * 5000)]
        from collections import OrderedDict
        groups = OrderedDict([("a", pages_a), ("b", pages_b)])
        parts = _split_groups_into_parts(groups, max_chars=6000)
        assert len(parts) == 2

    def test_single_large_group_not_split(self):
        """单个分组超出阈值，不应被强行拆散"""
        pages_a = [_make_page("https://e.com/a/1", "A1", "x" * 10000)]
        from collections import OrderedDict
        groups = OrderedDict([("a", pages_a)])
        parts = _split_groups_into_parts(groups, max_chars=5000)
        assert len(parts) == 1
        assert parts[0][0][0] == "a"


class TestExportSingleMarkdownSplit:
    def test_small_content_no_split(self):
        """小文档不拆分，输出单个文件"""
        pages = [
            _make_page("https://e.com/a/1", "Title A", "Small content"),
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            result = export_single_markdown(pages, Path(tmpdir), "test.md", max_chars=100_000)
            assert len(result) == 1
            assert result[0].name == "test.md"
            content = result[0].read_text(encoding='utf-8')
            assert "Title A" in content

    def test_large_content_splits(self):
        """大文档应被拆分为多个 part 文件"""
        pages = [
            _make_page("https://e.com/guide/intro", "Guide Intro", "A" * 3000),
            _make_page("https://e.com/guide/setup", "Guide Setup", "B" * 3000),
            _make_page("https://e.com/api/ref", "API Ref", "C" * 3000),
            _make_page("https://e.com/api/auth", "API Auth", "D" * 3000),
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            # 设置很小的阈值，强制拆分
            result = export_single_markdown(pages, Path(tmpdir), "doc_all.md", max_chars=7000)
            assert len(result) >= 2
            # 验证文件名格式
            names = [f.name for f in result]
            assert "doc_all_part1.md" in names
            assert "doc_all_part2.md" in names
            # 验证每个文件都包含分片头部信息
            for f in result:
                content = f.read_text(encoding='utf-8')
                assert "部分" in content  # 头部包含 "第 X / Y 部分"

    def test_split_preserves_all_content(self):
        """拆分后所有页面内容都应保留"""
        unique_markers = [f"UNIQUE_MARKER_{i}" for i in range(4)]
        pages = [
            _make_page("https://e.com/a/1", "Page1", unique_markers[0] * 500),
            _make_page("https://e.com/a/2", "Page2", unique_markers[1] * 500),
            _make_page("https://e.com/b/1", "Page3", unique_markers[2] * 500),
            _make_page("https://e.com/b/2", "Page4", unique_markers[3] * 500),
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            result = export_single_markdown(pages, Path(tmpdir), "test.md", max_chars=3000)
            # 合并所有分片的内容
            all_content = ""
            for f in result:
                all_content += f.read_text(encoding='utf-8')
            # 每个唯一标记都应在合并后的内容中
            for marker in unique_markers:
                assert marker in all_content
