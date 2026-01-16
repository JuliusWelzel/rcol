# Step 5: Upload Instruments

This guide explains how to upload `rcol` instrument templates to your REDCap project using PyCap.

## Prerequisites

- [x] REDCap project with API access ([Steps 1-3](index.md))
- [x] Python environment set up ([Step 4](python-setup.md))

## Basic Upload

### 1. Store Your API Key

You need your REDCap API key available locally as `RC_API_KEY`.

**Recommended: `.env` file (works well with the tutorials)**

```ini title=".env"
RC_API_KEY=YOUR_API_TOKEN_HERE
```

**Alternative: Environment variable**

=== "Windows (PowerShell)"

    ```powershell
    $env:RC_API_KEY = "YOUR_API_TOKEN_HERE"
    ```

=== "Windows (Command Prompt)"

    ```cmd
    set RC_API_KEY=YOUR_API_TOKEN_HERE
    ```

=== "Linux/macOS"

    ```bash
    export RC_API_KEY="YOUR_API_TOKEN_HERE"
    ```

!!! warning "Security"
    Never commit `.env` files or API keys to version control.

    Add this to your `.gitignore`:
    ```text
    # Secrets
    .env
    ```

### 2. Create the Upload Script

Create a new Python file:

```python title="upload_instruments.py"
from dotenv import load_dotenv
import os
import pandas as pd
from redcap import Project, RedcapError

# Import instruments from rcol
from rcol.instruments import fal, ehi, bdi_ii

# Load API key from .env file
load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")

# Combine instruments into one DataFrame
instruments = pd.concat([fal, ehi, bdi_ii], ignore_index=True)
print(f"📋 Preparing to upload {len(instruments)} fields...")

# Initialize REDCap project connection
api_url = "https://redcapdev.uol.de/api/"
rc_project = Project(api_url, RC_API_KEY)

# Upload instruments to REDCap
try:
    response = rc_project.import_metadata(instruments, import_format="df")
    print(f"✅ Successfully uploaded {response} fields to REDCap")
except RedcapError as e:
    print(f"❌ Error uploading to REDCap: {e}")
```

### 3. Run the Script

=== "Using uv"

    ```bash
    uv run python upload_instruments.py
    ```

=== "Using pip/venv"

    ```bash
    python upload_instruments.py
    ```

Expected output:

```
📋 Preparing to upload 45 fields...
✅ Successfully uploaded 45 fields to REDCap
```

### 4. Verify in REDCap

1. Log in to REDCap
2. Open your project
3. Go to **Online Designer**
4. You should see your uploaded instruments

## Upload Selected Instruments

To upload specific instruments:

```python title="upload_selected.py"
from dotenv import load_dotenv
import os
import pandas as pd
from redcap import Project, RedcapError
from rcol.rtg import (
    study_participant_information,
    becks_depression_inventory_ii,
    sf12,
    moca,
)

load_dotenv()
RC_API_KEY = os.getenv("RC_API_KEY")

# Combine selected instruments
instruments = pd.concat([
    study_participant_information,
    becks_depression_inventory_ii,
    sf12,
    moca,
], ignore_index=True)

print(f"📋 Uploading {len(instruments)} fields...")

# Upload
api_url = "https://redcapdev.uol.de/api/"
rc_project = Project(api_url, RC_API_KEY)

try:
    response = rc_project.import_metadata(instruments, import_format="df")
    print(f"✅ Successfully uploaded {response} fields")
except RedcapError as e:
    print(f"❌ Error: {e}")
```

## Handling Existing Instruments

!!! warning "Important"
    Uploading instruments **overwrites** existing metadata. Back up your project first!

### Backup Before Upload

```python
from redcap import Project

rc_project = Project("https://redcapdev.uol.de/api/", RC_API_KEY)

# Export current metadata as backup
metadata = rc_project.export_metadata(format_type="df")
metadata.to_csv("metadata_backup.csv", index=False)
print(f"✅ Backup saved: {len(metadata)} fields")
```

### Export and Review

```python
# View current project structure
metadata = rc_project.export_metadata(format_type="df")
print("Current instruments:")
print(metadata["form_name"].unique())
```

## What's Next?

After uploading your instruments, enable them as surveys:

**[→ Step 6: Enable Survey Mode](survey-mode.md)**

## Troubleshooting

??? question "Error: 'The field_name column contains duplicate values'"
    - Check that you're not uploading duplicate instruments
    - Each field_name must be unique across all instruments
    - Use the validation function above to identify duplicates

??? question "Error: 'You do not have API Import/Update privileges'"
    - Contact your REDCap administrator
    - Request Import/Update permissions for your API token

??? question "Only some fields were uploaded"
    - Check the response message for the actual count
    - Verify field_type values are valid REDCap types
    - Look for special characters in field_label or choices
