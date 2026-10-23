import pandas as pd

order_data = pd.DataFrame({
    "customer_id": [101, 102, 101, 103, 102, 104, 101, 103, 105, 104],
    "order_date": ["2024-01-05", "2024-01-07", "2024-01-10", "2024-01-12", "2024-01-15",
                   "2024-01-18", "2024-01-20", "2024-01-22", "2024-01-25", "2024-01-28"],
    "product_name": ["Laptop", "Mouse", "Mouse", "Keyboard", "Laptop",
                     "Mouse", "Keyboard", "Mouse", "Laptop", "Keyboard"],
    "quantity": [1, 3, 2, 4, 2, 5, 3, 1, 1, 2]
})

order_data["order_date"] = pd.to_datetime(order_data["order_date"])

# 1. Total number of orders by each customer
orders_per_customer = order_data.groupby("customer_id").size()
print("Total orders per customer:")
print(orders_per_customer)

# 2. Average order quantity for each product
avg_quantity = order_data.groupby("product_name")["quantity"].mean()
print("\nAverage order quantity per product:")
print(avg_quantity.round(2))

# 3. Earliest and latest order dates
print("\nEarliest order date:", order_data["order_date"].min().date())
print("Latest order date  :", order_data["order_date"].max().date())
