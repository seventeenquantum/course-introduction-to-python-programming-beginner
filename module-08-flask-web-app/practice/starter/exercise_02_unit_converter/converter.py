"""Exercise 2: Unit converter (starter): the maths.

convert(value, from_unit, to_unit) for km, miles, kg, pounds, c, f.
Expected: 10 km -> miles is about 6.21; 1 kg -> pounds is about 2.20;
100 c -> f is 212.0; km -> kg raises ValueError.

Hint: store length and mass factors in dictionaries relative to a base unit.
Temperature is a special case because it needs an offset, not just a multiplier.
Run `pytest` to check.
"""

LENGTH = {"km": 1.0, "miles": 1.609344}  # kilometres per unit
MASS = {"kg": 1.0, "pounds": 0.45359237}  # kilograms per unit
TEMPERATURE = {"c", "f"}
UNITS = list(LENGTH) + list(MASS) + sorted(TEMPERATURE)


def convert(value, from_unit, to_unit):
    # TODO: raise ValueError for unknown units or incompatible conversions
    pass
