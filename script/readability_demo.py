# Python Readability Demo (PEP 8 Naming & Comments)

# ❌ Poor variable naming (avoid this)
x = 100
y = 5
z = x * y
print("Bad Example Result:", z)

# ✅ Good variable naming (PEP 8 style)
price_per_item = 100
quantity = 5
total_price = price_per_item * quantity

print("Good Example Result:", total_price)


# -----------------------------------------
# Example with meaningful comments
# -----------------------------------------

# Calculate discount amount based on percentage
def calculate_discount(total_amount, discount_rate):
    discount = total_amount * discount_rate
    return discount


# Apply discount to total price
discount_value = calculate_discount(total_price, 0.1)

# Final amount after applying discount
final_amount = total_price - discount_value

print("Final Amount after discount:", final_amount)


# -----------------------------------------
# Avoid unnecessary comments
# -----------------------------------------

# ❌ Bad comment (obvious)
# adding two numbers
a = 10 + 5

# ✅ No comment needed here (self-explanatory)
b = 10 + 5


# -----------------------------------------
# Consistent naming example
# -----------------------------------------

user_name = "Anushka"
user_age = 20

print("User:", user_name)
print("Age:", user_age)