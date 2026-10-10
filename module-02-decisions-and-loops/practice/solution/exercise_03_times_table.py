n = int(input("Which table? "))
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")

print()
for row in range(1, 10):
    for col in range(1, 10):
        print(row * col, end="\t")
    print()
