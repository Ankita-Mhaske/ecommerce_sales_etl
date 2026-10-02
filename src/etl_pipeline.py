"""
E-commerce Sales ETL Pipeline

"""

from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "data" / "raw_sales.csv"
CLEAN_FILE = BASE_DIR / "data" / "clean_sales.csv"
DB_FILE = BASE_DIR / "data" / "sales.db"


def extract():
    return pd.read_csv(RAW_FILE)


def transform(df):
    df = df.copy()

    duplicate_count = df.duplicated(subset=["order_id"]).sum()

    df.columns = df.columns.str.strip().str.lower()
    df["order_date"] = pd.to_datetime(
    df["order_date"],
    format="%d-%m-%Y",
    errors="coerce"
)

    numeric_cols = ["quantity", "unit_price", "sales_amount"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.drop_duplicates(subset=["order_id"])
    df = df.dropna(subset=["order_id", "order_date", "product", "quantity", "unit_price"])

    df["state"] = df["state"].fillna("Unknown")

    invalid_count = ((df["quantity"] <= 0) | (df["unit_price"] <= 0)).sum()

    df = df[(df["quantity"] > 0) & (df["unit_price"] > 0)]

    incorrect_sales_count = (
    df["sales_amount"] != df["quantity"] * df["unit_price"]
    ).sum()

    df["sales_amount"] = df["quantity"] * df["unit_price"]
    df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

    return df, duplicate_count, invalid_count, incorrect_sales_count


def load(df):
    df.to_csv(CLEAN_FILE, index=False)

    with sqlite3.connect(DB_FILE) as conn:
        df.to_sql("sales", conn, if_exists="replace", index=False)


def main():
    data = extract()
    cleaned_data, duplicate_count, invalid_count, incorrect_sales_count = transform(data)
    load(cleaned_data)

    print(f"Extracted rows: {len(data)}")
    print(f"Duplicate rows removed: {duplicate_count}")
    print(f"Invalid rows removed: {invalid_count}")
    print(f"Incorrect sales amounts fixed: {incorrect_sales_count}")
    print(f"Loaded rows: {len(cleaned_data)}")
    print(f"Clean file: {CLEAN_FILE}")
    print(f"Database: {DB_FILE}")


if __name__ == "__main__":
    main()
