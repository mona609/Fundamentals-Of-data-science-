import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

customers = pd.read_csv("customers.csv")
features = ["age", "annual_spend", "orders_per_year", "session_minutes"]

# Scale the features
X = StandardScaler().fit_transform(customers[features])

# Try different numbers of clusters
ks = range(2, 7)
inertias = []
scores = []
print("k   inertia   silhouette")
for k in ks:
    model = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    inertias.append(model.inertia_)
    scores.append(silhouette_score(X, model.labels_))
    print(f"{k}   {model.inertia_:7.2f}   {scores[-1]:.3f}")

# Best k = highest silhouette score
best_k = list(ks)[scores.index(max(scores))]
print("\nBest number of clusters:", best_k)

final = KMeans(n_clusters=best_k, n_init=10, random_state=42).fit(X)
customers["segment"] = final.labels_

print("\nCustomers in each segment:")
print(customers["segment"].value_counts().sort_index().to_string())

print("\nAverage values of each segment:")
print(customers.groupby("segment")[features].mean().round(1).to_string())

# Plots
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].plot(list(ks), inertias, marker="o")
axes[0].set_title("Elbow Method")
axes[0].set_xlabel("Number of clusters (k)")
axes[0].set_ylabel("Inertia")

axes[1].scatter(customers["annual_spend"], customers["orders_per_year"],
                c=customers["segment"], cmap="viridis", s=50)
axes[1].set_title("Customer Segments")
axes[1].set_xlabel("Annual spend")
axes[1].set_ylabel("Orders per year")

plt.tight_layout()
plt.show()
