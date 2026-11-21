import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Columns: annual income (in thousands), spending score (1-100)
X = np.array([
    [27, 32],
    [24, 13],
    [25, 31],
    [27, 18],
    [21, 16],
    [26, 3],
    [22, 8],
    [26, 29],
    [57, 48],
    [57, 53],
    [60, 45],
    [59, 51],
    [64, 55],
    [56, 53],
    [61, 48],
    [57, 50],
    [90, 95],
    [77, 92],
    [82, 88],
    [85, 90],
    [83, 89],
    [87, 80],
    [90, 86],
    [81, 92]
])

# Scale and cluster
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = model.fit_predict(X_scaled)

# Cluster centres in the original units
centers = scaler.inverse_transform(model.cluster_centers_)
print("Existing customer segments:")
for i, c in enumerate(centers):
    print(f"  Segment {i}: income = {c[0]:.1f}, spending score = {c[1]:.1f}, customers = {np.sum(labels == i)}")

# Inputs for the new customer
income = float(input("\nEnter the annual income (in thousands): "))
score = float(input("Enter the spending score (1-100): "))

new_customer = np.array([[income, score]])
segment = model.predict(scaler.transform(new_customer))[0]
print(f"\nThe new customer belongs to Segment {segment}.")

# Plot
plt.figure(figsize=(7, 5))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=60)
plt.scatter(centers[:, 0], centers[:, 1], c="red", marker="X", s=200, label="Cluster centres")
plt.scatter(income, score, c="black", marker="*", s=300, label="New customer")
plt.title("Customer Segments (K-Means)")
plt.xlabel("Annual income (thousands)")
plt.ylabel("Spending score")
plt.legend()
plt.show()
