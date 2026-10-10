"""Exercise 3: Input validator module (starter).

Email rule: no spaces, exactly one @, at least one character before it,
and a "." somewhere after it.
Hint: text.isdigit() is False for negative numbers, so use try: int(text).
"""


def is_whole_number_in_range(text, low, high):
    """True if text is a whole number from low to high (inclusive).

    Raise ValueError if low is greater than high.
    """
    # TODO
    pass


def is_valid_email(text):
    """True if text looks like an email address by the rule above."""
    # TODO
    pass


def ask_until_valid(prompt, check):
    """Keep asking until check(answer) is true, then return the answer."""
    # TODO
    pass
