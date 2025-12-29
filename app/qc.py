import pandas as pd


REQUIRED_RESULTS_COLS = {"product", "parameter", "value"}
REQUIRED_SPEC_COLS = {"parameter", "min_spec", "max_spec"}


def validate_inputs(results: pd.DataFrame, spec: pd.DataFrame) -> None:
    missing_r = REQUIRED_RESULTS_COLS - set(results.columns)
    missing_s = REQUIRED_SPEC_COLS - set(spec.columns)

    if missing_r:
        raise ValueError(f"Results is missing columns: {sorted(missing_r)}")
    if missing_s:
        raise ValueError(f"Spec is missing columns: {sorted(missing_s)}")


def merge_with_spec(results: pd.DataFrame, spec: pd.DataFrame) -> pd.DataFrame:

    validate_inputs(results, spec)
    return results.merge(spec, on="parameter", how="left")


def add_in_spec(df_merged: pd.DataFrame) -> pd.DataFrame:

    df = df_merged.copy()

    has_spec = df["min_spec"].notna() & df["max_spec"].notna()

    in_spec = (df["value"] >= df["min_spec"]) & (df["value"] <= df["max_spec"])
    df["in_spec"] = has_spec & in_spec
    df["OOS"] = ~df["in_spec"]

    return df


def oos_report(df: pd.DataFrame, group_col: str) -> pd.DataFrame:

    if group_col not in df.columns:
        raise ValueError(f"Column '{group_col}' not found in dataframe")

    rep = (
        df.groupby(group_col)["OOS"]
          .agg(total_tests="count", oos_count="sum")
          .reset_index()
    )
    rep["oos_percent"] = (rep["oos_count"] / rep["total_tests"] * 100).round(1)
    return rep
