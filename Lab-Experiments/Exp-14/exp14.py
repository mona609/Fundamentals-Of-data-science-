import pandas as pd

customers = pd.DataFrame({
    "customer_id": range(1, 16),
    "age": [23, 25, 31, 23, 40, 25, 35, 31, 23, 28, 40, 35, 25, 31, 28],
    "purchase_amount": [450, 320, 800, 150, 1200, 275, 640, 510, 90, 330, 980, 420, 260, 700, 380]
})

# Frequency of each age
age_frequency = customers["age"].value_counts().sort_index()

print("Frequency distribution of customer ages:")
print(age_frequency.to_string())
