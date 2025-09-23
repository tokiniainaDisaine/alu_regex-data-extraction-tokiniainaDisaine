# ALU Regex Data Extraction

## Overview

This project provides Python utilities for extracting and validating common data types from text using regular expressions.  
Supported data types include:
- Emails
- URLs
- Phone numbers
- Credit card numbers
- Time formats
- HTML tags
- Hashtags
- Currency amounts

Each data type has:
- An extraction method (`extract_*`) that finds valid matches in text.
- A validation method (`validate_*`) that checks if a single string is valid.

## File Structure

- `src/regex_patterns.py`: Extraction functions using regex.
- `src/validators.py`: Validation functions using regex.
- `test.py`: Unit tests for all extract and validate functions.
- `README.md`: Project documentation.

## Usage

### Extraction Example

```python
from src.regex_patterns import RegexExtractor

text = "Contact us at support@example.com or admin@company.co.uk"
emails = RegexExtractor.extract_emails(text)
print(emails)  # ['support@example.com', 'admin@company.co.uk']
```

### Validation Example

```python
from src.validators import RegexValidator

print(RegexValidator.validate_email("support@example.com"))  # True
print(RegexValidator.validate_email("invalid-email"))        # False
```

## Running Tests

To run all unit tests, use:

```sh
python test.py
```

All tests are grouped by data type for clarity and maintainability.

## Requirements

- Python 3.x

No external dependencies are required.

<!-- ## License

MIT License -->