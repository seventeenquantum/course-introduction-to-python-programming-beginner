# Option A: Logic circuit simulator (recommended)

Build a half adder, a full adder and a 4-bit ripple adder from nothing but logic
gate functions, print their truth tables, and add two numbers from 0 to 15 by
running the bits through your circuit. No `+` operator does the adding.

- `starter/` has the gates, stubs with hints, and a complete test file
- `solution/` is the worked version

```text
cd starter
pip install pytest
pytest            # fails until you finish adders.py
python simulate.py
```

Keep this repository. In Course 2, Week 4, you rebuild the same adder with quantum
gates and compare it against your Python version.

Stretch goals: 8-bit width, a subtractor with two's complement, counting gate calls
as the width grows, an ASCII drawing of the full adder in your README.
