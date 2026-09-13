import csv, glob, sys
from collections import defaultdict

def summarize(folder):
    totals = defaultdict(float)
    for path in glob.glob(f"{folder}/*.csv"):
        with open(path) as f:
            for row in csv.DictReader(f):
                totals[(row["vendor"], row["date"][:7])] += float(row["amount"])
    return totals

def write_summary(totals, out):
    with open(out, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["vendor", "month", "total"])
        for (v, m), t in sorted(totals.items()):
            w.writerow([v, m, round(t, 2)])

if __name__ == "__main__":
    t = summarize(sys.argv[1])
    write_summary(t, "summary.csv")
    print(f"wrote {len(t)} rows to summary.csv")
