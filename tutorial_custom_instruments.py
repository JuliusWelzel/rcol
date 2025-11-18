"""Tutorial: Creating and Using Custom Instruments with rcol

This tutorial demonstrates how to:
1. Create custom instruments from scratch
2. Modify existing instruments by adding fields
3. Combine built-in and custom instruments
4. Upload everything to REDCap
"""

import os
import pandas as pd
from rcol.instruments import fal, ehi, moca
from redcap import Project

# Get REDCap API credentials from environment
api_key = os.getenv("REDCAP_API_KEY")
api_url = "https://redcapdev.uol.de/api/"  # Replace with your actual REDCap API URL

# ============================================================================
# 1. Using Built-in Instruments
# ============================================================================
print("Built-in instruments:")
print(f"FAL has {len(fal)} fields")
print(f"EHI has {len(ehi)} fields")
print(f"MoCA has {len(moca)} fields")
print()

# ============================================================================
# 2. Creating a Custom Instrument from Scratch
# ============================================================================
custom_instrument = pd.DataFrame({
    'field_name': ['record_id', 'custom_field_1', 'custom_field_2', 'custom_field_3'],
    'field_label': ['Record ID', 'Custom Field 1', 'Custom Field 2', 'Custom Field 3'],
    'field_type': ['text', 'text', 'radio', 'dropdown'],
    'choices': ['', '', '1, Yes | 0, No', 'A, Choice A | B, Choice B | C, Choice C'],
    'form_name': ['custom_form', 'custom_form', 'custom_form', 'custom_form'],
    'section_header': ['', 'Basic Information', '', 'Additional Options'],
    'field_note': ['', 'Enter text here', 'Select one option', 'Choose from dropdown'],
    'text_validation_type_or_show_slider_number': ['', '', '', ''],
    'text_validation_min': ['', '', '', ''],
    'text_validation_max': ['', '', '', ''],
    'identifier': ['', '', '', ''],
    'branching_logic': ['', '', '', ''],
    'required_field': ['', '', '', ''],
    'custom_alignment': ['', '', '', ''],
    'question_number': ['', '', '', ''],
    'matrix_group_name': ['', '', '', ''],
    'matrix_ranking': ['', '', '', ''],
    'field_annotation': ['', '', '', '']
})

print(f"Created custom instrument with {len(custom_instrument)} fields")
print()

# ============================================================================
# 3. Adding Questions to Existing Instruments
# ============================================================================
# Add a new question to FAL instrument
fal_new_question = pd.DataFrame({
    'field_name': ['fal_like_redcap'],
    'field_label': ['Do you like REDCap?'],
    'field_type': ['radio'],
    'form_name': ['fal'],
    'choices': ['1, Yes | 0, No'],
    'section_header': ['Feedback'],
    'field_note': ['Please provide your feedback'],
    'text_validation_type_or_show_slider_number': [''],
    'text_validation_min': [''],
    'text_validation_max': [''],
    'identifier': [''],
    'branching_logic': [''],
    'required_field': ['y'],
    'custom_alignment': [''],
    'question_number': [''],
    'matrix_group_name': [''],
    'matrix_ranking': [''],
    'field_annotation': ['']
})

# Concatenate new question to FAL
fal_extended = pd.concat([fal, fal_new_question], ignore_index=True)
print(f"Extended FAL from {len(fal)} to {len(fal_extended)} fields")
print()

# ============================================================================
# 4. Combining Multiple Instruments for Upload
# ============================================================================
# Stack all instruments together
all_instruments = pd.concat([
    fal_extended,
    ehi,
    moca,
    custom_instrument
], ignore_index=True)

print(f"Combined all instruments: {len(all_instruments)} total fields")
print(f"Forms included: {all_instruments['form_name'].unique().tolist()}")
print()

# ============================================================================
# 5. Uploading to REDCap
# ============================================================================
# Initialize REDCap project connection
RC_API_KEY = os.getenv("RC_API_KEY")
rc_project = Project(api_url, RC_API_KEY)

# Upload instruments to REDCap using the import_metadata method
try:
    response = rc_project.import_metadata(all_instruments, import_format='df')
    print(f"✓ Successfully uploaded {response} fields to REDCap")
except Exception as e:
    print(f"✗ Error uploading to REDCap: {e}")

