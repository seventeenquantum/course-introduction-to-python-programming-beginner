from text_cleaner import clean_whitespace, find_emails, mask_phone_numbers

SAMPLE = "  Contact   ada@example.com\tor call 555-123-4567.\n\nAlso   grace.h@navy.mil  "


def test_clean_whitespace():
    assert (
        clean_whitespace(SAMPLE)
        == "Contact ada@example.com or call 555-123-4567. Also grace.h@navy.mil"
    )


def test_find_emails():
    assert find_emails(SAMPLE) == ["ada@example.com", "grace.h@navy.mil"]


def test_mask_phone_numbers():
    assert "XXX-XXX-XXXX" in mask_phone_numbers(SAMPLE)
    assert "555-123-4567" not in mask_phone_numbers(SAMPLE)
