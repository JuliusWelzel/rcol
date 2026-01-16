# RTG Instruments

These instruments are from the Research Training Group (RTG) study, designed for specialized clinical and research applications.

---

## study_participant_information

**Study Participant Information**

Basic demographic and study enrollment information.

```python exec="true"
import pandas as pd
from rcol.rtg import study_participant_information

print(f"**Shape:** {study_participant_information.shape[0]} fields × {study_participant_information.shape[1]} columns")
print()
print(study_participant_information[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.rtg import study_participant_information
    
    print(study_participant_information)
    ```

---

## fal_initial_questionnaire

**FAL Initial Questionnaire**

Initial assessment questionnaire for the FAL study.

```python exec="true"
import pandas as pd
from rcol.rtg import fal_initial_questionnaire

print(f"**Shape:** {fal_initial_questionnaire.shape[0]} fields × {fal_initial_questionnaire.shape[1]} columns")
print()
print(fal_initial_questionnaire[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.rtg import fal_initial_questionnaire
    
    print(fal_initial_questionnaire)
    ```

---

## becks_depression_inventory_ii

**Beck's Depression Inventory II**

RTG version of the BDI-II for depression screening.

```python exec="true"
import pandas as pd
from rcol.rtg import becks_depression_inventory_ii

print(f"**Shape:** {becks_depression_inventory_ii.shape[0]} fields × {becks_depression_inventory_ii.shape[1]} columns")
print()
print(becks_depression_inventory_ii[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## stroke_telephone_interview

**Stroke Telephone Interview**

Phone-based assessment for stroke patients.

```python exec="true"
import pandas as pd
from rcol.rtg import stroke_telephone_interview

print(f"**Shape:** {stroke_telephone_interview.shape[0]} fields × {stroke_telephone_interview.shape[1]} columns")
print()
print(stroke_telephone_interview[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## frageboden_grk_p10

**Frageboden GRK P10**

Research Training Group P10 questionnaire.

```python exec="true"
import pandas as pd
from rcol.rtg import frageboden_grk_p10

print(f"**Shape:** {frageboden_grk_p10.shape[0]} fields × {frageboden_grk_p10.shape[1]} columns")
print()
print(frageboden_grk_p10[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## sf12

**SF-12 Health Survey**

Short-form health survey measuring quality of life.

```python exec="true"
import pandas as pd
from rcol.rtg import sf12

print(f"**Shape:** {sf12.shape[0]} fields × {sf12.shape[1]} columns")
print()
print(sf12[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## jebsen_taylor_hand_function_test

**Jebsen-Taylor Hand Function Test**

Assessment of hand function for daily activities.

```python exec="true"
import pandas as pd
from rcol.rtg import jebsen_taylor_hand_function_test

print(f"**Shape:** {jebsen_taylor_hand_function_test.shape[0]} fields × {jebsen_taylor_hand_function_test.shape[1]} columns")
print()
print(jebsen_taylor_hand_function_test[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## functional_gait_assessment

**Functional Gait Assessment**

Assessment of gait and balance abilities.

```python exec="true"
import pandas as pd
from rcol.rtg import functional_gait_assessment

print(f"**Shape:** {functional_gait_assessment.shape[0]} fields × {functional_gait_assessment.shape[1]} columns")
print()
print(functional_gait_assessment[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## tapm_divided_attention_dual_task

**TAPM Divided Attention Dual Task**

Test of attentional performance measuring divided attention.

```python exec="true"
import pandas as pd
from rcol.rtg import tapm_divided_attention_dual_task

print(f"**Shape:** {tapm_divided_attention_dual_task.shape[0]} fields × {tapm_divided_attention_dual_task.shape[1]} columns")
print()
print(tapm_divided_attention_dual_task[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## tapm_executive_control

**TAPM Executive Control**

Test of attentional performance measuring executive control.

```python exec="true"
import pandas as pd
from rcol.rtg import tapm_executive_control

print(f"**Shape:** {tapm_executive_control.shape[0]} fields × {tapm_executive_control.shape[1]} columns")
print()
print(tapm_executive_control[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## tapm_gonogo

**TAPM Go/No-Go**

Test of attentional performance measuring response inhibition.

```python exec="true"
import pandas as pd
from rcol.rtg import tapm_gonogo

print(f"**Shape:** {tapm_gonogo.shape[0]} fields × {tapm_gonogo.shape[1]} columns")
print()
print(tapm_gonogo[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## tapm_distractibility

**TAPM Distractibility**

Test of attentional performance measuring distractibility.

```python exec="true"
import pandas as pd
from rcol.rtg import tapm_distractibility

print(f"**Shape:** {tapm_distractibility.shape[0]} fields × {tapm_distractibility.shape[1]} columns")
print()
print(tapm_distractibility[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## moca

**Montreal Cognitive Assessment (RTG version)**

RTG-specific version of the MoCA cognitive screening.

```python exec="true"
import pandas as pd
from rcol.rtg import moca

print(f"**Shape:** {moca.shape[0]} fields × {moca.shape[1]} columns")
print()
print(moca[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## aachener_aphasia_test

**Aachener Aphasia Test**

Assessment for language disorders (aphasia).

```python exec="true"
import pandas as pd
from rcol.rtg import aachener_aphasia_test

print(f"**Shape:** {aachener_aphasia_test.shape[0]} fields × {aachener_aphasia_test.shape[1]} columns")
print()
print(aachener_aphasia_test[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## modified_ashworth_scale

**Modified Ashworth Scale**

Scale for measuring muscle spasticity.

```python exec="true"
import pandas as pd
from rcol.rtg import modified_ashworth_scale

print(f"**Shape:** {modified_ashworth_scale.shape[0]} fields × {modified_ashworth_scale.shape[1]} columns")
print()
print(modified_ashworth_scale[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## upper_extremity_fuglmeyer_assessment

**Upper Extremity Fugl-Meyer Assessment**

Assessment of motor function in the upper extremity post-stroke.

```python exec="true"
import pandas as pd
from rcol.rtg import upper_extremity_fuglmeyer_assessment

print(f"**Shape:** {upper_extremity_fuglmeyer_assessment.shape[0]} fields × {upper_extremity_fuglmeyer_assessment.shape[1]} columns")
print()
print(upper_extremity_fuglmeyer_assessment[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## action_research_arm_test

**Action Research Arm Test**

Assessment of upper limb function.

```python exec="true"
import pandas as pd
from rcol.rtg import action_research_arm_test

print(f"**Shape:** {action_research_arm_test.shape[0]} fields × {action_research_arm_test.shape[1]} columns")
print()
print(action_research_arm_test[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## modified_frenchay_scale

**Modified Frenchay Scale**

Assessment of arm function in daily activities.

```python exec="true"
import pandas as pd
from rcol.rtg import modified_frenchay_scale

print(f"**Shape:** {modified_frenchay_scale.shape[0]} fields × {modified_frenchay_scale.shape[1]} columns")
print()
print(modified_frenchay_scale[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## stroke_impact_scale

**Stroke Impact Scale**

Comprehensive measure of stroke outcomes and quality of life.

```python exec="true"
import pandas as pd
from rcol.rtg import stroke_impact_scale

print(f"**Shape:** {stroke_impact_scale.shape[0]} fields × {stroke_impact_scale.shape[1]} columns")
print()
print(stroke_impact_scale[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

---

## nasatlx

**NASA Task Load Index**

Subjective workload assessment tool.

```python exec="true"
import pandas as pd
from rcol.rtg import nasatlx

print(f"**Shape:** {nasatlx.shape[0]} fields × {nasatlx.shape[1]} columns")
print()
print(nasatlx[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```
