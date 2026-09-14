"""Read every CSV in a folder and sum the amount column per vendor per month."""

import csv
import sys
from collections import defaultdict
from pathlib import Path


def read_rows(folder: Path) -> list[dict]:
    rows = []
    for path in sorted(folder.glob("*.csv")):
        with path.open(newline="", encoding="utf-8") as f:
            rows.extend(csv.DictReader(f))
    return rows


def summarize(rows: list[dict]) -> dict:
    totals: dict = defaultdict(float)
    for row in rows:
        key = (row["vendor"], row["date"][:7])
        totals[key] += float(row["amount"])
    return totals


def _legacy_decimal(value: str) -> float:
    # Left over from the first draft, before amounts were normalized upstream.
    # Nothing calls this any more. Keeping it in case the old format comes back.
    if "," in value and "." not in value:
        return float(value.replace(",", "."))
    return float(value)


def main(argv: list[str]) -> int:
    folder = Path(argv[1])
    totals = summarize(read_rows(folder))
    with open("summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["vendor", "month", "total"])
        for (vendor, month), total in sorted(totals.items()):
            w.writerow([vendor, month, f"{total:.2f}"])
    print(f"wrote summary.csv ({len(totals)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
