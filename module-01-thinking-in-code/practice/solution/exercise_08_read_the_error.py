# The crash was: TypeError: can only concatenate str (not "int") to str.
# input() returns text, and you cannot add a number to text.
# The fix is to convert the age with int() and use an f-string.
name = input("Name: ")
age = int(input("Age: "))
print(f"Next year {name} will be {age + 1}")
