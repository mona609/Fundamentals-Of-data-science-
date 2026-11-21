import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Features: body temperature (C), cough score (0-10), fatigue score (0-10)
X = np.array([
    [36.6, 1, 2],
    [37.0, 2, 3],
    [36.8, 0, 1],
    [37.2, 3, 4],
    [36.5, 1, 3],
    [37.1, 4, 2],
    [36.9, 2, 2],
    [37.3, 3, 3],
    [36.7, 0, 2],
    [37.0, 1, 4],
    [38.5, 7, 8],
    [39.0, 8, 7],
    [38.2, 6, 7],
    [39.4, 9, 9],
    [38.8, 7, 6],
    [38.0, 5, 7],
    [39.1, 8, 8],
    [38.6, 6, 8],
    [39.5, 9, 7],
    [38.3, 7, 9]
])
# Labels: 0 = no condition, 1 = has the condition
y = np.array([0] * 10 + [1] * 10)

# Inputs for the new patient
temperature = float(input("Enter body temperature (C): "))
cough = float(input("Enter cough score (0-10): "))
fatigue = float(input("Enter fatigue score (0-10): "))
k = int(input("Enter the value of k: "))

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the KNN model
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_scaled, y)

# Predict for the new patient
new_patient = scaler.transform([[temperature, cough, fatigue]])
prediction = model.predict(new_patient)[0]
probability = model.predict_proba(new_patient)[0]

print(f"\nProbability of no condition: {probability[0]:.2f}")
print(f"Probability of condition   : {probability[1]:.2f}")
if prediction == 1:
    print("Prediction: the patient HAS the medical condition (1).")
else:
    print("Prediction: the patient does NOT have the medical condition (0).")
