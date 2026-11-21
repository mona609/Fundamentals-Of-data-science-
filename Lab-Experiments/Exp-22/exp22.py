import pandas as pd
from scipy import stats

reviews = pd.read_csv("customer_reviews.csv")

category = "Electronics"
ratings = reviews.loc[reviews["category"] == category, "rating"]

n = ratings.count()
mean = ratings.mean()
std = ratings.std()
sem = ratings.sem()                 # standard error of the mean

# 95% confidence interval for the true mean rating
low, high = stats.t.interval(0.95, df=n - 1, loc=mean, scale=sem)

# Satisfaction level = percentage of customers who gave 4 or 5
satisfaction = (ratings >= 4).mean() * 100

print(f"Product category : {category}")
print(f"Number of reviews: {n}")
print("\nRating counts:")
print(ratings.value_counts().sort_index().to_string())
print(f"\nAverage rating            : {mean:.3f}")
print(f"Standard deviation        : {std:.3f}")
print(f"95% confidence interval   : ({low:.3f}, {high:.3f})")
print(f"Customer satisfaction     : {satisfaction:.1f}% gave 4 or 5 stars")
