import re
"""
validators.py

Validation functions for common data types using regular expressions.
Each function takes a single string and returns True if it matches the pattern, False otherwise.
Supported types: emails, URLs, phone numbers, credit cards, time, HTML tags, hashtags, currency.
"""

def validate_emails(email):
    """
    Validates if the input string is a valid email address.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    return re.match(pattern, email, re.IGNORECASE) is not None

def validate_urls(url):
    """
    Validates if the input string is a valid URL.

    Args:
        url (str): URL to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
    return re.match(pattern, url, re.IGNORECASE) is not None

def validate_phone_num(phone_number):
    """
    Validates if the input string is a valid phone number.

    Args:
        phone_number (str): Phone number to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'\(?[0-9]{3}\)?[ -.]{1}[0-9]{3}[ -.]{1}[0-9]{4}\b'
    return re.match(pattern, phone_number, re.IGNORECASE) is not None

def validate_credit_card(credit_card_number):
    """
    Validates if the input string is a valid credit card number.

    Args:
        credit_card_number (str): Credit card number to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'[0-9]{4}[ -][0-9]{4}[ -][0-9]{4}[ -][0-9]{4}\b'
    return re.match(pattern, credit_card_number, re.IGNORECASE) is not None

def validate_time(time):
    """
    Validates if the input string is a valid time format (24-hour or 12-hour).

    Args:
        time (str): Time string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'[01]?[0-9]{1}:[0-5]{1}[0-9]{1}( [AP]M)?'
    return re.match(pattern, time, re.IGNORECASE) is not None

def validate_html(html_tag):
    """
    Validates if the input string is a valid HTML tag.

    Args:
        html_tag (str): HTML tag to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'<([a-zA-Z][a-zA-Z0-9]*)(?![^>]*\/>)[^>]*>'
    return re.match(pattern, html_tag, re.IGNORECASE) is not None

def validate_hashtag(hashtag):
    """
    Validates if the input string is a valid hashtag.

    Args:
        hashtag (str): Hashtag to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'#\w+'
    return re.match(pattern, hashtag, re.IGNORECASE) is not None

def validate_currency(currency):
    """
    Validates if the input string is a valid currency amount.

    Args:
        currency (str): Currency string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r'\$[0-9,]+\.[0-9]+'
    return re.match(pattern, currency, re.IGNORECASE) is not None
