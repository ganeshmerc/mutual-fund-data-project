USE mutual_fund_analysis;
SHOW DATABASES;
USE mutual_fund_analysis;
SHOW TABLES;
SELECT * FROM fund_master LIMIT 10;

SELECT scheme_name, fund_house, category, expense_ratio_pct
FROM fund_master
LIMIT 20;

SELECT scheme_name, fund_house, category
FROM fund_master
WHERE category = 'Equity';

SELECT scheme_name, expense_ratio_pct
FROM fund_master
WHERE expense_ratio_pct > 1.5;


SELECT scheme_name, expense_ratio_pct
FROM fund_master
ORDER BY expense_ratio_pct DESC
LIMIT 10;

SELECT category, COUNT(*) AS fund_count
FROM fund_master
GROUP BY category;

SELECT fund_house, AVG(expense_ratio_pct) AS avg_expense
FROM fund_master
GROUP BY fund_house
ORDER BY avg_expense DESC;

SELECT fund_house, COUNT(*) AS fund_count
FROM fund_master
GROUP BY fund_house
HAVING COUNT(*) > 5;

SELECT scheme_name, expense_ratio_pct
FROM fund_master
WHERE expense_ratio_pct > (SELECT AVG(expense_ratio_pct) FROM fund_master);

SELECT scheme_name, category, expense_ratio_pct,
       RANK() OVER (PARTITION BY category ORDER BY expense_ratio_pct DESC) AS rank_in_category
FROM fund_master;