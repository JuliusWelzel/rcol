import pandas as pd
from .instruments import fal_data, ehi_data
from typing import Dict

def get_instrument_template(name: str) -> pd.DataFrame:
    meta = {
        "fal": fal_data,
        "ehi": ehi_data,
    }
    if name not in meta:
        raise ValueError(f"Unknown instrument: {name}")
    # Extract field names for participant data entry
    field_names = [f["field_name"] for f in meta[name]]
    return pd.DataFrame(columns=field_names)
