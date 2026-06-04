import requests
import pandas as pd
from pathlib import Path

scheme_codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

raw_folder = Path("data/raw")

for code in scheme_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        json_data = response.json()

        nav_df = pd.DataFrame(json_data["data"])

        file_name = f"{code}_nav.csv"

        nav_df.to_csv(
            raw_folder / file_name,
            index=False
        )

        print(f"Saved {file_name}")

    else:
        print(f"Failed {code}")