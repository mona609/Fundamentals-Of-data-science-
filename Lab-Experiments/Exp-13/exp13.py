import re
from collections import Counter

# Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

# Lowercase and keep only the words (removes punctuation)
words = re.findall(r"[a-z']+", text.lower())

# Count the frequency of every word
frequency = Counter(words)

print("Total words:", len(words))
print("Unique words:", len(frequency))
print("\nWord frequency distribution:")
for word, count in frequency.most_common():
    print(f"{word:12} {count}")
