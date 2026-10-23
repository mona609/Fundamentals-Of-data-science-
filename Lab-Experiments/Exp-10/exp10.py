import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [25000, 27000, 31000, 29000, 35000, 38000,
         36000, 40000, 42000, 45000, 50000, 55000]

# 1. Line plot
plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker="o", color="blue")
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar plot
plt.figure(figsize=(8, 4))
plt.bar(months, sales, color="orange")
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
