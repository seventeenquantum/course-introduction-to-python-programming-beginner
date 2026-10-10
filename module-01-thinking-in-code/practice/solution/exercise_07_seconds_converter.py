total = int(input("Seconds: "))
hours = total // 3600
remainder = total % 3600
minutes = remainder // 60
seconds = remainder % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
