sentence = input("Sentence: ").lower()
for mark in ".,!?;:":
    sentence = sentence.replace(mark, "")

words = sentence.split()
if not words:
    print("No words entered.")
else:
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    most_common = max(counts, key=counts.get)
    print(f"Words: {len(words)}")
    print(f"Unique words: {len(counts)}")
    print(f"Most common: {most_common} ({counts[most_common]})")
