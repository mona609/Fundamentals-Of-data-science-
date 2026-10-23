import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Common words that carry little meaning
stop_words = {"the", "and", "is", "a", "an", "to", "of", "in", "it", "i", "was",
              "for", "on", "my", "this", "that", "with", "are", "but", "very",
              "be", "at", "as", "so", "we", "you", "have", "has", "had", "not"}

# 1. Load the dataset
data = pd.read_csv("data.csv")

# 2. Preprocess: lowercase, remove punctuation, remove stop words
all_words = []
for comment in data["feedback"]:
    comment = comment.lower()
    comment = re.sub(r"[^a-z\s]", "", comment)      # remove punctuation
    for word in comment.split():
        if word not in stop_words:
            all_words.append(word)

# 3. Frequency distribution
frequency = Counter(all_words)

# 4. Top N words
n = int(input("Enter the number of top words (N): "))
top_n = frequency.most_common(n)

print(f"\nTop {n} most frequent words:")
for word, count in top_n:
    print(f"{word:12} {count}")

# 5. Bar graph
words = [w for w, c in top_n]
counts = [c for w, c in top_n]

plt.figure(figsize=(8, 4))
plt.bar(words, counts, color="teal")
plt.title(f"Top {n} Most Frequent Words in Customer Feedback")
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.show()
