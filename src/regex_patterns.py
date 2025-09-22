import re
"""
regex_patterns.py

Extraction functions for common data types using regular expressions.
Each function takes a text input and returns a list of valid matches.
Supported types: emails, URLs, phone numbers, credit cards, time, HTML tags, hashtags, currency.
"""

def extract_and_validate_emails(text):
    """
    Extracts valid email addresses from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid email addresses found in the text.
    """
    pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_urls(text):
    """
    Extracts valid URLs from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid URLs found in the text.
    """
    pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    return [m.group(0) for m in matches]

def extract_and_validate_phone_num(text):
    """
    Extracts valid phone numbers from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid phone numbers found in the text.
    """
    pattern = r'\(?[0-9]{3}\)?[ -.]{1}[0-9]{3}[ -.]{1}[0-9]{4}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_credit_card(text):
    """
    Extracts valid credit card numbers from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid credit card numbers found in the text.
    """
    pattern = r'[0-9]{4}[ -][0-9]{4}[ -][0-9]{4}[ -][0-9]{4}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_time(text):
    """
    Extracts valid time formats (24-hour and 12-hour) from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid time strings found in the text.
    """
    pattern = r'[01]?[0-9]{1}:[0-5]{1}[0-9]{1}( [AP]M)?'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    return [m.group(0) for m in matches]

def extract_and_validate_html(text):
    """
    Extracts valid HTML tags from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid HTML tags found in the text.
    """
    pattern = r'<([a-zA-Z][a-zA-Z0-9]*)(?![^>]*\/>)[^>]*>'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    return [m.group(0) for m in matches]

def extract_and_validate_hashtag(text):
    """
    Extracts valid hashtags from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid hashtags found in the text.
    """
    pattern = r'#\w+'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_currency(text):
    """
    Extracts valid currency amounts from the given text.

    Args:
        text (str): Input text.

    Returns:
        list: List of valid currency amounts found in the text.
    """
    pattern = r'\$[0-9,]+\.[0-9]+'
    return re.findall(pattern, text, re.IGNORECASE)
