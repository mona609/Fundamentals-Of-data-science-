import numpy as np

# Fuel efficiency (miles per gallon) of 5 car models
fuel_efficiency = np.array([28.5, 32.0, 25.0, 35.5, 30.0])

average = np.mean(fuel_efficiency)
print(f"Average fuel efficiency: {average:.2f} mpg")

# Compare two models: Model 3 (index 2) and Model 4 (index 3)
old_model = fuel_efficiency[2]
new_model = fuel_efficiency[3]

improvement = (new_model - old_model) / old_model * 100
print(f"Model 3 = {old_model} mpg, Model 4 = {new_model} mpg")
print(f"Percentage improvement from Model 3 to Model 4: {improvement:.2f}%")
