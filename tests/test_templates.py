from src.instruments import fal, ehi

def test_template_columns():
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

