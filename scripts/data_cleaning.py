import pandas as pd
from pathlib import Path

raw = Path("data/raw")
processed = Path("data/processed")

processed.mkdir(exist_ok=True)

df = pd.read_csv(raw / "02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates()

df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df[df["nav"] > 0]

df.to_csv(processed / "nav_history_cleaned.csv", index=False)

print("NAV history cleaned successfully")

import pandas as pd
from pathlib import Path

raw = Path("data/raw")
processed = Path("data/processed")

df = pd.read_csv(raw / "08_investor_transactions.csv")

# clean column names
df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", "")

# date fix
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# standardise transaction type
df["transaction_type"] = df["transaction_type"].str.upper().str.strip()

valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]
df = df[df["transaction_type"].isin(valid_types)]

# amount validation
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")
df = df[df["amount_inr"] > 0]

# kyc validation
df["kyc_status"] = df["kyc_status"].str.upper().str.strip()
valid_kyc = ["YES", "NO", "PENDING"]
df = df[df["kyc_status"].isin(valid_kyc)]

# remove duplicates
df = df.drop_duplicates()

# save cleaned file
df.to_csv(processed / "investor_transactions_cleaned.csv", index=False)

print("Investor transactions cleaned successfully")

df = pd.read_csv(raw / "07_scheme_performance.csv")

# clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("%", "")

# convert numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# drop rows with missing key metrics
df = df.dropna(subset=["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"])

# filter expense ratio (0.1% - 2.5%)
if "expense_ratio_pct" in df.columns:
    df = df[(df["expense_ratio_pct"] >= 0.1) & (df["expense_ratio_pct"] <= 2.5)]

# save cleaned file
df.to_csv(processed / "scheme_performance_cleaned.csv", index=False)

print("Scheme performance cleaned successfully")