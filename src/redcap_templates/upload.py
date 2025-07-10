import pandas as pd
import redcap

def upload_to_redcap(df: pd.DataFrame, api_url: str, api_token: str) -> dict:
    """Upload a DataFrame to a REDCap project using PyCap."""
    project = redcap.Project(api_url, api_token)
    # Convert DataFrame to list of dicts for PyCap
    records = df.to_dict(orient="records")
    response = project.import_records(records)
    return response
