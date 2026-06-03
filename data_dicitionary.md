# 📘 Data Dictionary 

## Table: fact_transactions

| Column Name        | Data Type | Description                     | Allowed Values / Rules        | Source File |
|-------------------|----------|---------------------------------|-------------------------------|-------------|
| investor_id       | TEXT     | Unique ID of investor          | Alphanumeric                  | investor_transactions.csv |
| transaction_date  | TEXT     | Date of transaction            | YYYY-MM-DD format            | investor_transactions.csv |
| amfi_code         | INTEGER  | Mutual fund scheme code        | Numeric                      | investor_transactions.csv |
| transaction_type  | TEXT     | Type of transaction            | SIP / Lumpsum / Redemption   | investor_transactions.csv |
| amount_inr        | FLOAT    | Transaction amount in INR      | Must be > 0                  | investor_transactions.csv |
| state             | TEXT     | Investor state                 | Valid Indian states          | investor_transactions.csv |
| city              | TEXT     | Investor city                  | Valid city names             | investor_transactions.csv |
| city_tier         | TEXT     | City classification            | Tier 1 / Tier 2 / Tier 3     | investor_transactions.csv |
| age_group         | TEXT     | Age group of investor          | 18-25 / 26-35 / 36-50 / 50+  | investor_transactions.csv |
| gender            | TEXT     | Gender of investor             | Male / Female / Other        | investor_transactions.csv |
| annual_income_lakh| FLOAT    | Annual income (in lakhs)       | Positive numeric             | investor_transactions.csv |
| payment_mode      | TEXT     | Payment method                 | UPI / NetBanking / Card      | investor_transactions.csv |
| kyc_status        | TEXT     | KYC verification status        | Verified / Pending / Failed  | investor_transactions.csv |

---

## Table: dim_fund_master

| Column Name   | Data Type | Description                    | Allowed Values / Rules   | Source File |
|--------------|----------|--------------------------------|--------------------------|-------------|
| amfi_code    | INTEGER  | Unique fund scheme code        | Primary key              | fund_master.csv |
| scheme_name  | TEXT     | Mutual fund scheme name        | Text                     | fund_master.csv |
| fund_house   | TEXT     | Asset management company       | SBI / HDFC / ICICI etc   | fund_master.csv |
| category     | TEXT     | Fund category                 | Equity / Debt / Hybrid   | fund_master.csv |
| sub_category | TEXT     | Fund sub-category             | Large Cap / Mid Cap etc  | fund_master.csv |
| risk_level   | TEXT     | Risk level                    | Low / Medium / High      | fund_master.csv |

---

## Table: fact_nav_history

| Column Name | Data Type | Description              | Allowed Values / Rules | Source File |
|------------|----------|--------------------------|------------------------|-------------|
| amfi_code  | INTEGER  | Scheme code              | Numeric                | nav_history.csv |
| date       | TEXT     | NAV date                 | YYYY-MM-DD format      | nav_history.csv |
| nav        | FLOAT    | Net Asset Value          | Must be > 0           | nav_history.csv |

---

## Table: fact_performance

| Column Name       | Data Type | Description                    | Allowed Values / Rules | Source File |
|------------------|----------|--------------------------------|------------------------|-------------|
| amfi_code        | INTEGER  | Scheme code                   | Numeric                | performance.csv |
| scheme_name      | TEXT     | Scheme name                   | Text                   | performance.csv |
| fund_house       | TEXT     | Fund house                    | Text                   | performance.csv |
| category         | TEXT     | Fund category                 | Equity / Debt / Hybrid | performance.csv |
| plan             | TEXT     | Investment plan               | Growth / Dividend      | performance.csv |
| return_1yr_pct   | FLOAT    | 1-year return %               | Numeric                | performance.csv |
| return_3yr_pct   | FLOAT    | 3-year return %               | Numeric                | performance.csv |
| return_4yr_pct   | FLOAT    | 4-year return %               | Numeric                | performance.csv |
| benchmark_3yr_pct| FLOAT    | Benchmark return              | Numeric                | performance.csv |
| alpha            | FLOAT    | Excess return over benchmark  | Numeric                | performance.csv |
| beta             | FLOAT    | Market sensitivity            | 0–2 typical range      | performance.csv |
| sharpe_ratio     | FLOAT    | Risk-adjusted return          | Can be negative        | performance.csv |

---

## Table: fact_portfolio_holdings

| Column Name       | Data Type | Description                 | Allowed Values / Rules | Source File |
|------------------|----------|-----------------------------|------------------------|-------------|
| amfi_code        | INTEGER  | Scheme code                | Numeric                | portfolio_holdings.csv |
| stock_symbol     | TEXT     | Stock ticker               | NSE / BSE symbols     | portfolio_holdings.csv |
| stock_name       | TEXT     | Company name               | Text                  | portfolio_holdings.csv |
| sector           | TEXT     | Industry sector            | IT / Banking / Pharma | portfolio_holdings.csv |
| weight_pct       | FLOAT    | Portfolio weight (%)       | 0–100                 | portfolio_holdings.csv |
| market_value_cr  | FLOAT    | Market value (crores)      | Positive number       | portfolio_holdings.csv |
| current_price_inr| FLOAT    | Current stock price        | Must be > 0           | portfolio_holdings.csv |
| portfolio_date   | TEXT     | Snapshot date              | YYYY-MM-DD format     | portfolio_holdings.csv |

---
