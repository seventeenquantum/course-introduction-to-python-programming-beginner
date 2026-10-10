from itertools import product


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


def print_truth_table(name, gate, inputs=2):
    header = " ".join("ABC"[:inputs]) + " | " + name
    print(header)
    print("-" * len(header))
    for values in product([0, 1], repeat=inputs):
        print(" ".join(str(v) for v in values), "|", gate(*values))
    print()


# Bonus: NAND is universal, so every other gate can be built from it.
def not_from_nand(a):
    return NAND(a, a)


def and_from_nand(a, b):
    return NAND(NAND(a, b), NAND(a, b))


def or_from_nand(a, b):
    return NAND(NAND(a, a), NAND(b, b))


if __name__ == "__main__":
    for gate_name, gate in [
        ("AND", AND),
        ("OR", OR),
        ("XOR", XOR),
        ("NAND", NAND),
        ("NOR", NOR),
    ]:
        print_truth_table(gate_name, gate)
    print_truth_table("NOT", NOT, inputs=1)

    for a, b in product([0, 1], repeat=2):
        assert not_from_nand(a) == NOT(a)
        assert and_from_nand(a, b) == AND(a, b)
        assert or_from_nand(a, b) == OR(a, b)
    print("NAND can build NOT, AND and OR.")
