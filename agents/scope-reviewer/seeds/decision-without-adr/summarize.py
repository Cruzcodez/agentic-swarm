import glob, sys, sqlite3, csv

DB = "invoices.db"

def load(folder):
    # switched from in-memory dicts to sqlite so we can run ad-hoc queries later
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS invoices (vendor TEXT, month TEXT, amount REAL)")
    for path in glob.glob(f"{folder}/*.csv"):
        with open(path) as f:
            rows = [(r["vendor"], r["date"][:7], float(r["amount"])) for r in csv.DictReader(f)]
        conn.executemany("INSERT INTO invoices VALUES (?,?,?)", rows)
    conn.commit()
    return conn

def summarize(conn):
    return conn.execute("SELECT vendor, month, ROUND(SUM(amount),2) FROM invoices GROUP BY vendor, month ORDER BY 1,2").fetchall()
