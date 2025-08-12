import pandas as pd

# FAL instrument metadata
fal_data = [
    {"field_name": "record_id", "form_name": "fal", "section_header": "", "field_type": "text", "field_label": "Probanden-ID", "choices": "", "field_note": "", "text_validation_type_or_show_slider_number": "", "text_validation_min": "", "text_validation_max": "", "identifier": "", "branching_logic": "", "required_field": "", "custom_alignment": "", "question_number": "", "matrix_group_name": "", "matrix_ranking": "", "field_annotation": ""},
    {"field_name": "fal_datum", "form_name": "fal", "section_header": "", "field_type": "text", "field_label": "Datum", "choices": "", "field_note": "", "text_validation_type_or_show_slider_number": "date_ymd", "text_validation_min": "", "text_validation_max": "", "identifier": "", "branching_logic": "", "required_field": "", "custom_alignment": "", "question_number": "", "matrix_group_name": "", "matrix_ranking": "", "field_annotation": ""},
    # ... (add all other fal_data dicts here) ...
]

# EHI instrument metadata
ehi_data = [
    {"field_name": "ehi_schreiben", "form_name": "edinburgh_handedness", "section_header": "", "field_type": "checkbox", "field_label": "1. Schreiben", "choices": "1, Links (1 Kreuz) | 2, Links (2 Kreuze) | 3, Rechts (1 Kreuz) | 4, Rechts (2 Kreuze) | 5, Beide gleich", "field_note": "", "text_validation_type_or_show_slider_number": "", "text_validation_min": "", "text_validation_max": "", "identifier": "", "branching_logic": "", "required_field": "", "custom_alignment": "", "question_number": "", "matrix_group_name": "", "matrix_ranking": "", "field_annotation": ""},
    {"field_name": "ehi_zeichnen", "form_name": "edinburgh_handedness", "section_header": "", "field_type": "checkbox", "field_label": "2. Zeichnen", "choices": "1, Links (1 Kreuz) | 2, Links (2 Kreuze) | 3, Rechts (1 Kreuz) | 4, Rechts (2 Kreuze) | 5, Beide gleich", "field_note": "", "text_validation_type_or_show_slider_number": "", "text_validation_min": "", "text_validation_max": "", "identifier": "", "branching_logic": "", "required_field": "", "custom_alignment": "", "question_number": "", "matrix_group_name": "", "matrix_ranking": "", "field_annotation": ""},
    # ... (add all other ehi_data dicts here) ...
]

fal = pd.DataFrame(fal_data)
ehi = pd.DataFrame(ehi_data)
