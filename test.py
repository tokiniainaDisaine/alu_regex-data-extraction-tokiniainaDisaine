import unittest
from src.regex_patterns import (
    extract_and_validate_emails, 
    extract_and_validate_urls, 
    extract_and_validate_phone_num, 
    extract_and_validate_credit_card,
    extract_and_validate_time,
    extract_and_validate_html,
    extract_and_validate_hashtag,
    extract_and_validate_currency
)
from src.validators import (
    validate_emails, 
    validate_urls, 
    validate_phone_num, 
    validate_credit_card,
    validate_time,
    validate_html,
    validate_hashtag,
    validate_currency
)

class TestEmails(unittest.TestCase):
    def test_extract_and_validate_emails(self):
        text = "Contact us at support@example.com or admin@company.co.uk or invalid email or user@com or user@.com"
        expected = ["support@example.com", "admin@company.co.uk"]
        self.assertEqual(extract_and_validate_emails(text), expected)

    def test_validate_email(self):
        self.assertTrue(validate_emails("support@example.com"))
        self.assertTrue(validate_emails("firstname.lastname@company.co.uk"))
        self.assertFalse(validate_emails("invalid-email"))
        self.assertFalse(validate_emails("user@com"))
        self.assertFalse(validate_emails("user@.com"))

class TestURLs(unittest.TestCase):
    def test_extract_and_validate_urls(self):
        text = "Visit https://www.example.com or https://subdomain.example.org/page or invalid-url or www.example.com or http://example"
        expected = ["https://www.example.com", "https://subdomain.example.org/page"]
        self.assertEqual(extract_and_validate_urls(text), expected)

    def test_validate_url(self):
        self.assertTrue(validate_urls("https://www.example.com"))
        self.assertTrue(validate_urls("http://subdomain.example.org/page"))
        self.assertFalse(validate_urls("invalid-url"))
        self.assertFalse(validate_urls("www.example.com"))
        self.assertFalse(validate_urls("http://example"))

class TestPhoneNumbers(unittest.TestCase):
    def test_extract_and_validate_phone_numbers(self):
        text = "Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890 or 123 456 7890 or 1234567890 or 123-456-789 or 123.456.789 or 123 456 789 or 123456789"
        expected = ["(123) 456-7890", "123-456-7890", "123.456.7890", "123 456 7890"]
        self.assertEqual(extract_and_validate_phone_num(text), expected)

    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_num("(123) 456-7890"))
        self.assertTrue(validate_phone_num("123-456-7890"))
        self.assertTrue(validate_phone_num("123.456.7890"))
        self.assertTrue(validate_phone_num("123 456 7890"))
        self.assertFalse(validate_phone_num("1234567890"))
        self.assertFalse(validate_phone_num("123-456-789"))
        self.assertFalse(validate_phone_num("123.456.789"))
        self.assertFalse(validate_phone_num("123 456 789"))
        self.assertFalse(validate_phone_num("123456789"))

class TestCreditCardNumbers(unittest.TestCase):
    def test_extract_and_validate_credit_card_numbers(self):
        text = "Credit card numbers: 1234 5678 9012 3456 or 1234-5678-9012-3456 or 1234567890123456 or 1234 5678 9012 345 or 123456789012345 or 1234-5678-9012-345 or 1234 5678 9012 34567"
        expected = ["1234 5678 9012 3456", "1234-5678-9012-3456"]
        self.assertEqual(extract_and_validate_credit_card(text), expected)

    def test_validate_credit_card_number(self):
        self.assertTrue(validate_credit_card("1234 5678 9012 3456"))
        self.assertTrue(validate_credit_card("1234-5678-9012-3456"))
        self.assertFalse(validate_credit_card("1234567890123456"))
        self.assertFalse(validate_credit_card("1234 5678 9012 345"))
        self.assertFalse(validate_credit_card("123456789012345"))
        self.assertFalse(validate_credit_card("1234-5678-9012-345"))
        self.assertFalse(validate_credit_card("1234 5678 9012 34567"))

class TestTime(unittest.TestCase):
    def test_extract_and_validate_time(self):
        text = "Meeting at 14:30 and lunch at 2:30 PM and invalid 25:61 or 99:99 AM"
        expected = ["14:30", "2:30 PM"]
        self.assertEqual(extract_and_validate_time(text), expected)

    def test_validate_time(self):
        self.assertTrue(validate_time("14:30"))
        self.assertTrue(validate_time("2:30 PM"))
        self.assertFalse(validate_time("25:61"))
        self.assertFalse(validate_time("99:99 AM"))

class TestHTMLTags(unittest.TestCase):
    def test_extract_and_validate_html(self):
        text = "<p>Paragraph</p> <div class=\"example\">Content</div> <img src=\"image.jpg\" alt=\"description\"> plain text"
        expected = ["<p>", "<div class=\"example\">", "<img src=\"image.jpg\" alt=\"description\">"]
        self.assertEqual(extract_and_validate_html(text), expected)

    def test_validate_html(self):
        self.assertTrue(validate_html("<p>"))
        self.assertTrue(validate_html("<div class=\"example\">"))
        self.assertTrue(validate_html("<img src=\"image.jpg\" alt=\"description\">"))
        self.assertFalse(validate_html("plain text"))
        self.assertFalse(validate_html("p>"))

class TestHashtags(unittest.TestCase):
    def test_extract_and_validate_hashtag(self):
        text = "Some hashtags: #example and #ThisIsAHashtag and not-a-hashtag"
        expected = ["#example", "#ThisIsAHashtag"]
        self.assertEqual(extract_and_validate_hashtag(text), expected)

    def test_validate_hashtag(self):
        self.assertTrue(validate_hashtag("#example"))
        self.assertTrue(validate_hashtag("#ThisIsAHashtag"))
        self.assertFalse(validate_hashtag("not-a-hashtag"))
        self.assertFalse(validate_hashtag("#"))

class TestCurrency(unittest.TestCase):
    def test_extract_and_validate_currency(self):
        text = "Prices: $19.99, $1,234.56, $100, and $0.99"
        expected = ["$19.99", "$1,234.56", "$0.99"]
        self.assertEqual(extract_and_validate_currency(text), expected)

    def test_validate_currency(self):
        self.assertTrue(validate_currency("$19.99"))
        self.assertTrue(validate_currency("$1,234.56"))
        self.assertTrue(validate_currency("$0.99"))
        self.assertFalse(validate_currency("$100"))
        self.assertFalse(validate_currency("19.99"))

if __name__ == '__main__':
    unittest.main()