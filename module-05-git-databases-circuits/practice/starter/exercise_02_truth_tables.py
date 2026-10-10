"""Exercise 2: Truth tables for all the gates.

Write AND, OR, NOT, XOR, NAND and NOR working on the numbers 0 and 1.
Then write print_truth_table(name, gate, inputs=2) that prints a table for
any gate, using itertools.product to generate every input combination.

Expected output for AND:
  A B | AND
  ---------
  0 0 | 0
  0 1 | 0
  1 0 | 0
  1 1 | 1

Hints: product([0, 1], repeat=2) gives (0,0), (0,1), (1,0), (1,1).
Call a gate with gate(*values) to unpack the tuple into arguments.

Bonus: NAND is "universal". Build NOT, AND and OR using only NAND,
and use assert to check them against the real gates.
"""

from itertools import product


def AND(a, b):
    # TODO
    pass


def OR(a, b):
    # TODO
    pass


def NOT(a):
    # TODO
    pass


def XOR(a, b):
    # TODO
    pass


def NAND(a, b):
    # TODO
    pass


def NOR(a, b):
    # TODO
    pass


def print_truth_table(name, gate, inputs=2):
    # TODO
    pass
