import numpy as np

# Sales of Q1, Q2, Q3, Q4
sales_data = np.array([120000, 135000, 150000, 170000])

total_sales = np.sum(sales_data)

q1 = sales_data[0]
q4 = sales_data[3]
percent_increase = (q4 - q1) / q1 * 100

print("Total sales for the year:", total_sales)
print(f"Percentage increase from Q1 to Q4: {percent_increase:.2f}%")
