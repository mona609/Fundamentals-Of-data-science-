import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("houses.csv")

# ---------- Bivariate analysis ----------
correlation = data["size_sqft"].corr(data["price"])
print(f"Correlation between size and price: {correlation:.3f}")

# ---------- Regression model ----------
X = data[["size_sqft"]]
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nPrice = {model.coef_[0]:.2f} x size + {model.intercept_:,.2f}")

# ---------- Evaluation ----------
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Absolute Error (MAE): {mae:,.2f}")
print(f"Mean Squared Error (MSE) : {mse:,.2f}")
print(f"Root Mean Squared Error  : {rmse:,.2f}")
print(f"R-squared (R2)           : {r2:.4f}")

# ---------- Plot ----------
plt.figure(figsize=(7, 5))
plt.scatter(X_test, y_test, color="blue", label="Actual prices (test data)")
plt.plot(X_test.sort_values("size_sqft"),
         model.predict(X_test.sort_values("size_sqft")),
         color="red", label="Regression line")
plt.title("House Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price")
plt.legend()
plt.show()
