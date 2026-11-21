import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

patients = pd.read_csv("patients.csv")

# Convert gender to numbers
patients["gender"] = patients["gender"].map({"M": 1, "F": 0})

X = patients[["age", "gender", "blood_pressure", "cholesterol"]]
y = patients["outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# Predict on the test set
y_pred = model.predict(X_test_scaled)

results = X_test.copy()
results["actual"] = y_test
results["predicted"] = y_pred
print("Test set results:")
print(results.to_string())

# Evaluation (Good is treated as the positive class)
print("\nModel performance:")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label='Good'):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred, pos_label='Good'):.4f}")
print(f"F1-score : {f1_score(y_test, y_pred, pos_label='Good'):.4f}")
