# Instrument Reference

This section contains all REDCap instrument templates bundled with `rcol`. Each template is a `pandas.DataFrame` that follows the REDCap metadata export format and can be uploaded directly to your REDCap project.

## Categories

| Category | Description | Link |
|----------|-------------|------|
| **General Instruments** | Standard questionnaires and assessments commonly used in research studies | [View instruments](general.md) |
| **RTG Instruments** | Specialized instruments from the Research Training Group (RTG) study | [View instruments](rtg.md) |

## Quick Usage

```python
# Import general instruments
from rcol.instruments import fal, ehi, bdi_ii

# Import RTG instruments
from rcol.rtg import study_participant_information, sf12

# Combine multiple instruments
import pandas as pd
combined = pd.concat([fal, ehi], ignore_index=True)
```

## DataFrame Structure

Each instrument DataFrame contains the following columns (REDCap metadata format):

| Column | Description |
|--------|-------------|
| `field_name` | Unique identifier for the field |
| `form_name` | Name of the instrument/form |
| `section_header` | Section header text (if any) |
| `field_type` | Type of field (text, radio, dropdown, etc.) |
| `field_label` | Question text shown to participants |
| `choices` | Answer choices for radio/dropdown fields |
| `field_note` | Additional notes shown below the field |
| `text_validation_type_or_show_slider_number` | Validation type |
| `text_validation_min` | Minimum value for validation |
| `text_validation_max` | Maximum value for validation |
| `branching_logic` | Conditional display logic |
| `required_field` | Whether the field is required |
