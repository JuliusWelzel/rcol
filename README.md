# rcol
rcol (RedCap Uni Oldenburg) is a Python package that provides Pandas DataFrame templates for REDCap instruments with stacking and upload functionality.

## Installation

```bash
pip install rcol
```

## Quick Start

```python
from rcol.instruments import fal, ehi, bdi_ii
import pandas as pd

# Use individual instruments
print(f"FAL has {len(fal)} fields")
print(f"EHI has {len(ehi)} fields") 
print(f"BDI-II has {len(bdi_ii)} fields")

# Stack multiple instruments for REDCap upload
all_instruments = pd.concat([fal, ehi, bdi_ii], ignore_index=True)
print(f"Combined: {len(all_instruments)} total fields")

# Upload to REDCap (requires PyCap and API credentials)
from redcap import Project
project = Project(api_url, api_token)
project.import_metadata(all_instruments, import_format='df')
```

## Available Instruments

- `fal`: Fragebogen zur Allgemeinen Leistungsfähigkeit (General Performance Questionnaire)
- `ehi`: Edinburgh Handedness Inventory 
- `bdi_ii`: Beck Depression Inventory II
- `moca`: Montreal Cognitive Assessment (Version A)

## Contributing a New Instrument

1. **Fork this repository**

2. **Add your instrument data** in `src/rcol/instruments.py`:
   ```python
   # Define your instrument fields
   my_instrument_data = [
       {
           "field_name": "record_id",
           "form_name": "my_instrument", 
           "field_type": "text",
           "field_label": "Record ID",
           # ... other REDCap metadata fields
       },
       # ... more fields
   ]
   
   # Create DataFrame
   my_instrument = pd.DataFrame(my_instrument_data)
   ```

3. **Add a test** in `tests/test_templates.py`:
   ```python
   def test_my_instrument():
       assert "record_id" in my_instrument.columns
       assert "my_field" in my_instrument.columns
   ```

4. **Submit a pull request** with your instrument and test

## Development

```bash
# Clone and install for development
git clone https://github.com/JuliusWelzel/rcol.git
cd rcol
uv sync

# Run tests
uv run pytest

# Build package
uv build
```

## License

MIT
