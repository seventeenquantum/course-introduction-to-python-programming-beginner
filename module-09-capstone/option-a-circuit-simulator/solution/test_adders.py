from itertools import product

from adders import from_bits, full_adder, half_adder, ripple_adder, to_bits


def test_half_adder():
    assert half_adder(0, 0) == (0, 0)
    assert half_adder(0, 1) == (1, 0)
    assert half_adder(1, 0) == (1, 0)
    assert half_adder(1, 1) == (0, 1)


def test_full_adder_matches_arithmetic():
    for a, b, c in product([0, 1], repeat=3):
        s, carry = full_adder(a, b, c)
        assert 2 * carry + s == a + b + c


def test_to_and_from_bits():
    assert to_bits(6) == [0, 1, 1, 0]
    assert from_bits([0, 1, 1, 0]) == 6


def test_ripple_adder_every_pair():
    for x in range(16):
        for y in range(16):
            sum_bits, carry = ripple_adder(to_bits(x), to_bits(y))
            assert from_bits(sum_bits) + 16 * carry == x + y


def test_overflow_sets_the_carry():
    sum_bits, carry = ripple_adder(to_bits(15), to_bits(1))
    assert sum_bits == [0, 0, 0, 0]
    assert carry == 1
