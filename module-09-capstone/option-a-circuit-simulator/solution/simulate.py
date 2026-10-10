from itertools import product

from adders import from_bits, full_adder, half_adder, ripple_adder, to_bits


def show_half_adder():
    print("A B | Sum Carry")
    for a, b in product([0, 1], repeat=2):
        s, c = half_adder(a, b)
        print(f"{a} {b} |  {s}    {c}")


def show_full_adder():
    print("A B Cin | Sum Cout")
    for a, b, cin in product([0, 1], repeat=3):
        s, c = full_adder(a, b, cin)
        print(f"{a} {b}  {cin}  |  {s}    {c}")


def add_two_numbers():
    try:
        x = int(input("First number (0 to 15): "))
        y = int(input("Second number (0 to 15): "))
        sum_bits, carry = ripple_adder(to_bits(x), to_bits(y))
    except ValueError:
        print("Please enter whole numbers from 0 to 15.")
        return
    result_bits = "".join(str(b) for b in reversed(sum_bits))
    print(f"{x:04b} + {y:04b} = {carry}{result_bits}")
    print(f"{x} + {y} = {from_bits(sum_bits) + 16 * carry}")


if __name__ == "__main__":
    show_half_adder()
    print()
    show_full_adder()
    print()
    add_two_numbers()
