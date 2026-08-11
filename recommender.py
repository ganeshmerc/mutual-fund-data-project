
import pandas as pd

# Load performance data
performance = pd.read_csv(
    r"E:\mutual-fund-data-project\Data\Processed\07_scheme_performance_cleaned.csv"
)

def recommend_funds(risk_appetite):
    """
    Recommend top 3 mutual funds based on Sharpe ratio
    within the selected risk grade.

    Risk appetite: Low / Moderate / High
    """

    risk_appetite = risk_appetite.strip().title()

    valid_risks = ["Low", "Moderate", "High"]

    if risk_appetite not in valid_risks:
        print("Invalid risk appetite.")
        print("Choose: Low, Moderate, or High")
        return pd.DataFrame()

    recommendations = (
        performance[
            performance["risk_grade"].str.strip().str.title()
            == risk_appetite
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
        [
            [
                "amfi_code",
                "scheme_name",
                "risk_grade",
                "sharpe_ratio"
            ]
        ]
        .copy()
    )

    print(f"\nTop 3 Funds for {risk_appetite} Risk Appetite")
    print("=" * 60)

    if recommendations.empty:
        print("No funds found for this risk grade.")
        return recommendations

    print(recommendations.to_string(index=False))

    return recommendations


if __name__ == "__main__":
    risk = input(
        "Enter risk appetite (Low / Moderate / High): "
    )

    recommend_funds(risk)
