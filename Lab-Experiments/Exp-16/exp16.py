import re
import pandas as pd
from collections import Counter

reviews = pd.DataFrame({
    "review": [
        "Great product, works very well!",
        "The quality is great and the delivery was fast.",
        "Not good. The battery life is very poor.",
        "Excellent value for money, I love it.",
        "The product stopped working after a week.",
        "Fast delivery and great packaging.",
        "Very good quality, works well and looks great.",
        "Poor quality, I want a refund."
    ]
})

# Join all reviews, lowercase, and extract the words
all_text = " ".join(reviews["review"]).lower()
words = re.findall(r"[a-z']+", all_text)

frequency = Counter(words)

print("Top 10 most frequent words:")
for word, count in frequency.most_common(10):
    print(f"{word:10} {count}")
