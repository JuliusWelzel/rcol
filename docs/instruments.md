# Instrument Reference

These tables are rendered directly from the `pandas.DataFrame` objects shipped in
`rcol.instruments` using `mkdocstrings`.

## fal

**Fragebogen zur Allgemeinen Leistungsfähigkeit (General Performance Questionnaire)**

```python
from rcol.instruments import fal
print(fal.shape)  # (rows, columns)
print(fal.head())
```

::: rcol.instruments.fal
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

## ehi

**Edinburgh Handedness Inventory**

```python
from rcol.instruments import ehi
print(ehi.shape)  # (rows, columns)
print(ehi.head())
```

::: rcol.instruments.ehi
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

## bdi_ii

**Beck Depression Inventory II**

```python
from rcol.instruments import bdi_ii
print(bdi_ii.shape)  # (rows, columns)
print(bdi_ii.head())
```

::: rcol.instruments.bdi_ii
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

## moca

**Montreal Cognitive Assessment**

```python
from rcol.instruments import moca
print(moca.shape)  # (rows, columns)
print(moca.head())
```

::: rcol.instruments.moca
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

## tmt

**Trail Making Test**

```python
from rcol.instruments import tmt
print(tmt.shape)  # (rows, columns)
print(tmt.head())
```

::: rcol.instruments.tmt
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

## wnss

**Weinstein's Noise Sensitivity Scale (WNSS-21)**

```python
from rcol.instruments import wnss
print(wnss.shape)  # (rows, columns)
print(wnss.head())
```

::: rcol.instruments.wnss
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

## RTG Instruments

The following instruments are from the RTG (Rostock Treatment Group) study:

### study_participant_information

**Study Participant Information**

```python
from rcol.rtg import study_participant_information
print(study_participant_information.shape)
print(study_participant_information.head())
```

::: rcol.rtg.study_participant_information
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### fal_initial_questionnaire

**FAL Initial Questionnaire**

```python
from rcol.rtg import fal_initial_questionnaire
print(fal_initial_questionnaire.shape)
print(fal_initial_questionnaire.head())
```

::: rcol.rtg.fal_initial_questionnaire
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### becks_depression_inventory_ii

**Beck's Depression Inventory II**

```python
from rcol.rtg import becks_depression_inventory_ii
print(becks_depression_inventory_ii.shape)
print(becks_depression_inventory_ii.head())
```

::: rcol.rtg.becks_depression_inventory_ii
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### stroke_telephone_interview

**Stroke Telephone Interview**

```python
from rcol.rtg import stroke_telephone_interview
print(stroke_telephone_interview.shape)
print(stroke_telephone_interview.head())
```

::: rcol.rtg.stroke_telephone_interview
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### frageboden_grk_p10

**Frageboden GRK P10**

```python
from rcol.rtg import frageboden_grk_p10
print(frageboden_grk_p10.shape)
print(frageboden_grk_p10.head())
```

::: rcol.rtg.frageboden_grk_p10
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### sf12

**SF-12 Health Survey**

```python
from rcol.rtg import sf12
print(sf12.shape)
print(sf12.head())
```

::: rcol.rtg.sf12
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### jebsen_taylor_hand_function_test

**Jebsen-Taylor Hand Function Test**

```python
from rcol.rtg import jebsen_taylor_hand_function_test
print(jebsen_taylor_hand_function_test.shape)
print(jebsen_taylor_hand_function_test.head())
```

::: rcol.rtg.jebsen_taylor_hand_function_test
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### functional_gait_assessment

**Functional Gait Assessment**

```python
from rcol.rtg import functional_gait_assessment
print(functional_gait_assessment.shape)
print(functional_gait_assessment.head())
```

::: rcol.rtg.functional_gait_assessment
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### tapm_divided_attention_dual_task

**TAPM Divided Attention Dual Task**

```python
from rcol.rtg import tapm_divided_attention_dual_task
print(tapm_divided_attention_dual_task.shape)
print(tapm_divided_attention_dual_task.head())
```

::: rcol.rtg.tapm_divided_attention_dual_task
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### tapm_executive_control

**TAPM Executive Control**

```python
from rcol.rtg import tapm_executive_control
print(tapm_executive_control.shape)
print(tapm_executive_control.head())
```

::: rcol.rtg.tapm_executive_control
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### tapm_gonogo

**TAPM Go/No-Go**

```python
from rcol.rtg import tapm_gonogo
print(tapm_gonogo.shape)
print(tapm_gonogo.head())
```

::: rcol.rtg.tapm_gonogo
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### tapm_distractibility

**TAPM Distractibility**

```python
from rcol.rtg import tapm_distractibility
print(tapm_distractibility.shape)
print(tapm_distractibility.head())
```

::: rcol.rtg.tapm_distractibility
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### moca

**Montreal Cognitive Assessment (RTG version)**

```python
from rcol.rtg import moca
print(moca.shape)
print(moca.head())
```

::: rcol.rtg.moca
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### aachener_aphasia_test

**Aachener Aphasia Test**

```python
from rcol.rtg import aachener_aphasia_test
print(aachener_aphasia_test.shape)
print(aachener_aphasia_test.head())
```

::: rcol.rtg.aachener_aphasia_test
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### modified_ashworth_scale

**Modified Ashworth Scale**

```python
from rcol.rtg import modified_ashworth_scale
print(modified_ashworth_scale.shape)
print(modified_ashworth_scale.head())
```

::: rcol.rtg.modified_ashworth_scale
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### upper_extremity_fuglmeyer_assessment

**Upper Extremity Fugl-Meyer Assessment**

```python
from rcol.rtg import upper_extremity_fuglmeyer_assessment
print(upper_extremity_fuglmeyer_assessment.shape)
print(upper_extremity_fuglmeyer_assessment.head())
```

::: rcol.rtg.upper_extremity_fuglmeyer_assessment
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### action_research_arm_test

**Action Research Arm Test**

```python
from rcol.rtg import action_research_arm_test
print(action_research_arm_test.shape)
print(action_research_arm_test.head())
```

::: rcol.rtg.action_research_arm_test
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### modified_frenchay_scale

**Modified Frenchay Scale**

```python
from rcol.rtg import modified_frenchay_scale
print(modified_frenchay_scale.shape)
print(modified_frenchay_scale.head())
```

::: rcol.rtg.modified_frenchay_scale
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### stroke_impact_scale

**Stroke Impact Scale**

```python
from rcol.rtg import stroke_impact_scale
print(stroke_impact_scale.shape)
print(stroke_impact_scale.head())
```

::: rcol.rtg.stroke_impact_scale
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

### nasatlx

**NASA Task Load Index**

```python
from rcol.rtg import nasatlx
print(nasatlx.shape)
print(nasatlx.head())
```

::: rcol.rtg.nasatlx
    handler: python
    options:
        show_source: false
        show_root_heading: false
        show_root_toc_entry: false

