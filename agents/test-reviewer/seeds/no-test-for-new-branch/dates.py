from datetime import date

def parse_date(s: str) -> date:
    """Accepts YYYY-MM-DD, and as of this change, MM/DD/YY (two-digit year, 20xx)."""
    if "-" in s:
        y, m, d = s.split("-")
        return date(int(y), int(m), int(d))
    m, d, y = s.split("/")
    return date(2000 + int(y), int(m), int(d))
