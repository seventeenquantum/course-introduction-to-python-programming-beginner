counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_lines = []

try:
    with open("server.log") as f:
        for line in f:
            parts = line.strip().split(" ", 3)
            if len(parts) < 4:
                continue
            level = parts[2]
            if level in counts:
                counts[level] += 1
            if level == "ERROR":
                error_lines.append(line.strip())
except FileNotFoundError:
    print("server.log was not found. Check the file name and folder.")
else:
    for level, number in counts.items():
        print(f"{level}: {number}")
    print("\nErrors:")
    for line in error_lines:
        print(line)
