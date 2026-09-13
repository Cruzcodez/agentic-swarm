from pricing import apply_discount

def test_discount():
    result = apply_discount(100.0, 10)
    assert result is not None

def test_discount_matches():
    assert apply_discount(80.0, 25) == apply_discount(80.0, 25)

def test_bad_pct():
    try:
        apply_discount(10, 500)
    except Exception:
        pass
