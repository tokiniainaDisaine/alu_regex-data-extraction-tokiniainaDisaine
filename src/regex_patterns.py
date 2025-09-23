import re
"""
regex_patterns.py

Extraction functions for common data types using regular expressions.
Each function takes a text input and returns a list of valid matches.
Supported types: emails, URLs, phone numbers, credit cards, time, HTML tags, hashtags, currency.
"""

class RegexExtractor:
    @staticmethod
    def extract_emails(text):
        """
        Extracts valid email addresses from the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of valid email addresses found in the text.
        """
        pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[a-zA-Z]{2,}\b'
        return re.findall(pattern, text, re.IGNORECASE)

    @staticmethod
    def extract_urls(text):
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

    @staticmethod
    def extract_phone_numbers(text):
        """
        Extracts valid phone numbers from the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of valid phone numbers found in the text.
        """
        pattern = r'\(?\d{3}\)?[ -.]\d{3}[ -.]\d{4}\b'
        return re.findall(pattern, text, re.IGNORECASE)

    @staticmethod
    def extract_credit_cards(text):
        """
        Extracts valid credit card numbers from the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of valid credit card numbers found in the text.
        """
        pattern = r'\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}\b'
        return re.findall(pattern, text, re.IGNORECASE)

    @staticmethod
    def extract_time(text):
        """
        Extracts valid time formats (24-hour and 12-hour) from the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of valid time strings found in the text.
        """
        pattern = r'((?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?)'
        matches = re.finditer(pattern, text, re.IGNORECASE)
        return [m.group(0) for m in matches]

    @staticmethod
    def extract_html_tags(text):
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

    @staticmethod
    def extract_hashtags(text):
        """
        Extracts valid hashtags from the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of valid hashtags found in the text.
        """
        pattern = r'#\w+'
        return re.findall(pattern, text, re.IGNORECASE)

    @staticmethod
    def extract_currency(text):
        """
        Extracts valid currency amounts from the given text.

        Args:
            text (str): Input text.

        Returns:
            list: List of valid currency amounts found in the text.
        """
        pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2,})?\b'
        return re.findall(pattern, text, re.IGNORECASE)

    @staticmethod
    def extract_all(text):
        """Run all extractors and return results as a dict."""
        return {
            "emails": RegexExtractor.extract_emails(text),
            "urls": RegexExtractor.extract_urls(text),
            "phones": RegexExtractor.extract_phone_numbers(text),
            "credit_cards": RegexExtractor.extract_credit_cards(text),
            "time": RegexExtractor.extract_time(text),
            "html_tags": RegexExtractor.extract_html_tags(text),
            "hashtags": RegexExtractor.extract_hashtags(text),
            "currency": RegexExtractor.extract_currency(text)
        }