from dotenv import load_dotenv
import pandas as pd
from redcap import Project
import os
from src.rcol.instruments import fal, ehi, bdi_ii

import src.rcol.rtg as rtg

load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")

# list all instruments from rtg (exclude built-in functions and modules)
rtg_instruments = [
    attr for attr in dir(rtg) 
    if not attr.startswith("_") 
    and isinstance(getattr(rtg, attr), pd.DataFrame)
    and not callable(getattr(rtg, attr))
    and attr != "pd"  # exclude pandas import
]
print("RTG Instruments:")
print(rtg_instruments)

# loop over all instrument names from rtg and concatenate them
rtg_dfs = []
for instrument_name in rtg_instruments:
    instrument_df = getattr(rtg, instrument_name)
    rtg_dfs.append(instrument_df)
    print(f"  - {instrument_name}: {instrument_df.shape[0]} rows")

# Combine all RTG instruments into one big DataFrame
all_rtg_instruments = pd.concat(rtg_dfs, ignore_index=True)
print(f"\nTotal RTG instruments DataFrame: {all_rtg_instruments.shape[0]} rows")


# initalize the redcap project
api_url = 'https://redcapdev.uol.de/api/'
rc_project = Project(api_url, RC_API_KEY)

# upload instruments to RedCap using the import_metadata method
rc_project.import_metadata(all_rtg_instruments, import_format='df')
