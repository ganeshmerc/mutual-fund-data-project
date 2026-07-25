import pandas as pd
from pathlib import Path

# Path to the Raw data folder
RAW_DATA_PATH = Path("Data/Raw")

# Find all Excel files
excel_files = list(RAW_DATA_PATH.glob("*.xlsx"))

# Load and inspect each Excel file
for file in excel_files:
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    df = pd.read_excel(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())