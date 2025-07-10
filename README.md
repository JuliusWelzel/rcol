# rcol

A Python package for creating, stacking, and uploading pandas DataFrame templates for REDCap instruments. Includes tests for REDCap compatibility. Uses uv for packaging and publishing to PyPI.

## Features
- DataFrame templates for REDCap instruments
- Stack and upload to REDCap projects
- REDCap compatibility testing
- PyPI-ready with uv

## Usage
Install with uv:
```sh
uv pip install .
```

Example usage:
```python
from redcap_templates import get_instrument_template, stack_instruments, upload_to_redcap

df = get_instrument_template('demographics')
# ... fill in data ...
stacked = stack_instruments([df])
# upload_to_redcap(stacked, api_url, api_token)
```

## Development
- Run tests with `pytest`
- Publish with `uv publish`

## License
MIT
