# rcol Documentation

Welcome to the documentation for **rcol (RedCap Uni Oldenburg)**. This site provides an overview of the package, quick-start guidance, and automatically generated reference pages for every REDCap instrument template bundled in the library.

## Overview

rcol ships Pandas `DataFrame` templates for common REDCap instruments and convenience utilities for stacking and uploading them to a REDCap project. The templates follow the REDCap metadata export format so they can be uploaded without manual formatting.

## Installation

```bash
uv add rcol
```

Or, when working inside the repository:

```bash
uv sync
```

## Quick Start

```python
from rcol.instruments import fal, ehi, bdi_ii
import pandas as pd

print(f"FAL has {len(fal)} fields")
print(f"EHI has {len(ehi)} fields")
print(f"BDI-II has {len(bdi_ii)} fields")

all_instruments = pd.concat([fal, ehi, bdi_ii], ignore_index=True)
```

## Instrument Reference

The **Instrument Reference** section in the navigation is generated directly from the REDCap templates distributed with the library. Each page lists all metadata columns and values so you can review field names, branching logic, validation, and choice lists at a glance.
