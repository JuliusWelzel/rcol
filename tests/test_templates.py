"""Tests validating all REDCap instrument templates."""

from __future__ import annotations

import pandas as pd
import pytest

from rcol import instruments as inst
from rcol import rtg

REQUIRED_COLUMNS = {
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
    "field_annotation",
}


INSTRUMENTS = {
    name: value
    for name, value in vars(inst).items()
    if isinstance(value, pd.DataFrame) and not name.startswith("_")
}

# Add RTG instruments
RTG_INSTRUMENTS = {
    name: value
    for name, value in vars(rtg).items()
    if isinstance(value, pd.DataFrame) and not name.startswith("_")
}

INSTRUMENTS.update(RTG_INSTRUMENTS)

assert INSTRUMENTS, "No instrument DataFrames discovered in rcol.instruments or rcol.rtg"


@pytest.mark.parametrize("name, dataframe", INSTRUMENTS.items())
def test_instrument_is_dataframe(name: str, dataframe: pd.DataFrame) -> None:
    """Ensure each instrument exposes a pandas DataFrame."""

    assert isinstance(
        dataframe, pd.DataFrame
    ), f"Instrument '{name}' must be a pandas DataFrame"
    assert not dataframe.empty, f"Instrument '{name}' must contain at least one field"


@pytest.mark.parametrize("name, dataframe", INSTRUMENTS.items())
def test_instrument_has_required_columns(name: str, dataframe: pd.DataFrame) -> None:
    """Validate the REDCap metadata columns are present."""

    missing = REQUIRED_COLUMNS.difference(dataframe.columns)
    assert not missing, (
        f"Instrument '{name}' is missing required columns: "
        f"{', '.join(sorted(missing))}"
    )


@pytest.mark.parametrize("name, dataframe", INSTRUMENTS.items())
def test_instrument_field_name_integrity(name: str, dataframe: pd.DataFrame) -> None:
    """Check that field names are unique and non-empty."""

    assert dataframe["field_name"].notna().all(), (
        f"Instrument '{name}' contains empty field_name entries"
    )
    duplicates = dataframe[dataframe["field_name"].duplicated()]["field_name"].tolist()
    assert not duplicates, (
        f"Instrument '{name}' has duplicate field_name entries: "
        f"{', '.join(duplicates)}"
    )