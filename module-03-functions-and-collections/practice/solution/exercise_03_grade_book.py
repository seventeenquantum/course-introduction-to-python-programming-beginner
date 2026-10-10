grades = {
    "Ada": [92, 88, 95],
    "Ben": [70, 65, 80],
    "Cleo": [55, 62, 48],
}


def average(scores):
    return sum(scores) / len(scores)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    return "F"


averages = {}
for name, scores in grades.items():
    averages[name] = average(scores)
    print(f"{name:<6}{averages[name]:>7.2f}  {letter_grade(averages[name])}")

class_average = sum(averages.values()) / len(averages)
top = max(averages, key=averages.get)
print(f"Class average: {class_average:.2f}")
print(f"Top student: {top}")
