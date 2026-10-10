"""Adders built only from logic gates (starter). No + operator for the adding!

half adder: sum = XOR of the inputs, carry = AND of the inputs.
full adder: built from two half adders and an OR.

Numbers become lists of bits, LEAST significant bit first: 6 is [0, 1, 1, 0].
Two new tools: (number >> i) & 1 reads bit i of a number, and zip(a, b)
walks through two lists in step.

Run `pytest` to check your work. It tests every possible pair of 4-bit inputs.
"""

from gates import AND, OR, XOR


def half_adder(a, b):
    """Add two bits. Return (sum_bit, carry_out)."""
    # TODO
    pass


def full_adder(a, b, carry_in):
    """Add two bits and a carry. Return (sum_bit, carry_out)."""
    # TODO
    pass


def to_bits(number, width=4):
    """Return a list of bits, least significant first: 6 -> [0, 1, 1, 0].

    Raise ValueError if the number does not fit in `width` bits.
    """
    # TODO
    pass


def from_bits(bits):
    """Turn a list of bits (least significant first) back into a number."""
    # TODO
    pass


def ripple_adder(a_bits, b_bits):
    """Add two equal-length bit lists. Return (sum_bits, carry_out).

    The carry out of each column becomes the carry in of the next.
    Raise ValueError if the lists have different lengths.
    """
    # TODO
    pass
