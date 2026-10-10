from gates import AND, OR, XOR


def half_adder(a, b):
    """Add two bits. Return (sum_bit, carry_out)."""
    return XOR(a, b), AND(a, b)


def full_adder(a, b, carry_in):
    """Add two bits and a carry. Return (sum_bit, carry_out)."""
    sum1, carry1 = half_adder(a, b)
    sum_bit, carry2 = half_adder(sum1, carry_in)
    return sum_bit, OR(carry1, carry2)


def to_bits(number, width=4):
    """Return a list of bits, least significant first: 6 -> [0, 1, 1, 0]."""
    if not 0 <= number < 2 ** width:
        raise ValueError(f"number must fit in {width} bits")
    return [(number >> i) & 1 for i in range(width)]


def from_bits(bits):
    """Turn a list of bits (least significant first) back into a number."""
    return sum(bit << i for i, bit in enumerate(bits))


def ripple_adder(a_bits, b_bits):
    """Add two equal-length bit lists. Return (sum_bits, carry_out)."""
    if len(a_bits) != len(b_bits):
        raise ValueError("inputs must be the same length")
    carry = 0
    sum_bits = []
    for a, b in zip(a_bits, b_bits):
        s, carry = full_adder(a, b, carry)
        sum_bits.append(s)
    return sum_bits, carry
