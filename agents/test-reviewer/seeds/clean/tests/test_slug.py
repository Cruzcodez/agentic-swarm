import pytest
from slug import slugify

@pytest.mark.parametrize("given,expected", [
    ("Hello World", "hello-world"),
    ("  spaced  out  ", "spaced-out"),
    ("Already-slug", "already-slug"),
    ("symbols!@#here", "symbols-here"),
    ("", "untitled"),
    ("!!!", "untitled"),
])
def test_slugify(given, expected):
    assert slugify(given) == expected
