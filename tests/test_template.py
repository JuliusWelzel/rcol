import pandas as pd
from redcap_templates import get_instrument_template, stack_instruments

def test_create_template():
    fal = get_instrument_template("fal")
    df = fal.copy()
    assert "record_id" in df.columns
    assert len(df) == 0

def test_stack_templates():
    fal1 = get_instrument_template("fal")
    fal2 = get_instrument_template("fal")
    fal1.loc[0] = [1] + [None]*(len(fal1.columns)-1)
    fal2.loc[0] = [2] + [None]*(len(fal2.columns)-1)
    stacked = stack_instruments([fal1, fal2])
    assert len(stacked) == 2
    assert "record_id" in stacked.columns

def test_redcap_compatibility():
    fal = get_instrument_template("fal")
    assert all(isinstance(col, str) and col for col in fal.columns)
    assert fal.empty
