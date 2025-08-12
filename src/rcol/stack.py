import pandas as pd
from typing import List

def stack_instruments(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(dfs, ignore_index=True)
