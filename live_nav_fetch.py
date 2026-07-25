import requests
import pandas as pd
from pathlib import Path

# MFAPI scheme codes
schemes = {
    "HDFC_Top_100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

# Create output folder
output_dir = Path("Data/Raw/Live_NAV")
output_dir.mkdir(parents=True, exist_ok=True)

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        scheme_info = data["meta"]
        nav_data = data["data"]

        df = pd.DataFrame(nav_data)

        df["scheme_code"] = scheme_code
        df["scheme_name"] = scheme_info["scheme_name"]

        filename = output_dir / f"{scheme_name}_{scheme_code}.csv"

        df.to_csv(filename, index=False)

        print(f"Successfully fetched: {scheme_name}")
        print(f"Records: {len(df)}")
        print(f"Saved to: {filename}")

    else:
        print(f"Failed to fetch {scheme_name}")