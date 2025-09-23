# ALU Regex Data Extraction

## Overview

ALU Regex Data Extraction is a Python project that provides easy-to-use utilities for **extracting** and **validating** common data types from text using regular expressions.  
It is designed to help you reliably find and check patterns such as emails, URLs, phone numbers, credit card numbers, time formats, HTML tags, hashtags, and currency amounts in any text data.

## Supported Data Types

- **Emails** (e.g., `user@example.com`)
- **URLs** (e.g., `https://www.example.com`)
- **Phone numbers** (e.g., `(123) 456-7890`, `123-456-7890`)
- **Credit card numbers** (e.g., `1234 5678 9012 3456`)
- **Time formats** (24-hour and 12-hour, e.g., `14:30`, `2:30 PM`)
- **HTML tags** (e.g., `<div>`, `<a href="#">`)
- **Hashtags** (e.g., `#Python`)
- **Currency amounts** (e.g., `$1,234.56`)

## Features

- **Extraction functions**: Find all valid matches of a data type in a given text.
- **Validation functions**: Check if a single string is a valid instance of a data type.
- **Simple API**: Consistent function names and usage patterns.
- **No external dependencies**: Only Python's built-in `re` module is used.

## File Structure

- `src/regex_patterns.py`  
  Contains extraction functions for each data type using regular expressions.
- `src/validators.py`  
  Contains validation functions for each data type using regular expressions.
- `src/raw_regex.txt`  
  Reference file containing raw regex patterns for all supported types.
- `test.py`  
  Unit tests for all extraction and validation functions.
- `README.md`  
  Project documentation.

## Usage

### Extraction Example

To extract all email addresses from a text:

```python
from src.regex_patterns import RegexExtractor

text = "Contact us at support@example.com or admin@company.co.uk"
emails = RegexExtractor.extract_emails(text)
print(emails)  # Output: ['support@example.com', 'admin@company.co.uk']
```

You can similarly extract URLs, phone numbers, and other supported types using the corresponding `extract_*` methods.

### Validation Example

To check if a string is a valid email address:

```python
from src.validators import RegexValidator

print(RegexValidator.validate_email("support@example.com"))  # Output: True
print(RegexValidator.validate_email("invalid-email"))        # Output: False
```

Validation methods are available for all supported data types.

### Extract All Example

To extract all supported data types from a text at once:

```python
from src.regex_patterns import RegexExtractor

text = "Email: user@mail.com, Phone: 123-456-7890, Price: $99.99"
results = RegexExtractor.extract_all(text)
print(results)
# Output: {'emails': ['user@mail.com'], 'urls': [], 'phones': ['123-456-7890'], ...}
```

## Running Tests

To run all unit tests and verify the correctness of extraction and validation functions, use:

```sh
python test.py
```

All tests are grouped by data type for clarity and maintainability.

## Regex Reference

For a list of all raw regex patterns used for extraction and validation, see `src/raw_regex.txt`.

## Requirements

- Python 3.x
- No external dependencies required

---

<!-- ## License

MIT License -->