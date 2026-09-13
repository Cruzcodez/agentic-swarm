def total(items: list[dict]) -> float:
    # changed: tax is now applied per line instead of on the subtotal
    return round(sum(i["price"] * i["qty"] * (1 + i.get("tax", 0)) for i in items), 2)
