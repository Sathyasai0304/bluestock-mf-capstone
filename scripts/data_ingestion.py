import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

csv_files = list(raw_path.glob("*.csv"))

if not csv_files:
    print("No CSV files found in data/raw")

for file in csv_files:
    print("\n" + "=" * 50)
    print(f"File: {file.name}")

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nFirst 5 Rows:")
    print(df.head())
    print("\nMissing Values:")
    print(df.isnull().sum())