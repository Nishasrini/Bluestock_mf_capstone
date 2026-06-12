# Mutual Fund Analytics Capstone Project

## Project Overview

The Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, and portfolio risk metrics. The project integrates data ingestion, data cleaning, ETL processing, exploratory data analysis, advanced analytics, and dashboard visualization to generate meaningful investment insights.

The project uses Python for data processing and analytics, SQLite for data storage, SQL for querying, Jupyter Notebooks for analysis, and Power BI for interactive dashboard development.

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/Nishasrini/Bluestock_mf_capstone.git
cd <repository-name>
```

### Install Dependencies

```bash
pip install -r requirements.txt

---

## Project Structure

```text
BLUESTOCK_MF_CAPSTONE/

├── dashboard/
│   └── bluestock_mf_dashboard.pbix

├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db

├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb

├── reports/
│   └── data_quality_report.txt

├── scripts/
│   ├── data_ingestion.py
│   ├── etl_pipeline.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   ├── recommender.py
│   └── run_pipeline.py

├── sql/
│   ├── schema.sql
│   └── queries.sql

├── data_dictionary.md
├── requirements.txt
└── README.md
```

---

## File Descriptions

### Dashboard

- **bluestock_mf_dashboard.pbix** – Interactive Power BI dashboard for mutual fund analytics and visualization.

### Data

- **raw/** – Original source datasets.
- **processed/** – Cleaned datasets and analytics outputs.
- **bluestock_mf.db** – SQLite database containing project data.

### Notebooks

- **01_data_ingestion.ipynb** – Data collection and loading.
- **02_data_cleaning.ipynb** – Data preprocessing and cleaning.
- **03_eda_analysis.ipynb** – Exploratory Data Analysis.
- **04_performance_analytics.ipynb** – Fund performance metrics.
- **05_advanced_analytics.ipynb** – Risk metrics and advanced analytics.

### Scripts

- **data_ingestion.py** – Loads raw datasets into the project.
- **etl_pipeline.py** – Performs extraction, transformation, and loading operations.
- **compute_metrics.py** – Computes fund performance and risk metrics.
- **live_nav_fetch.py** – Retrieves NAV data.
- **recommender.py** – Fund recommendation system.
- **run_pipeline.py** – Executes the complete project workflow.

### SQL

- **schema.sql** – Database schema creation scripts.
- **queries.sql** – Analytical SQL queries.

### Reports

- **data_quality_report.txt** – Data quality validation report.

---

## How to Run ETL Pipeline

Navigate to the scripts folder and execute:

```bash
cd scripts
python run_pipeline.py
```

The ETL pipeline performs:

1. Data Ingestion
2. Data Cleaning
3. Database Loading
4. Metric Computation
5. Risk Analysis
6. Output Generation

Processed datasets are saved in the `data/processed/` folder.

---

## How to Open Dashboard

1. Open Power BI Desktop.
2. Select **Open Report**.
3. Navigate to:

```text
dashboard/bluestock_mf_dashboard.pbix
```

4. Open the report.
5. Refresh data if required.

---

## Key Analytics Implemented

- Exploratory Data Analysis (EDA)
- Fund Performance Analysis
- CAGR Calculation
- Alpha and Beta Metrics
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector Concentration Risk (HHI)
- Fund Recommendation System

---

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQL
- Jupyter Notebook
- Power BI
- Matplotlib

---
