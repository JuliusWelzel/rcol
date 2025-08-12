"""
Tutorial: Using the rcol package for REDCap instrument metadata design and upload
"""
import pandas as pd
from rcol import get_instrument_template

# 1. Get instrument templates (e.g., 'fal', 'ehi')
fal = get_instrument_template("fal")
ehi = get_instrument_template("ehi")

# 2. Stack all instrument DataFrames (for demonstration)
all_instruments = pd.concat([fal, ehi], ignore_index=True)

print("All instrument data entry templates:")
print(all_instruments.head())

print("\nTutorial complete. This script is for instrument data entry template design. No participant data is uploaded.")
