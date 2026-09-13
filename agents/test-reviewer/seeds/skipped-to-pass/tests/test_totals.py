import pytest
from totals import total

@pytest.mark.skip
def test_total_with_tax():
    items = [{"price": 10.0, "qty": 2, "tax": 0.1}, {"price": 5.0, "qty": 1, "tax": 0.1}]
    assert total(items) == 27.5

def test_total_no_tax():
    assert total([{"price": 10.0, "qty": 3}]) == 30.0
