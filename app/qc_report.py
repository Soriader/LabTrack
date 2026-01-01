from pathlib import Path
import pandas as pd
from app.qc_utils import load_results_csv, merge_with_spec, add_in_spec, oos_report
from app.specs import load_spec_csv

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

    print("Saved:")
    print("-", out_dir / "qc_results.csv")
    print("-", out_dir / "oos_by_product.csv")
    print("-", out_dir / "oos_by_parameter.csv")


if __name__ == "__main__":
    main()
