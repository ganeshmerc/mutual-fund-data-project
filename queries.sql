-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Top 5 expense ratios
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 3. Average 1-Year Return
SELECT AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance;

-- 4. Average 3-Year Return
SELECT AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance;

-- 5. Average 5-Year Return
SELECT AVG(return_5yr_pct) AS avg_return_5yr
FROM fact_performance;

-- 6. Count funds by category
SELECT category, COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;

-- 7. Count funds by fund house
SELECT fund_house, COUNT(*) AS total_funds
FROM dim_fund
GROUP BY fund_house;

-- 8. Average expense ratio by category
SELECT category,
AVG(expense_ratio_pct) AS avg_expense
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
GROUP BY category;

-- 9. Highest Morningstar Rating
SELECT scheme_name, morningstar_rating
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
ORDER BY morningstar_rating DESC;

-- 10. Average AUM by category
SELECT category,
AVG(aum_crore) AS avg_aum
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code=df.amfi_code
GROUP BY category;