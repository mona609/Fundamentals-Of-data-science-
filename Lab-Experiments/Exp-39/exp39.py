import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

transactions = pd.read_csv("transactions.csv")
print("Number of transactions:", len(transactions))

# Combine the transactions of each customer (average per transaction)
customers = transactions.groupby("customer_id").agg(
    total_spent=("total_spent", "mean"),
    items_purchased=("items_purchased", "mean")
).reset_index()
print("Number of customers   :", len(customers))

# Scale and cluster
features = ["total_spent", "items_purchased"]
scaler = StandardScaler()
X = scaler.fit_transform(customers[features])

model = KMeans(n_clusters=3, n_init=10, random_state=42)
customers["cluster"] = model.fit_predict(X)

summary = customers.groupby("cluster").agg(
    customers=("customer_id", "count"),
    avg_spent=("total_spent", "mean"),
    avg_items=("items_purchased", "mean")
).round(1)
print("\nCluster summary:")
print(summary.to_string())

# ---------- Visualisation ----------
centers = scaler.inverse_transform(model.cluster_centers_)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].scatter(customers["total_spent"], customers["items_purchased"],
                c=customers["cluster"], cmap="viridis", s=60)
axes[0].scatter(centers[:, 0], centers[:, 1], c="red", marker="X", s=200, label="Cluster centres")
axes[0].set_title("Customer Clusters")
axes[0].set_xlabel("Average amount spent per transaction")
axes[0].set_ylabel("Average items per transaction")
axes[0].legend()

axes[1].bar(summary.index.astype(str), summary["avg_spent"], color=["#440154", "#21918c", "#fde725"])
axes[1].set_title("Average Spending of Each Cluster")
axes[1].set_xlabel("Cluster")
axes[1].set_ylabel("Average amount spent")

plt.tight_layout()
plt.show()
