# rcol

[![CI](https://github.com/JuliusWelzel/rcol/actions/workflows/ci.yml/badge.svg)](https://github.com/JuliusWelzel/rcol/actions/workflows/ci.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/rcol.svg)](https://badge.fury.io/py/rcol)

rcol (RedCap Uni Oldenburg) is a Python package that provides Pandas DataFrame templates for REDCap instruments with stacking and upload functionality.

**Tested on:** Windows, Linux, macOS | **Python:** 3.8, 3.9, 3.10, 3.11, 3.12, 3.13

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
- `moca`: Montreal Cognitive Assessment
- `tmt`: Trail Making Test
- `wnss`: Weinstein's Noise Sensitivity Scale (WNSS-21)


## Creating Custom Instruments

You can create custom instruments or extend existing ones without contributing to the package:

```python
import pandas as pd
from rcol.instruments import fal, ehi
from redcap import Project

# Create a custom instrument from scratch
custom_instrument = pd.DataFrame({
    'field_name': ['record_id', 'custom_field_1', 'custom_field_2'],
    'field_label': ['Record ID', 'Custom Field 1', 'Custom Field 2'],
    'field_type': ['text', 'text', 'radio'],
    'form_name': ['custom_form', 'custom_form', 'custom_form'],
    'choices': ['', '', '1, Yes | 0, No']
})

# Add a new question to an existing instrument
fal_new_question = pd.DataFrame({
    'field_name': ['fal_like_redcap'],
    'field_label': ['Do you like REDCap?'],
    'field_type': ['radio'],
    'form_name': ['fal'],
    'choices': ['1, Yes | 0, No']
})

fal_extended = pd.concat([fal, fal_new_question], ignore_index=True)

# Combine everything and upload to REDCap
all_instruments = pd.concat([fal_extended, ehi, custom_instrument], ignore_index=True)

project = Project(api_url, api_token)
project.import_metadata(all_instruments, import_format='df')
```

**See `tutorial_custom_instruments.py` for a complete guide with all REDCap metadata fields.**

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

3. **Run the instrument test suite** to validate your template. The shared tests automatically pick up every `pandas.DataFrame` exported from `rcol.instruments` and check for required REDCap metadata, non-empty field names, and duplicate protection:

    ```bash
    uv run --with pytest pytest -k instrument
    ```

    If you add custom validation that needs extra assertions, extend `tests/test_templates.py` accordingly.

4. **Preview the documentation (optional).** The MkDocs site renders the instrument tables directly from `rcol.instruments`. To check the output locally:

    ```bash
    uv run --group docs mkdocs serve
    ```

5. **Submit a pull request.** Every PR triggers the GitHub Actions CI workflow, which runs the instrument tests across Windows, Linux, and macOS with Python 3.8-3.13. Make sure the workflow badge stays green before requesting review.

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

## Documentation

The documentation site is powered by MkDocs and `mkdocstrings`, so instrumentation
tables are rendered directly from `rcol.instruments` at build time.

```bash
# Serve docs locally
uv run --group docs mkdocs serve

# Build static site
uv run --group docs mkdocs build
```

## License

MIT
