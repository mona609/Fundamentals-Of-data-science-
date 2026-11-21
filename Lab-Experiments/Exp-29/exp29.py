import textwrap
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix)

# Load the dataset as a DataFrame
data = load_breast_cancer(as_frame=True).frame

print("Available columns:")
print(textwrap.fill(", ".join(data.columns), width=70))

# Names given by the user
feature_names = input("\nEnter the feature names (separated by commas): ")
features = [name.strip() for name in feature_names.split(",")]
target = input("Enter the target variable name: ").strip()

X = data[features]
y = data[target]

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model = make_pipeline(StandardScaler(), LogisticRegression())
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

print("\nEvaluation on the test data:")
print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1-score : {f1_score(y_test, y_pred):.4f}")
print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))
