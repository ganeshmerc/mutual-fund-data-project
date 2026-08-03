import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned CSV files
nav = pd.read_csv("Data/Processed/02_nav_history_cleaned.csv")
transactions = pd.read_csv("Data/Processed/08_investor_transactions_cleaned.csv")
performance = pd.read_csv("Data/Processed/07_scheme_performance_cleaned.csv")

# Create dim_fund table
dim_fund = performance[
    ["amfi_code", "scheme_name", "fund_house", "category", "plan", "risk_grade"]
].drop_duplicates()

dim_fund.to_sql("dim_fund", engine, if_exists="replace", index=False)

# Create fact_nav
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

# Create fact_transactions
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

# Create fact_performance
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("✅ SQLite database created successfully!")

print("\nRow Counts")
print("dim_fund:", len(dim_fund))
print("fact_nav:", len(nav))
print("fact_transactions:", len(transactions))
print("fact_performance:", len(performance))