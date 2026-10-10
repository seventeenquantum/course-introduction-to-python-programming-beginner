"""Logic gates working on the integers 0 and 1 (from Week 5, Exercise 2)."""


def AND(a, b):
    return int(a and b)


def OR(a, b):
    return int(a or b)


def NOT(a):
    return int(not a)


def XOR(a, b):
    return int(a != b)


def NAND(a, b):
    return NOT(AND(a, b))


def NOR(a, b):
    return NOT(OR(a, b))
