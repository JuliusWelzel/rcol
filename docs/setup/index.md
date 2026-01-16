# REDCap Setup Guide

This guide walks you through setting up REDCap at the University of Oldenburg and using `rcol` to manage your instruments.

## Overview

Setting up a REDCap project involves these steps:

| Step | Description | Link |
|:----:|-------------|------|
| **1** | **Get an Account** — Register for a REDCap account at the University of Oldenburg | [Registration Guide](account.md) |
| **2** | **Create a Project** — Request a new REDCap project from your administrator | [Project Setup](project.md) |
| **3** | **Get API Access** — Request API credentials to enable programmatic access | [API Setup](api-key.md) |
| **4** | **Setup Python** — Install Python and the required packages | [Python Setup](python-setup.md) |
| **5** | **Upload Instruments** — Use rcol to upload instrument templates to your project | [Upload Guide](upload-instruments.md) |
| **6** | **Enable Surveys** — Configure your instruments as participant surveys | [Survey Mode](survey-mode.md) |

## Quick Start

If you already have a REDCap account with API access, you can quickly upload instruments:

```python
from dotenv import load_dotenv
import os
import pandas as pd
from redcap import Project
from rcol.instruments import fal, ehi

# Load API key from .env file
load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")

# Combine instruments
instruments = pd.concat([fal, ehi], ignore_index=True)

# Upload to REDCap
rc_project = Project("https://redcapdev.uol.de/api/", RC_API_KEY)
response = rc_project.import_metadata(instruments, import_format="df")
print(f"✅ Uploaded {response} fields")
```

## Need Help?

If you encounter issues during setup:

1. Check the [Troubleshooting](troubleshooting.md) page
2. Contact the REDCap administrator at your institution
3. Open an issue on the [rcol GitHub repository](https://github.com/your-org/rcol)
