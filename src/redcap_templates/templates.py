import pandas as pd
from .instruments import fal
from typing import Dict

def get_instrument_template(name: str) -> pd.DataFrame:
    """Return a pandas DataFrame template for a given REDCap instrument name."""
    templates: Dict[str, pd.DataFrame] = {
        "fal": fal,
    }
    if name not in templates:
        raise ValueError(f"Unknown instrument: {name}")
    return templates[name].copy()
