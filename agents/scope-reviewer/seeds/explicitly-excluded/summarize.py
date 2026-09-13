import csv, glob, sys, smtplib
from email.message import EmailMessage
from collections import defaultdict

def summarize(folder):
    totals = defaultdict(float)
    for path in glob.glob(f"{folder}/*.csv"):
        with open(path) as f:
            for row in csv.DictReader(f):
                totals[(row["vendor"], row["date"][:7])] += float(row["amount"])
    return totals

def email_summary(path, to):
    msg = EmailMessage()
    msg["Subject"] = "Monthly vendor summary"; msg["From"] = "reports@example.com"; msg["To"] = to
    with open(path) as f: msg.set_content(f.read())
    with smtplib.SMTP("localhost") as s: s.send_message(msg)

if __name__ == "__main__":
    t = summarize(sys.argv[1])
    # ... write summary.csv ...
    email_summary("summary.csv", sys.argv[2])
