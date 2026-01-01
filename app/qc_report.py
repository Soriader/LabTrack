from pathlib import Path
import pandas as pd
from app.qc_utils import load_results_csv, merge_with_spec, add_in_spec, oos_report
from app.specs import load_spec_csv
import matplotlib.pyplot as plt

def save_oos_bar_chart(df_report: pd.DataFrame, category_col: str, out_path: Path, title: str) -> None:

    plt.figure(figsize=(7, 4))
    plt.bar(df_report[category_col], df_report["oos_percent"])
    plt.title(title)
    plt.xlabel(category_col.capitalize())
    plt.ylabel("OOS [%]")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


def main():
    base_dir = Path(__file__).resolve().parent  # .../app
    results_path = base_dir / "result.csv"
    out_dir = base_dir / "reports"
    out_dir.mkdir(exist_ok=True)

    results = load_results_csv(str(results_path))
    spec = load_spec_csv()

    df_merged = merge_with_spec(results, spec)
    df_qc = add_in_spec(df_merged)

    oos_by_product = oos_report(df_qc, "product")
    oos_by_parameter = oos_report(df_qc, "parameter")

    df_qc.to_csv(out_dir / "qc_results.csv", index=False)
    oos_by_product.to_csv(out_dir / "oos_by_product.csv", index=False)
    oos_by_parameter.to_csv(out_dir / "oos_by_parameter.csv", index=False)

    save_oos_bar_chart(
        oos_by_product,
        category_col="product",
        out_path=out_dir / "oos_by_product.png",
        title="OOS percentage per product",
    )

    save_oos_bar_chart(
        oos_by_parameter,
        category_col="parameter",
        out_path=out_dir / "oos_by_parameter.png",
        title="OOS percentage per parameter",
    )

    print("-", out_dir / "oos_by_product.png")
    print("-", out_dir / "oos_by_parameter.png")

    print("Saved:")
    print("-", out_dir / "qc_results.csv")
    print("-", out_dir / "oos_by_product.csv")
    print("-", out_dir / "oos_by_parameter.csv")


if __name__ == "__main__":
    main()
