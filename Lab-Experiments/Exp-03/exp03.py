import numpy as np

# Columns: bedrooms, square footage, sale price
house_data = np.array([
    [3, 1500, 250000],
    [5, 2800, 520000],
    [4, 2000, 340000],
    [6, 3500, 690000],
    [2,  900, 150000],
    [5, 3000, 560000],
    [3, 1400, 230000],
    [7, 4000, 810000],
    [4, 2200, 360000],
    [5, 2600, 480000]
])
# To read from a CSV file instead:
# house_data = np.genfromtxt("house_data.csv", delimiter=",", skip_header=1)

bedrooms = house_data[:, 0]
price = house_data[:, 2]

# True only for houses with more than 4 bedrooms
mask = bedrooms > 4

print("Houses with more than 4 bedrooms:", np.sum(mask))
print("Their prices:", price[mask])
print(f"Average sale price: {price[mask].mean():.2f}")
