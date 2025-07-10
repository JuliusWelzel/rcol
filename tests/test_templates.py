import pandas as pd
from redcap_templates import get_instrument_template, stack_instruments

def test_template_columns():
    fal = get_instrument_template("fal")
    ehi = get_instrument_template("ehi")
    # FAL
    assert "record_id" in fal.columns
    assert "fal_datum" in fal.columns
    assert "fal_alter" in fal.columns
    assert "fal_haendigkeit" in fal.columns
    # EHI
    assert "ehi_schreiben" in ehi.columns
    assert "ehi_zeichnen" in ehi.columns
    assert "ehi_werfen" in ehi.columns
    assert "ehi_schere" in ehi.columns

def test_stack_instruments():
    fal1 = get_instrument_template("fal")
    fal2 = get_instrument_template("fal")
    fal1.loc[0] = [1] + [None]*(len(fal1.columns)-1)
    fal2.loc[0] = [2] + [None]*(len(fal2.columns)-1)
    stacked = stack_instruments([fal1, fal2])
    assert len(stacked) == 2
    assert "record_id" in stacked.columns
    # EHI
    ehi1 = get_instrument_template("ehi")
    ehi2 = get_instrument_template("ehi")
    ehi1.loc[0] = [1] + [None]*(len(ehi1.columns)-1)
    ehi2.loc[0] = [2] + [None]*(len(ehi2.columns)-1)
    stacked_ehi = stack_instruments([ehi1, ehi2])
    assert len(stacked_ehi) == 2
    assert "ehi_schreiben" in stacked_ehi.columns

def test_redcap_compatibility():
    fal = get_instrument_template("fal")
    ehi = get_instrument_template("ehi")
    # FAL
    assert all(isinstance(col, str) and col for col in fal.columns)
    assert fal.empty
    # EHI
    assert all(isinstance(col, str) and col for col in ehi.columns)
    assert ehi.empty
