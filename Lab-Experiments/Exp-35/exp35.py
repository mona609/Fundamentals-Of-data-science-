import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

customers = pd.read_csv("retail_customers.csv")
features = ["total_spent", "visit_frequency"]

# Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(customers[features])

# K-Means with 3 clusters
model = KMeans(n_clusters=3, n_init=10, random_state=42)
customers["cluster"] = model.fit_predict(X)

# Average of each cluster
summary = customers.groupby("cluster").agg(
    customers=("customer_id", "count"),
    avg_spent=("total_spent", "mean"),
    avg_visits=("visit_frequency", "mean")
).round(1)

# Name the clusters by average spending (lowest to highest)
order = summary["avg_spent"].sort_values().index
names = dict(zip(order, ["Low spenders", "Medium spenders", "High spenders"]))
summary["segment"] = summary.index.map(names)

print("Customer segments:")
print(summary.to_string())

# Plot
centers = scaler.inverse_transform(model.cluster_centers_)
plt.figure(figsize=(7, 5))
plt.scatter(customers["total_spent"], customers["visit_frequency"],
            c=customers["cluster"], cmap="viridis", s=60)
plt.scatter(centers[:, 0], centers[:, 1], c="red", marker="X", s=200, label="Cluster centres")
plt.title("Customer Segments by Spending Pattern")
plt.xlabel("Total amount spent")
plt.ylabel("Visits per month")
plt.legend()
plt.show()
