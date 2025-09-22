# ALU Regex Data Extraction

## Overview

This project provides Python utilities for extracting and validating common data types from text using regular expressions.  
It is designed to help you reliably find and check patterns such as emails, URLs, phone numbers, credit card numbers, time formats, HTML tags, hashtags, and currency amounts.

## Supported Data Types

- **Emails**
- **URLs**
- **Phone numbers**
- **Credit card numbers**
- **Time formats** (24-hour and 12-hour)
- **HTML tags**
- **Hashtags**
- **Currency amounts**

## File Structure

- `src/regex_patterns.py`  
  Extraction functions for each data type using regular expressions.
- `src/validators.py`  
  Validation functions for each data type using regular expressions.
- `src/raw_regex.txt`  
  Reference file containing raw regex patterns for all supported types.
- `test.py`  
  Unit tests for all extraction and validation functions.
- `README.md`  
  Project documentation.

## Usage

### Extraction Example

```python
from src.regex_patterns import extract_and_validate_emails

text = "Contact us at support@example.com or admin@company.co.uk"
emails = extract_and_validate_emails(text)
print(emails)  # ['support@example.com', 'admin@company.co.uk']
```

### Validation Example

```python
from src.validators import validate_emails

print(validate_emails("support@example.com"))  # True
print(validate_emails("invalid-email"))        # False
```

## Running Tests

To run all unit tests, use:

```sh
python test.py
```

All tests are grouped by data type for clarity and maintainability.

## Regex Reference

See `src/raw_regex.txt` for all raw regex patterns used for extraction and validation.

## Requirements

- Python 3.x
- No external dependencies required

<!-- ## License

MIT License -->