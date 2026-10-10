import re


def clean_whitespace(text):
    return re.sub(r"\s+", " ", text).strip()


def find_emails(text):
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)


def mask_phone_numbers(text):
    return re.sub(r"\b\d{3}-\d{3}-\d{4}\b", "XXX-XXX-XXXX", text)


if __name__ == "__main__":
    sample = "  Contact   ada@example.com\tor call 555-123-4567.\n\nAlso   grace.h@navy.mil  "
    print(clean_whitespace(sample))
    print(find_emails(sample))
    print(mask_phone_numbers(sample))

# Limitation to discuss: this email pattern would include a full stop at the end
# of a sentence if one followed the address. Real email matching is harder than it looks.
