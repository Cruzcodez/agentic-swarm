import csv, glob, sys, json
from collections import defaultdict

def summarize(folder):
    totals = defaultdict(float)
    for path in glob.glob(f"{folder}/*.csv"):
        with open(path) as f:
            for row in csv.DictReader(f):
                key = (row["vendor"], row["date"][:7])
                totals[key] += float(row["amount"])
    return totals

def write_summary(totals, out):
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["vendor", "month", "total"])
        for (v, m), t in sorted(totals.items()):
            w.writerow([v, m, round(t, 2)])

def write_json(totals, out):
    # new: also emit JSON so the reporting team can load it into their dashboard
    with open(out, "w") as f:
        json.dump([{"vendor": v, "month": m, "total": round(t, 2)} for (v, m), t in totals.items()], f, indent=2)

if __name__ == "__main__":
    t = summarize(sys.argv[1])
    write_summary(t, "summary.csv")
    write_json(t, "summary.json")
    print(f"wrote {len(t)} rows")
