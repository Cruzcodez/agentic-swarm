from dates import parse_date
from datetime import date

def test_iso():
    assert parse_date("2026-09-13") == date(2026, 9, 13)
