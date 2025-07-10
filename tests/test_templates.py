import pandas as pd
from redcap_templates import get_instrument_template, stack_instruments

def test_template_columns():
    fal = get_instrument_template("fal")
    assert "record_id" in fal.columns
    assert "fal_datum" in fal.columns
    assert "fal_alter" in fal.columns
    assert "fal_haendigkeit" in fal.columns

def test_stack_instruments():
    fal1 = get_instrument_template("fal")
    fal2 = get_instrument_template("fal")
    fal1.loc[0] = [1] + [None]*(len(fal1.columns)-1)
    fal2.loc[0] = [2] + [None]*(len(fal2.columns)-1)
    stacked = stack_instruments([fal1, fal2])
    assert len(stacked) == 2
    assert "record_id" in stacked.columns

def test_redcap_compatibility():
    fal = get_instrument_template("fal")
    # Check all columns are present and non-empty
    assert all(isinstance(col, str) and col for col in fal.columns)
    # Check that the DataFrame is empty (template)
    assert fal.empty
