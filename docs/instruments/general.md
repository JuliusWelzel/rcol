# General Instruments

These are standard questionnaires and assessments commonly used in research studies.

---

## fal

**Fragebogen zur Allgemeinen Leistungsfähigkeit (General Performance Questionnaire)**

A general questionnaire assessing overall performance and capabilities.

```python exec="true"
import pandas as pd
from rcol.instruments import fal

print(f"**Shape:** {fal.shape[0]} fields × {fal.shape[1]} columns")
print()
print(fal[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.instruments import fal
    
    # View all fields
    print(fal)
    
    # Get specific columns
    print(fal[['field_name', 'field_label']])
    ```

---

## ehi

**Edinburgh Handedness Inventory**

A standardized questionnaire to assess hand dominance (laterality).

```python exec="true"
import pandas as pd
from rcol.instruments import ehi

print(f"**Shape:** {ehi.shape[0]} fields × {ehi.shape[1]} columns")
print()
print(ehi[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.instruments import ehi
    
    # View all fields
    print(ehi)
    ```

---

## bdi_ii

**Beck Depression Inventory II**

A widely used self-report measure for assessing depression severity.

```python exec="true"
import pandas as pd
from rcol.instruments import bdi_ii

print(f"**Shape:** {bdi_ii.shape[0]} fields × {bdi_ii.shape[1]} columns")
print()
print(bdi_ii[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.instruments import bdi_ii
    
    # View all fields
    print(bdi_ii)
    ```

---

## moca

**Montreal Cognitive Assessment**

A screening tool for mild cognitive impairment.

```python exec="true"
import pandas as pd
from rcol.instruments import moca

print(f"**Shape:** {moca.shape[0]} fields × {moca.shape[1]} columns")
print()
print(moca[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.instruments import moca
    
    # View all fields
    print(moca)
    ```

---

## tmt

**Trail Making Test**

A neuropsychological test of visual attention and task switching.

```python exec="true"
import pandas as pd
from rcol.instruments import tmt

print(f"**Shape:** {tmt.shape[0]} fields × {tmt.shape[1]} columns")
print()
print(tmt[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.instruments import tmt
    
    # View all fields
    print(tmt)
    ```

---

## wnss

**Weinstein's Noise Sensitivity Scale (WNSS-21)**

A questionnaire measuring sensitivity to noise.

```python exec="true"
import pandas as pd
from rcol.instruments import wnss

print(f"**Shape:** {wnss.shape[0]} fields × {wnss.shape[1]} columns")
print()
print(wnss[['field_name', 'field_type', 'field_label']].to_markdown(index=False))
```

??? example "Usage Example"
    ```python
    from rcol.instruments import wnss
    
    # View all fields
    print(wnss)
    ```
