import pandas as pd

posts = pd.DataFrame({
    "post_id": range(1, 16),
    "likes": [10, 25, 10, 40, 25, 10, 55, 40, 25, 10, 70, 55, 25, 40, 10]
})

# How many posts received each number of likes
likes_frequency = posts["likes"].value_counts().sort_index()

print("Frequency distribution of likes:")
print("Likes  Posts")
for likes, count in likes_frequency.items():
    print(f"{likes:5}  {count:5}")
