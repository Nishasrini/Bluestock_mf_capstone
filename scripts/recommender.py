import pandas as pd
def recommend_funds(risk_appetite, fund_file):
    df = pd.read_csv(fund_file)
    df["risk_grade"] = df["risk_grade"].str.strip().str.title()
    risk_appetite = risk_appetite.strip().title()
    filtered = df[df["risk_grade"] == risk_appetite]
    if filtered.empty:
        print(f"No funds found for risk appetite: {risk_appetite}")
        return None
    recommendations = (
        filtered.sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)[
            [
                "scheme_name",
                "fund_house",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "expense_ratio_pct",
                "morningstar_rating"
            ]
        ]
    )
    return recommendations
if __name__ == "__main__":
    risk = input(
        "Enter Risk Appetite (Low / Moderate / High): "
    )
    result = recommend_funds(
        risk,
        "data/processed/clean_performance.csv"
    )
    if result is not None:
        print("\nTop 3 Recommended Funds\n")
        print(result.to_string(index=False))