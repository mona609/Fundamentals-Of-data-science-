import numpy as np

# Each row = one product, each column = price of one sale
sales = np.array([
    [250, 300, 275],
    [1200, 1150, 1250],
    [80, 95, 90]
])

print("Sales matrix:")
print(sales)

# Average price of each product (row-wise)
per_product = np.mean(sales, axis=1)
for i, avg in enumerate(per_product, start=1):
    print(f"Average price of product {i}: {avg:.2f}")

# Average price of all products sold
overall = np.mean(sales)
print(f"Average price of all products sold: {overall:.2f}")
