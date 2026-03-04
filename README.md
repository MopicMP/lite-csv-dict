# lite-csv-dict

> Lite read csv directly into list of dicts

[![PyPI version](https://badge.fury.io/py/lite-csv-dict.svg)](https://pypi.org/project/lite-csv-dict/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)

## Installation

```bash
pip install lite-csv-dict
```

## Quick Start

```python
from lite_csv_dict import dict

# Basic usage
result = dict("your input here")
print(result)
```

## Features

- Simple, clean API with type hints
- Zero dependencies (pure Python)
- Python 3.8+ compatible
- Fully tested
- Lightweight (< 5KB)

## API Reference

### `dict(input)`

Main utility function.

**Parameters:**
- `input` — The input data to process

**Returns:** Processed result

### `batch(inputs)`

Process multiple inputs at once.

**Parameters:**
- `inputs` — List of inputs

**Returns:** List of results

## Examples

```python
from lite_csv_dict import dict

# Example 1: Basic usage
result = dict("Hello World")

# Example 2: Batch processing
from lite_csv_dict import batch
results = batch(["item1", "item2", "item3"])
```

## Running Tests

```bash
pip install pytest
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

### Learn More

**Want to build tools like this?** Check out the
**[Python For Beginners](https://gumroad.com/l/python-for-beginners)** course — it teaches you
step-by-step how to create useful Python utilities from scratch,
with real-world projects and best practices.

*Built with skills from [Python For Beginners](https://gumroad.com/l/python-for-beginners)*
