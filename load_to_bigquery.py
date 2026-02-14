import os
import pandas as pd
from google.cloud import bigquery

PROJECT_ID = "retail-sales-analytics-484115"
DATASET_ID = "retail_dw"
TABLE_ID = "raw_sales"

def find_first_csv(raw_dir: str) -> str:
    csvs = [f for f in os.listdir(raw_dir) if f.lower().endswith(".csv")]
    if not csvs:
        raise FileNotFoundError("No CSV found in data/raw/")
    return os.path.join(raw_dir, csvs[0])

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    raw_dir = os.path.join(repo_root, "data", "raw")

    csv_path = find_first_csv(raw_dir)
    print(f"Reading: {csv_path}")

    df = pd.read_csv(csv_path)

    df.columns = (
        df.columns.astype(str)
        .str.strip().str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    df = df.dropna(how="all")

    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    if "month" in df.columns:
        df["month"] = pd.to_numeric(df["month"], errors="coerce").astype("Int64")

    for c in ["retail_sales", "retail_transfers", "warehouse_sales"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    print("Columns:", list(df.columns))
    print("Rows:", len(df))

    client = bigquery.Client(project=PROJECT_ID)

    client.create_dataset(f"{PROJECT_ID}.{DATASET_ID}", exists_ok=True)

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    print(f"Loading to BigQuery: {table_ref}")
    load_job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    load_job.result()

    table = client.get_table(table_ref)
    print(f"✅ Loaded {table.num_rows} rows into {table.full_table_id}")

if __name__ == "__main__":
    main()
