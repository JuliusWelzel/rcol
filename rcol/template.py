# This module is deprecated. Please use the installed package 'redcap_templates' instead.

import pandas as pd
from typing import List, Dict

class RedcapInstrumentTemplate:
    """
    Base class for REDCap instrument DataFrame templates.
    """
    def __init__(self, fields: List[str], instrument_name: str):
        self.fields = fields
        self.instrument_name = instrument_name

    def create_template(self, n_rows: int = 1) -> pd.DataFrame:
        """
        Create a DataFrame template for the instrument.
        """
        df = pd.DataFrame(columns=self.fields)
        return df.reindex(range(n_rows))

    @staticmethod
    def stack_templates(templates: List[pd.DataFrame]) -> pd.DataFrame:
        """
        Stack multiple instrument DataFrames vertically.
        """
        return pd.concat(templates, ignore_index=True)

    def to_redcap_format(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Prepare DataFrame for REDCap upload (override as needed).
        """
        # Placeholder: implement REDCap-specific formatting if needed
        return df

    def upload_to_redcap(self, df: pd.DataFrame, api_url: str, api_token: str) -> Dict:
        """
        Upload DataFrame to REDCap project via API.
        """
        import requests
        data = df.to_dict(orient="records")
        payload = {
            'token': api_token,
            'content': 'record',
            'format': 'json',
            'type': 'flat',
            'data': pd.io.json.dumps(data)
        }
        response = requests.post(api_url, data=payload)
        response.raise_for_status()
        return response.json()
