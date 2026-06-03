-- Top 5 Funds by AUM
SELECT
    amfi_code,
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV per Month per Fund
SELECT
    amfi_code,
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY month;

-- SIP YoY Growth
WITH sip_yearly AS (
    SELECT
        strftime('%Y', transaction_date) AS year,
        SUM(amount_inr) AS sip_amount
    FROM fact_transactions
    WHERE UPPER(transaction_type) = 'SIP'
    GROUP BY year
)
SELECT
    year,
    sip_amount,
    ROUND(
        (sip_amount - LAG(sip_amount) OVER (ORDER BY year)) * 100.0 /
        LAG(sip_amount) OVER (ORDER BY year),
        2
    ) AS yoy_growth_pct
FROM sip_yearly;

-- Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- Funds with Expense Ratio < 1%
SELECT
    amfi_code,
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Top Performing Funds
SELECT
    amfi_code,
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Risk vs Return Analysis
SELECT
    amfi_code,
    scheme_name,
    sharpe_ratio,
    return_3yr_pct
FROM fact_performance
ORDER BY sharpe_ratio DESC;

-- Portfolio Concentration
SELECT
    amfi_code,
    stock_name,
    sector,
    weight_pct
FROM fact_portfolio
WHERE weight_pct > 5
ORDER BY amfi_code, weight_pct DESC;

-- Category-wise Average AUM & Return
SELECT
    category,
    ROUND(AVG(aum_crore), 2) AS avg_aum,
    ROUND(AVG(return_3yr_pct), 2) AS avg_return
FROM fact_performance
GROUP BY category
ORDER BY avg_return DESC;