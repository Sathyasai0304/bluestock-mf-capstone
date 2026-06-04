import pandas as pd
import sqlite3
from pathlib import Path

processed = Path("data/processed")
db_path = "data/db/bluestock_mf.db"

Path("data/db").mkdir(exist_ok=True)

conn = sqlite3.connect(db_path)

nav = pd.read_csv(processed / "nav_history_cleaned.csv")
txn = pd.read_csv(processed / "investor_transactions_cleaned.csv")
perf = pd.read_csv(processed / "scheme_performance_cleaned.csv")

nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
txn.to_sql("fact_transactions", conn, if_exists="replace", index=False)
perf.to_sql("fact_performance", conn, if_exists="replace", index=False)

print("SQLite database created and data loaded successfully")

conn.close()