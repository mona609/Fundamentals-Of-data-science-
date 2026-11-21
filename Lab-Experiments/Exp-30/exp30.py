import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the dataset
cars = pd.read_csv("cars.csv")
print("Cars in the dataset:", len(cars))

# Inputs for the new car
mileage = float(input("\nEnter the mileage (km): "))
age = int(input("Enter the age of the car (years): "))
brand = input("Enter the brand (Maruti/Honda/Toyota/BMW): ").strip()
engine = input("Enter the engine type (Petrol/Diesel): ").strip()

new_car = pd.DataFrame([[mileage, age, brand, engine]],
                       columns=["mileage", "age", "brand", "engine"])

# One-hot encode the text columns (train and new car together so columns match)
features = cars.drop(columns="price")
all_cars = pd.concat([features, new_car], ignore_index=True)
encoded = pd.get_dummies(all_cars, columns=["brand", "engine"], dtype=int)

X = encoded.iloc[:-1]            # training rows
X_new = encoded.iloc[[-1]]       # the new car
y = cars["price"]

# Train the CART regression tree
model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(X, y)

# Predict the price
predicted_price = model.predict(X_new)[0]
print(f"\nPredicted price of the car: {predicted_price:.2f} lakhs")

# Decision path of the new car
tree = model.tree_
path = model.decision_path(X_new).indices
leaf = model.apply(X_new)[0]

print("\nDecision path:")
for node in path:
    if node == leaf:
        print(f"  Leaf reached -> predicted price = {tree.value[node][0][0]:.2f} lakhs")
        continue
    feature = X.columns[tree.feature[node]]
    threshold = tree.threshold[node]
    value = X_new.iloc[0][feature]
    sign = "<=" if value <= threshold else ">"
    print(f"  {feature} = {value:g}  ({sign} {threshold:.2f})")
