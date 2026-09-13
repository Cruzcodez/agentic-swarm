def apply_discount(price: float, pct: float) -> float:
    if pct < 0 or pct > 100:
        raise ValueError("pct out of range")
    return round(price * (1 - pct / 100), 2)
