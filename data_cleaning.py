import pandas as pd

# Load the scheme performance dataset
df = pd.read_csv("Data/Raw/07_scheme_performance.csv")

# Remove completely empty rows
df = df.dropna(how="all")

# Display basic information
print(df.head())
print(df.columns)
print(df.info())

# List of numeric columns to validate
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

# Convert columns to numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for missing values
print("\nMissing values in numeric columns:")
print(df[numeric_cols].isnull().sum())

# Validate expense ratio
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid expense ratios:", len(invalid_expense))

if len(invalid_expense) == 0:
    print("✅ All expense ratios are within range (0.1% - 2.5%)")
else:
    print("❌ Invalid expense ratios found")
    print(invalid_expense[["scheme_name", "expense_ratio_pct"]])

# Save cleaned dataset
df.to_csv(
    "Data/Processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\n✅ Scheme performance cleaned and saved successfully!")