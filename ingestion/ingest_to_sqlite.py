import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # .../ingestion
REPO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # repo root

RAW_PATH = os.path.join(REPO_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(REPO_DIR, "data", "processed")
DB_PATH = os.path.join(os.environ["TEMP"], "retail.db")

TABLE_RAW = "raw_sales"

def main():
    os.makedirs(PROCESSED_DIR, exist_ok=True)


    csv_files = [f for f in os.listdir(RAW_PATH) if f.lower().endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError("No CSV found in data/raw/. Put your dataset there first.")

    csv_path = os.path.join(RAW_PATH, csv_files[0])
    print(f"Reading: {csv_path}")

    df = pd.read_csv(csv_path)

    # Standardize column names
    df.columns = (
        df.columns.astype(str)
        .str.strip().str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    df = df.dropna(how="all")

    print("Columns:", list(df.columns))
    print("Rows:", len(df))

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql(TABLE_RAW, conn, if_exists="replace", index=False)

    print(f"Loaded table '{TABLE_RAW}' into {DB_PATH}")

if __name__ == "__main__":
    main()
