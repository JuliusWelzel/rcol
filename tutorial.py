"""
Tutorial: Using the rcol package for REDCap instrument metadata design and upload
Adapted from https://github.com/JuliusWelzel/redcap2bids/blob/master/scripts/instrument2redcap.py
"""
import pandas as pd
from redcap import Project
from redcap_templates import get_instrument_template

# 1. Get instrument templates (e.g., 'fal')
fal = get_instrument_template("fal")
ehi = get_instrument_template("ehi")  # Add more as needed

# 2. Stack all instrument metadata DataFrames
all_instruments = pd.concat([fal,ehi], ignore_index=True)  # Add more: [fal, ehi, ...]

print("All instrument metadata:")
print(all_instruments.head())

# 3. Upload instrument metadata to REDCap project via API (admin only)
api_url = "https://your-redcap-server/api/"
api_key = "YOUR_API_TOKEN"
rc_project = Project(api_url, api_key)
rc_project.import_metadata(all_instruments, import_format='df')
print("Instrument metadata uploaded to REDCap.")

print("\nTutorial complete. This script is for instrument metadata design and REDCap API upload. No participant data is uploaded.")
