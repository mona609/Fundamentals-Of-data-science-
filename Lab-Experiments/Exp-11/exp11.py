import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 31)

np.random.seed(1)
sales = np.random.randint(20, 80, size=30)   # daily sales of the product

# 1. Line plot
plt.figure(figsize=(8, 4))
plt.plot(days, sales, color="green")
plt.title("Daily Sales - Line Plot")
plt.xlabel("Day of the month")
plt.ylabel("Units sold")
plt.grid(True)
plt.show()

# 2. Scatter plot
plt.figure(figsize=(8, 4))
plt.scatter(days, sales, color="red")
plt.title("Daily Sales - Scatter Plot")
plt.xlabel("Day of the month")
plt.ylabel("Units sold")
plt.show()

# 3. Bar plot
plt.figure(figsize=(8, 4))
plt.bar(days, sales, color="purple")
plt.title("Daily Sales - Bar Plot")
plt.xlabel("Day of the month")
plt.ylabel("Units sold")
plt.show()
