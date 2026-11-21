import pandas as pd

data = pd.read_csv("temperature_data.csv")
cities = data.drop(columns="date")

# 1. Mean temperature of each city
mean_temp = cities.mean()

# 2. Standard deviation of each city
std_temp = cities.std()

# 3. Temperature range (highest - lowest) of each city
temp_range = cities.max() - cities.min()

summary = pd.DataFrame({
    "Mean": mean_temp,
    "Std Dev": std_temp,
    "Min": cities.min(),
    "Max": cities.max(),
    "Range": temp_range
}).round(2)

print("Temperature summary of each city (degree Celsius):")
print(summary.to_string())

# 3. City with the highest temperature range
print(f"\nCity with the highest temperature range: {temp_range.idxmax()} ({temp_range.max():.1f})")

# 4. City with the most consistent temperature (lowest standard deviation)
print(f"City with the most consistent temperature: {std_temp.idxmin()} (std = {std_temp.min():.2f})")
