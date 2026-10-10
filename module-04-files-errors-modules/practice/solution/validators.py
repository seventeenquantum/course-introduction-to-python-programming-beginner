def is_whole_number_in_range(text, low, high):
    if low > high:
        raise ValueError("low must not be greater than high")
    try:
        number = int(text)
    except ValueError:
        return False
    return low <= number <= high


def is_valid_email(text):
    if " " in text or text.count("@") != 1:
        return False
    name, domain = text.split("@")
    return len(name) > 0 and "." in domain


def ask_until_valid(prompt, check):
    while True:
        answer = input(prompt)
        if check(answer):
            return answer
        print("That is not valid. Please try again.")
