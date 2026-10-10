password = input("Password: ")

has_digit = False
has_upper = False
has_lower = False
for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True

score = 0
if len(password) >= 8:
    score += 1
if has_digit:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1

if score <= 2:
    print("Weak")
elif score == 3:
    print("Medium")
else:
    print("Strong")
