# rcol Documentation

Welcome to **rcol** (REDCap Uni Oldenburg) — a Python package providing pandas DataFrame templates for common REDCap instruments.

## Features

- ✅ **Pre-built instrument templates** — Ready-to-use REDCap metadata DataFrames
- ✅ **REDCap-compatible format** — Upload directly via API without manual formatting
- ✅ **Easy to combine** — Stack multiple instruments with pandas
- ✅ **Validated** — Tested for REDCap compatibility

## Getting Started (Recommended)

If you’re new to REDCap at Uni Oldenburg, start here:

**[→ Getting Started](getting-started.md)**

## Quick Start

### Installation

```bash
uv add rcol
```

### Basic Usage

```python
from dotenv import load_dotenv
import os
import pandas as pd
from redcap import Project
from rcol.instruments import fal, ehi, bdi_ii

# Load API key from .env file
load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")

# View a single instrument
print(fal)

# Combine multiple instruments
combined = pd.concat([fal, ehi, bdi_ii], ignore_index=True)

# Upload to REDCap
rc_project = Project("https://redcapdev.uol.de/api/", RC_API_KEY)
response = rc_project.import_metadata(combined, import_format="df")
print(f"Uploaded {response} fields")
```

## Available Instruments

### General Instruments

| Instrument | Description |
|------------|-------------|
| `fal` | Fragebogen zur Allgemeinen Leistungsfähigkeit |
| `ehi` | Edinburgh Handedness Inventory |
| `bdi_ii` | Beck Depression Inventory II |
| `moca` | Montreal Cognitive Assessment |
| `tmt` | Trail Making Test |
| `wnss` | Weinstein's Noise Sensitivity Scale |

### RTG Instruments

Specialized instruments from the Research Training Group study:

| Instrument | Description |
|------------|-------------|
| `study_participant_information` | Basic demographic information |
| `becks_depression_inventory_ii` | Depression screening |
| `sf12` | SF-12 Health Survey |
| `moca` | Montreal Cognitive Assessment (RTG version) |
| And many more... | [View all RTG instruments](instruments/rtg.md) |


## Next Steps

- [View all instruments](instruments/index.md) — Browse available templates
- [Setup Guide](setup/index.md) — Complete REDCap setup walkthrough
- [Upload Instruments](setup/upload-instruments.md) — Upload to your project
