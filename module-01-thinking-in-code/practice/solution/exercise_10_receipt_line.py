name = input("Item: ")
price = float(input("Price: "))
qty = int(input("Quantity: "))
print(f"{name:<10}{qty:>3} x {price:>7.2f} = {price * qty:>8.2f}")
