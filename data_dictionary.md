# Mutual Fund Data Dictionary

## 1. NAV History

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique Mutual Fund Identifier |
| date | Date | NAV Date |
| nav | Float | Net Asset Value |

---

## 2. Investor Transactions

| Column | Data Type | Description |
|--------|-----------|-------------|
| investor_id | Text | Unique Investor ID |
| transaction_date | Date | Transaction Date |
| amfi_code | Integer | Mutual Fund Identifier |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction Amount |
| state | Text | Investor State |
| city | Text | Investor City |
| city_tier | Text | T30 / B30 |
| age_group | Text | Investor Age Group |
| gender | Text | Male / Female |
| annual_income_lakh | Float | Annual Income (Lakhs) |
| payment_mode | Text | UPI / Cheque / Net Banking / Mandate |
| kyc_status | Text | Verified / Pending |

---

## 3. Scheme Performance

| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Mutual Fund Identifier |
| scheme_name | Text | Mutual Fund Scheme Name |
| fund_house | Text | Fund House |
| category | Text | Fund Category |
| plan | Text | Direct / Regular |
| return_1yr_pct | Float | 1 Year Return (%) |
| return_3yr_pct | Float | 3 Year Return (%) |
| return_5yr_pct | Float | 5 Year Return (%) |
| benchmark_3yr_pct | Float | Benchmark Return (%) |
| alpha | Float | Alpha |
| beta | Float | Beta |
| sharpe_ratio | Float | Sharpe Ratio |
| sortino_ratio | Float | Sortino Ratio |
| std_dev_ann_pct | Float | Annual Standard Deviation |
| max_drawdown_pct | Float | Maximum Drawdown |
| aum_crore | Float | Assets Under Management (Crores) |
| expense_ratio_pct | Float | Expense Ratio (%) |
| morningstar_rating | Integer | Morningstar Rating |
| risk_grade | Text | Risk Category |