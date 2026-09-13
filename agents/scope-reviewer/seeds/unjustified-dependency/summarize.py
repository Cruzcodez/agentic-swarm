import pandas as pd, glob, sys

def summarize(folder):
    df = pd.concat(pd.read_csv(p) for p in glob.glob(f"{folder}/*.csv"))
    df["month"] = df["date"].str[:7]
    return df.groupby(["vendor", "month"])["amount"].sum().round(2).reset_index()

if __name__ == "__main__":
    summarize(sys.argv[1]).to_csv("summary.csv", index=False)
