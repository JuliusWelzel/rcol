# Troubleshooting

Common issues and solutions when working with REDCap and `rcol`.

## Installation Issues

### rcol not found after installation

**Symptom:** `ModuleNotFoundError: No module named 'rcol'`

**Solutions:**

1. Ensure you're using the correct Python environment:
   ```bash
   # Check which Python is active
   which python  # Linux/macOS
   where python  # Windows
   ```

2. Reinstall rcol:
   ```bash
   uv add rcol
   # or
   pip install --upgrade rcol
   ```

3. Verify installation:
   ```bash
   python -c "import rcol; print('OK')"
   ```

---

### Dependency conflicts

**Symptom:** Error messages about incompatible package versions

**Solutions:**

1. Create a fresh virtual environment:
   ```bash
   uv venv --python 3.11
   uv add rcol
   ```

2. Or with pip:
   ```bash
   python -m venv .venv --clear
   .venv\Scripts\activate  # Windows
   pip install rcol
   ```

---

## API Issues

### 403 Forbidden Error

**Symptom:** `{"error": "You do not have permissions to use the API"}`

**Causes & Solutions:**

| Cause | Solution |
|-------|----------|
| Token not approved | Wait for admin approval |
| Wrong token | Verify token is copied correctly |
| Insufficient rights | Request additional API permissions |

---

### 401 Unauthorized Error

**Symptom:** `{"error": "Invalid token"}`

**Solutions:**

1. Verify your token is correct (no extra spaces)
2. Check if token was regenerated
3. Request a new token if necessary

---

### SSL Certificate Error

**Symptom:** `SSLCertVerifyError: certificate verify failed`

**Solutions:**

1. Update certifi package:
   ```bash
   pip install --upgrade certifi
   ```

2. If on a corporate network, you may need to install your organization's CA certificate

---

## Upload Issues

### Duplicate field names

**Symptom:** `{"error": "The field_name column contains duplicate values: record_id"}`

**Solution:**

Remove duplicate record_id when combining instruments:

```python
from rcol.instruments import fal, ehi
import pandas as pd

# Remove record_id from second instrument
ehi_no_id = ehi[ehi["field_name"] != "record_id"]

# Combine
instruments = pd.concat([fal, ehi_no_id], ignore_index=True)
```

---

### Invalid field type

**Symptom:** `{"error": "Invalid field type"}`

**Solution:**

Check that field_type values are valid:

```python
valid_types = [
    "text", "notes", "dropdown", "radio", 
    "checkbox", "yesno", "truefalse", 
    "file", "slider", "calc", "descriptive"
]

invalid = df[~df["field_type"].isin(valid_types)]
if len(invalid) > 0:
    print("Invalid field types found:")
    print(invalid[["field_name", "field_type"]])
```

---

### Branching logic errors

**Symptom:** Upload succeeds but branching logic doesn't work

**Solution:**

Verify branching logic syntax:

```python
# Check for common issues
for idx, row in df.iterrows():
    logic = row.get("branching_logic", "")
    if logic:
        # Check for smart quotes
        if '"' in logic or '"' in logic:
            print(f"Smart quotes in {row['field_name']}")
        
        # Check for missing brackets
        if logic.count('[') != logic.count(']'):
            print(f"Unbalanced brackets in {row['field_name']}")
```

---

## Survey Issues

### Survey link not working

**Checklist:**

- [ ] Project has surveys enabled
- [ ] Instrument is enabled as survey
- [ ] Survey status is "Active"
- [ ] Link is the correct type (public vs. participant-specific)

---

### Missing required field marker

**Solution:**

In survey settings, enable "Display required field indicator"

---

### Survey displays incorrectly on mobile

**Solutions:**

1. Use responsive field alignment
2. Test with REDCap's mobile preview
3. Avoid very long field labels

---

## Data Issues

### Exported data has wrong encoding

**Symptom:** Special characters (ä, ö, ü) display incorrectly

**Solution:**

```python
# When reading exported data
df = pd.read_csv("export.csv", encoding="utf-8-sig")

# When uploading
instruments.to_json(orient="records", force_ascii=False)
```

---

### Choices not displaying correctly

**Symptom:** Radio/dropdown choices show raw values

**Solution:**

Verify choice format: `value, label | value, label`

```python
# Correct format
choices = "1, Yes | 2, No | 3, Maybe"

# Common mistakes
wrong1 = "1,Yes | 2,No"      # Missing space after comma
wrong2 = "1, Yes; 2, No"      # Wrong separator (semicolon)
wrong3 = "Yes | No"           # Missing values
```

---

## Getting Help

If you're still stuck:

1. **Check REDCap documentation:** Your institution may have local guides
2. **Contact REDCap admin:** For project-specific issues
3. **Open an issue:** On the [rcol GitHub repository](https://github.com/your-org/rcol)

When reporting issues, include:

- Python version (`python --version`)
- rcol version (`pip show rcol`)
- Full error message
- Minimal code to reproduce the issue
