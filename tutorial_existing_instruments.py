"""Tutorial: Using Existing Instruments from rcol

This tutorial demonstrates how to:
1. Import and use existing instruments from the rcol package
2. Access instruments from the rtg (Research Template Gallery) module
3. Combine multiple instruments
4. Upload to REDCap

Prerequisites:
- Install rcol: pip install rcol
- Install python-dotenv: pip install python-dotenv
- Install PyCap: pip install PyCap
- Set up a .env file with your RC_API_KEY

Usage:
    python tutorial_existing_instruments.py
"""

from dotenv import load_dotenv
import pandas as pd
from redcap import Project, RedcapError
import os

# Import instruments from the installed rcol package
from rcol.instruments import fal, ehi, bdi_ii
import rcol.rtg as rtg

load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")

# ============================================================================
# 1. Using Individual Instruments
# ============================================================================
print("Individual instruments from rcol.instruments:")
print(f"  - FAL: {len(fal)} fields")
print(f"  - EHI: {len(ehi)} fields")
print(f"  - BDI-II: {len(bdi_ii)} fields")
print()

# ============================================================================
# 2. Discovering RTG (Research Template Gallery) Instruments
# ============================================================================
# List all instruments from rtg (exclude built-in functions and modules)
rtg_instruments = [
    attr for attr in dir(rtg) 
    if not attr.startswith("_") 
    and isinstance(getattr(rtg, attr), pd.DataFrame)
    and not callable(getattr(rtg, attr))
    and attr != "pd"  # exclude pandas import
]
print("RTG (Research Template Gallery) Instruments:")
print(rtg_instruments)
print()

# ============================================================================
# 3. Combining RTG Instruments
# ============================================================================
# Loop over all instrument names from rtg and concatenate them
rtg_dfs = []
for instrument_name in rtg_instruments:
    instrument_df = getattr(rtg, instrument_name)
    rtg_dfs.append(instrument_df)
    print(f"  - {instrument_name}: {instrument_df.shape[0]} rows")

# Combine all RTG instruments into one big DataFrame
if rtg_dfs:
    all_rtg_instruments = pd.concat(rtg_dfs, ignore_index=True)
    print(f"Total RTG instruments DataFrame: {all_rtg_instruments.shape[0]} rows")
else:
    print("No RTG instruments found")
    all_rtg_instruments = None
print()


# ============================================================================
# 4. Uploading to REDCap
# ============================================================================
# Initialize the REDCap project
if all_rtg_instruments is not None:
    api_url = 'https://redcapdev.uol.de/api/'
    rc_project = Project(api_url, RC_API_KEY)

    # Upload instruments to REDCap using the import_metadata method
    # Note: This will replace/update the project metadata
    try:
        response = rc_project.import_metadata(all_rtg_instruments, import_format='df')
        print(f"✓ Successfully uploaded {response} fields to REDCap")
    except RedcapError as e:
        print(f"✗ Error uploading to REDCap: {e}")
        print("  Make sure RC_API_KEY is set in your .env file and the API URL is correct")
else:
    print("Skipping REDCap upload (no instruments to upload)")
