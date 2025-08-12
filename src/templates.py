import pandas as pd
from .instruments import fal, ehi


def get_instrument(name: str) -> pd.DataFrame:
    meta = {
        "fal": fal,
        "ehi": ehi,
    }
    if name not in meta:
        raise ValueError(f"Unknown instrument: {name}")
    # Extract field names for participant data entry
    field_names = [f["field_name"] for f in meta[name]]
    return pd.DataFrame(columns=field_names)
