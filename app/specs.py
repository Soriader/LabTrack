import pandas as pd


def get_default_spec() -> pd.DataFrame:

    return pd.DataFrame({
        "parameter": ["pH", "Density", "Acidity", "Viscosity"],
        "min_spec": [6.00, 0.90, 0.00, 0.00],
        "max_spec": [6.60, 1.03, 0.45, 9000],
        "unit_spec": ["-", "g/cm3", "mg KOH/g", "mPa·s"],
    })