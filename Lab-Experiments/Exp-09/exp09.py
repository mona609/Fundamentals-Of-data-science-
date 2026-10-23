import pandas as pd

property_data = pd.DataFrame({
    "property_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "location": ["Adyar", "T Nagar", "Adyar", "Velachery", "T Nagar",
                 "Velachery", "Adyar", "T Nagar", "Velachery", "Adyar"],
    "bedrooms": [3, 5, 2, 4, 6, 3, 5, 4, 5, 2],
    "area_sqft": [1500, 2800, 1000, 2100, 3600, 1600, 2900, 2200, 2700, 950],
    "listing_price": [9000000, 18500000, 6500000, 11000000, 25000000,
                      8800000, 19000000, 14000000, 15500000, 6000000]
})
print("Average listing price by location:")
print(property_data.groupby("location")["listing_price"].mean().round(2).to_string())
count = (property_data["bedrooms"] > 4).sum()
print("\nProperties with more than 4 bedrooms:", count)
largest = property_data.loc[property_data["area_sqft"].idxmax()]
print("\nProperty with the largest area:")
print(largest)
