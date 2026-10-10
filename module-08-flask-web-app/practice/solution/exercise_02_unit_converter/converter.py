LENGTH = {"km": 1.0, "miles": 1.609344}  # kilometres per unit
MASS = {"kg": 1.0, "pounds": 0.45359237}  # kilograms per unit
TEMPERATURE = {"c", "f"}
UNITS = list(LENGTH) + list(MASS) + sorted(TEMPERATURE)


def convert(value, from_unit, to_unit):
    if from_unit not in UNITS or to_unit not in UNITS:
        raise ValueError("Unknown unit.")
    if from_unit == to_unit:
        return value
    if from_unit in LENGTH and to_unit in LENGTH:
        return value * LENGTH[from_unit] / LENGTH[to_unit]
    if from_unit in MASS and to_unit in MASS:
        return value * MASS[from_unit] / MASS[to_unit]
    if from_unit == "c" and to_unit == "f":
        return value * 9 / 5 + 32
    if from_unit == "f" and to_unit == "c":
        return (value - 32) * 5 / 9
    raise ValueError(f"Cannot convert {from_unit} to {to_unit}.")
