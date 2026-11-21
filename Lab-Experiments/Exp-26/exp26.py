import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Columns: area (sq ft), bedrooms, location rating (1-3), price
data = pd.DataFrame([
    [1600, 3, 3, 6001000],
    [2800, 2, 1, 7623000],
    [1450, 2, 2, 4874000],
    [1950, 3, 3, 6777000],
    [1950, 3, 1, 5722000],
    [2100, 1, 3, 6953000],
    [2750, 4, 1, 7990000],
    [2400, 2, 2, 7301000],
    [2350, 3, 1, 6802000],
    [2150, 2, 3, 7199000],
    [1600, 1, 1, 4696000],
    [1700, 3, 3, 6050000],
    [2350, 2, 1, 6726000],
    [2500, 3, 3, 8318000],
    [2750, 2, 1, 7756000],
    [2300, 3, 1, 6713000]
], columns=["area", "bedrooms", "location", "price"])

X = data[["area", "bedrooms", "location"]]
y = data["price"]

# Train the model
model = LinearRegression()
model.fit(X, y)

print("Coefficients:")
for name, coef in zip(X.columns, model.coef_):
    print(f"  {name:9}: {coef:,.2f}")
print(f"Intercept: {model.intercept_:,.2f}")
print(f"R-squared: {r2_score(y, model.predict(X)):.4f}")

# Inputs for the new house
area = float(input("\nEnter the area (sq ft): "))
bedrooms = int(input("Enter the number of bedrooms: "))
location = int(input("Enter the location rating (1-3): "))

new_house = pd.DataFrame([[area, bedrooms, location]], columns=X.columns)
predicted_price = model.predict(new_house)[0]

print(f"\nPredicted price of the new house: {predicted_price:,.0f}")
