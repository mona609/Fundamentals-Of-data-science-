import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

cars = pd.read_csv("car_prices.csv")

features = ["engine_size", "horsepower", "fuel_efficiency"]
X = cars[features]
y = cars["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# ---------- Model ----------
model = LinearRegression()
model.fit(X_train, y_train)

print("Coefficients (change in price for 1 unit increase):")
for name, coef in zip(features, model.coef_):
    print(f"  {name:16}: {coef:10.2f}")
print(f"  Intercept       : {model.intercept_:10.2f}")

# ---------- Evaluation ----------
y_pred = model.predict(X_test)
print(f"\nR-squared: {r2_score(y_test, y_pred):.4f}")
print(f"MAE      : {mean_absolute_error(y_test, y_pred):,.2f}")
print(f"RMSE     : {np.sqrt(mean_squared_error(y_test, y_pred)):,.2f}")

# ---------- Most influential factors ----------
# Scale the features so that the coefficients can be compared fairly
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
scaled_model = LinearRegression().fit(X_scaled, y)

importance = pd.Series(scaled_model.coef_, index=features)
ranked = importance.abs().sort_values(ascending=False)

print("\nInfluence on price (standardised coefficients):")
for name in ranked.index:
    print(f"  {name:16}: {importance[name]:10.2f}")
print(f"\nMost influential factor: {ranked.index[0]}")

plt.figure(figsize=(6, 4))
plt.bar(importance.index, importance.values, color="steelblue")
plt.title("Influence of Each Feature on Car Price")
plt.ylabel("Standardised coefficient")
plt.show()
