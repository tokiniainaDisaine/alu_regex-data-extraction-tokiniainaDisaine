import re

def validate_emails(email):
    pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    return re.match(pattern, email, re.IGNORECASE) is not None

def validate_urls(url):
    pattern = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)'
    return re.match(pattern, url, re.IGNORECASE) is not None

def validate_phone_num(phone_number):
    pattern = r'\(?[0-9]{3}\)?[ -.]{1}[0-9]{3}[ -.]{1}[0-9]{4}\b'
    return re.match(pattern, phone_number, re.IGNORECASE) is not None

def validate_credit_card(credit_card_number):
    pattern = r'[0-9]{4}[ -][0-9]{4}[ -][0-9]{4}[ -][0-9]{4}\b'
    return re.match(pattern, credit_card_number, re.IGNORECASE) is not None

def validate_time(time):
    pattern = r'[01]?[0-9]{1}:[0-5]{1}[0-9]{1}( [AP]M)?'
    return re.match(pattern, time, re.IGNORECASE) is not None

def validate_html(html_tag):
    pattern = r'<([a-zA-Z][a-zA-Z0-9]*)(?![^>]*\/>)[^>]*>'
    return re.match(pattern, html_tag, re.IGNORECASE) is not None

def validate_hashtag(hashtag):
    pattern = r'#\w+'
    return re.match(pattern, hashtag, re.IGNORECASE) is not None

def validate_currency(currency):
    pattern = r'\$[0-9,]+\.[0-9]+'
    return re.match(pattern, currency, re.IGNORECASE) is not None
