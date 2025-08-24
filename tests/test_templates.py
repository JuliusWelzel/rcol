from rcol.instruments import fal, ehi, bdi_ii
import pandas as pd
import pytest

required_columns = [
    "field_name",
    "form_name",
    "section_header",
    "field_type",
    "field_label",
    "choices",
    "field_note",
    "text_validation_type_or_show_slider_number",
    "text_validation_min",
    "text_validation_max",
    "identifier",
    "branching_logic",
    "required_field",
    "custom_alignment",
    "question_number",
    "matrix_group_name",
    "matrix_ranking",
    "field_annotation"
] 


instruments = ["fal", "ehi"]

@pytest.mark.parametrize("instrument", instruments)
def test_instrument_has_required_columns(instrument):
    for col in required_columns:
        assert col in instrument.columns, f"Missing column '{col}' in instrument '{instrument}'"