# Item prices and quantities
prices = [50, 120, 30, 15]
quantities = [2, 1, 4, 6]

discount_rate = 10   # percent
tax_rate = 5         # percent

# Subtotal = sum of (price x quantity)
subtotal = 0
for price, qty in zip(prices, quantities):
    subtotal += price * qty

discount = subtotal * discount_rate / 100
after_discount = subtotal - discount

tax = after_discount * tax_rate / 100
total = after_discount + tax

print(f"Subtotal        : {subtotal:.2f}")
print(f"Discount ({discount_rate}%)  : -{discount:.2f}")
print(f"Tax ({tax_rate}%)        : +{tax:.2f}")
print(f"Total cost      : {total:.2f}")
