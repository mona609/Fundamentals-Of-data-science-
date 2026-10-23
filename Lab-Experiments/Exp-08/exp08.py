import pandas as pd

sales_data = pd.DataFrame({
    "product": ["Phone", "Laptop", "Earbuds", "Charger", "Phone", "Watch", "Laptop",
                "Speaker", "Earbuds", "Camera", "Phone", "Charger", "Watch", "Earbuds"],
    "units_sold": [12, 5, 20, 15, 8, 6, 7, 4, 18, 3, 10, 9, 5, 14]
})

# Total units sold of every product
total_sold = sales_data.groupby("product")["units_sold"].sum()

# 5 products with the highest total
top5 = total_sold.nlargest(5)

print("Top 5 products sold in the past month:")
print(top5)
