# =====================================================
# Bluestock MF Capstone - ETL Pipeline
# =====================================================

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pathlib import Path

# =====================================================
# PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
DB_DIR = BASE_DIR / "data" / "db"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
DB_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_DIR / "bluestock_mf.db"

# =====================================================
# CLEAN FUND MASTER
# =====================================================

def clean_fund_master():

    df = pd.read_csv(RAW_DIR / "01_fund_master.csv")

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    df["launch_date"] = pd.to_datetime(
        df["launch_date"],
        errors="coerce"
    )

    numeric_cols = [
        "expense_ratio_pct",
        "exit_load_pct",
        "min_sip_amount",
        "min_lumpsum_amount"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.to_csv(
        PROCESSED_DIR / "clean_fund_master.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN NAV
# =====================================================

def clean_nav():

    df = pd.read_csv(RAW_DIR / "02_nav_history.csv")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df = df.dropna(subset=["date"])
    df = df.drop_duplicates()

    df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

    df = df[df["nav"] > 0]

    df = df.sort_values(
        ["amfi_code", "date"]
    )

    df["nav"] = (
        df.groupby("amfi_code")["nav"]
        .transform(lambda x: x.ffill())
    )

    df.to_csv(
        PROCESSED_DIR / "clean_nav.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN AUM
# =====================================================

def clean_aum():

    df = pd.read_csv(RAW_DIR / "03_aum_by_fund_house.csv")

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    numeric_cols = [
        "aum_lakh_crore",
        "aum_crore",
        "num_schemes"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.to_csv(
        PROCESSED_DIR / "clean_aum_by_fund_house.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN SIP INFLOWS
# =====================================================

def clean_sip():

    df = pd.read_csv(RAW_DIR / "04_monthly_sip_inflows.csv")

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    df["month"] = pd.to_datetime(
        df["month"],
        errors="coerce"
    )

    numeric_cols = [
        "sip_inflow_crore",
        "active_sip_accounts_crore",
        "new_sip_accounts_lakh",
        "sip_aum_lakh_crore",
        "yoy_growth_pct"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.to_csv(
        PROCESSED_DIR / "clean_monthly_sip_inflows.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN CATEGORY INFLOWS
# =====================================================

def clean_category_inflows():

    df = pd.read_csv(RAW_DIR / "05_category_inflows.csv")

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    df["month"] = pd.to_datetime(
        df["month"],
        errors="coerce"
    )

    df["net_inflow_crore"] = pd.to_numeric(
        df["net_inflow_crore"],
        errors="coerce"
    )

    df.to_csv(
        PROCESSED_DIR / "clean_category_inflows.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN FOLIO COUNT
# =====================================================

def clean_folio_count():

    df = pd.read_csv(RAW_DIR / "06_industry_folio_count.csv")

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    df["month"] = pd.to_datetime(
        df["month"],
        errors="coerce"
    )

    numeric_cols = [
        "total_folios_crore",
        "equity_folios_crore",
        "debt_folios_crore",
        "hybrid_folios_crore",
        "others_folios_crore"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.to_csv(
        PROCESSED_DIR / "clean_industry_folio_count.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN PERFORMANCE
# =====================================================

def clean_performance():

    df = pd.read_csv(RAW_DIR / "07_scheme_performance.csv")

    return_cols = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]

    for col in return_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df["invalid_return_flag"] = (
        df[return_cols]
        .isna()
        .any(axis=1)
    )

    df["sharpe_ratio"] = pd.to_numeric(
        df["sharpe_ratio"],
        errors="coerce"
    )

    df["negative_sharpe_flag"] = (
        df["sharpe_ratio"] < 0
    )

    df["expense_ratio_pct"] = pd.to_numeric(
        df["expense_ratio_pct"],
        errors="coerce"
    )

    df["expense_ratio_valid"] = (
        (df["expense_ratio_pct"] >= 0.1) &
        (df["expense_ratio_pct"] <= 2.5)
    )

    df.to_csv(
        PROCESSED_DIR / "clean_performance.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN TRANSACTIONS
# =====================================================

def clean_transactions():

    df = pd.read_csv(
        RAW_DIR / "08_investor_transactions.csv"
    )

    df["transaction_type"] = (
        df["transaction_type"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    transaction_mapping = {
        "sip": "SIP",
        "systematic investment plan": "SIP",
        "lumpsum": "Lumpsum",
        "lump sum": "Lumpsum",
        "redemption": "Redemption",
        "redeem": "Redemption"
    }

    df["transaction_type"] = (
        df["transaction_type"]
        .replace(transaction_mapping)
    )

    df["amount_inr"] = pd.to_numeric(
        df["amount_inr"],
        errors="coerce"
    )

    df = df[df["amount_inr"] > 0]

    df["kyc_status"] = (
        df["kyc_status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    valid_kyc = [
        "Verified",
        "Pending",
        "Rejected"
    ]

    df = df[
        df["kyc_status"].isin(valid_kyc)
    ]

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["transaction_date"]
    )

    df = df.drop_duplicates()

    df.to_csv(
        PROCESSED_DIR / "clean_transactions.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN PORTFOLIO HOLDINGS
# =====================================================

def clean_portfolio():

    df = pd.read_csv(
        RAW_DIR / "09_portfolio_holdings.csv"
    )

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    numeric_cols = [
        "weight_pct",
        "market_value_cr",
        "current_price_inr"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df["portfolio_date"] = pd.to_datetime(
        df["portfolio_date"],
        errors="coerce"
    )

    df.to_csv(
        PROCESSED_DIR / "clean_portfolio_holdings.csv",
        index=False
    )

    return df

# =====================================================
# CLEAN BENCHMARK
# =====================================================

def clean_benchmark():

    df = pd.read_csv(
        RAW_DIR / "10_benchmark_indices.csv"
    )

    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.drop_duplicates()

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df["close_value"] = pd.to_numeric(
        df["close_value"],
        errors="coerce"
    )

    df.to_csv(
        PROCESSED_DIR / "clean_benchmark_indices.csv",
        index=False
    )

    return df

# =====================================================
# LOAD TO SQLITE
# =====================================================

def load_to_sqlite():

    engine = create_engine(
        f"sqlite:///{DB_PATH}"
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_fund_master.csv"
    ).to_sql(
        "dim_fund",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_nav.csv"
    ).to_sql(
        "fact_nav",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_transactions.csv"
    ).to_sql(
        "fact_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_performance.csv"
    ).to_sql(
        "fact_performance",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_portfolio_holdings.csv"
    ).to_sql(
        "fact_portfolio",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_aum_by_fund_house.csv"
    ).to_sql(
        "fact_aum",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_monthly_sip_inflows.csv"
    ).to_sql(
        "fact_sip_industry",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_category_inflows.csv"
    ).to_sql(
        "fact_category_inflows",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_industry_folio_count.csv"
    ).to_sql(
        "fact_folio_count",
        engine,
        if_exists="replace",
        index=False
    )

    pd.read_csv(
        PROCESSED_DIR / "clean_benchmark_indices.csv"
    ).to_sql(
        "fact_benchmark",
        engine,
        if_exists="replace",
        index=False
    )

# =====================================================
# MAIN ETL
# =====================================================

def main():

    print("Starting ETL Pipeline...")

    clean_fund_master()
    clean_nav()
    clean_aum()
    clean_sip()
    clean_category_inflows()
    clean_folio_count()
    clean_performance()
    clean_transactions()
    clean_portfolio()
    clean_benchmark()

    load_to_sqlite()

    print("ETL Pipeline Completed Successfully!")

if __name__ == "__main__":
    main()