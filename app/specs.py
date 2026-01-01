from pathlib import Path
import pandas as pd

def load_spec_csv(path: str | None = None) -> pd.DataFrame:

    if path is None:
        path = Path(__file__).resolve().parent / "spec.csv"

    spec = pd.read_csv(path)

    spec["min_spec"] = pd.to_numeric(spec["min_spec"], errors="coerce")
    spec["max_spec"] = pd.to_numeric(spec["max_spec"], errors="coerce")

    return spec


def get_default_spec() -> pd.DataFrame:

    return pd.DataFrame({
        "parameter": ["pH", "Density", "Acidity", "Viscosity"],
        "min_spec": [6.00, 0.90, 0.00, 0.00],
        "max_spec": [6.60, 1.03, 0.45, 9000],
        "unit_spec": ["-", "g/cm3", "mg KOH/g", "mPa·s"],
    })