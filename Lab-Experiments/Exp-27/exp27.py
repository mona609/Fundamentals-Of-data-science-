import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Columns: monthly usage minutes, contract months, support calls, churn (0/1)
data = pd.DataFrame([
    [110, 1, 8, 1],
    [120, 3, 1, 1],
    [100, 6, 1, 1],
    [540, 12, 3, 0],
    [350, 1, 5, 1],
    [310, 24, 7, 0],
    [190, 6, 7, 1],
    [130, 6, 0, 0],
    [190, 12, 5, 1],
    [370, 24, 1, 0],
    [110, 1, 7, 1],
    [410, 1, 2, 1],
    [400, 24, 3, 0],
    [380, 3, 6, 1],
    [440, 24, 7, 0],
    [590, 24, 4, 0],
    [210, 1, 2, 1],
    [240, 12, 2, 0],
    [430, 24, 0, 0],
    [330, 6, 5, 1],
    [250, 12, 7, 1],
    [340, 6, 3, 1],
    [510, 1, 2, 1],
    [400, 3, 4, 1]
], columns=["usage", "contract", "calls", "churn"])

X = data[["usage", "contract", "calls"]]
y = data["churn"]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_scaled, y)
print(f"Training accuracy: {model.score(X_scaled, y) * 100:.1f}%\n")

# Inputs for the new customer
usage = float(input("Enter monthly usage minutes: "))
contract = float(input("Enter contract duration (months): "))
calls = float(input("Enter number of customer support calls: "))

new_customer = scaler.transform(pd.DataFrame([[usage, contract, calls]], columns=X.columns))
prediction = model.predict(new_customer)[0]
probability = model.predict_proba(new_customer)[0][1]

print(f"\nProbability of churn: {probability:.2f}")
if prediction == 1:
    print("Prediction: the customer will CHURN (1).")
else:
    print("Prediction: the customer will NOT churn (0).")
