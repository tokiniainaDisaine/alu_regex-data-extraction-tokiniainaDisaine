import re

def extract_and_validate_emails(text):
    pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_urls(text):
    pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    return [m.group(0) for m in matches]

def extract_and_validate_phone_num(text):
    pattern = r'\(?[0-9]{3}\)?[ -.]{1}[0-9]{3}[ -.]{1}[0-9]{4}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_credit_card(text):
    pattern = r'[0-9]{4}[ -][0-9]{4}[ -][0-9]{4}[ -][0-9]{4}\b'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_time(text):
    pattern = r'[01]?[0-9]{1}:[0-5]{1}[0-9]{1}( [AP]M)?'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    return [m.group(0) for m in matches]

def extract_and_validate_html(text):
    pattern = r'<([a-zA-Z][a-zA-Z0-9]*)(?![^>]*\/>)[^>]*>'
    matches = re.finditer(pattern, text, re.IGNORECASE)
    return [m.group(0) for m in matches]

def extract_and_validate_hashtag(text):
    pattern = r'#\w+'
    return re.findall(pattern, text, re.IGNORECASE)

def extract_and_validate_currency(text):
    pattern = r'\$[0-9,]+\.[0-9]+'
    return re.findall(pattern, text, re.IGNORECASE)