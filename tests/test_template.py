import pandas as pd
from rcol.template import RedcapInstrumentTemplate

def test_create_template():
    fields = ['record_id', 'field1', 'field2']
    template = RedcapInstrumentTemplate(fields, 'test_instrument')
    df = template.create_template(3)
    assert list(df.columns) == fields
    assert len(df) == 3

def test_stack_templates():
    fields = ['record_id', 'field1']
    t = RedcapInstrumentTemplate(fields, 'test')
    df1 = t.create_template(2)
    df2 = t.create_template(1)
    stacked = RedcapInstrumentTemplate.stack_templates([df1, df2])
    assert len(stacked) == 3
    assert list(stacked.columns) == fields

def test_to_redcap_format():
    fields = ['record_id', 'field1']
    t = RedcapInstrumentTemplate(fields, 'test')
    df = t.create_template(1)
    formatted = t.to_redcap_format(df)
    assert isinstance(formatted, pd.DataFrame)
    assert list(formatted.columns) == fields

def test_redcap_compatibility():
    # Simulate REDCap compatibility: all columns must be strings, no missing field names
    fields = ['record_id', 'field1', 'field2']
    t = RedcapInstrumentTemplate(fields, 'test')
    df = t.create_template(2)
    assert all(isinstance(col, str) for col in df.columns)
    assert all(col for col in df.columns)
