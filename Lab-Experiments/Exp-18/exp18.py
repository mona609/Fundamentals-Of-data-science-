import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "age": [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    "fat": [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
            34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
})

# 1. Mean, median and standard deviation
print("            age     %fat")
print(f"Mean     {data['age'].mean():7.2f}  {data['fat'].mean():7.2f}")
print(f"Median   {data['age'].median():7.2f}  {data['fat'].median():7.2f}")
print(f"Std dev  {data['age'].std():7.2f}  {data['fat'].std():7.2f}")

# 2. Boxplots
plt.figure(figsize=(6, 4))
plt.boxplot([data["age"], data["fat"]])
plt.xticks([1, 2], ["Age", "%Fat"])
plt.title("Boxplots of Age and %Fat")
plt.show()

# 3. Scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(data["age"], data["fat"], color="red")
plt.title("Scatter Plot: Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.show()

# 4. Q-Q plot (sorted values of one variable against the other)
age_sorted = np.sort(data["age"])
fat_sorted = np.sort(data["fat"])

plt.figure(figsize=(6, 4))
plt.scatter(age_sorted, fat_sorted, color="green")
low = min(age_sorted.min(), fat_sorted.min())
high = max(age_sorted.max(), fat_sorted.max())
plt.plot([low, high], [low, high], "k--")        # reference line y = x
plt.title("Q-Q Plot: Age vs %Fat")
plt.xlabel("Age quantiles")
plt.ylabel("%Fat quantiles")
plt.show()
