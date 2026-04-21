# Python Functions: Parameters and Return Values

# -------------------------------
# 1. Function with Parameters
# -------------------------------

def add(a, b):
    return a + b

result1 = add(5, 10)
print("Addition Result:", result1)

# -------------------------------
# 2. Function Returning Value
# -------------------------------

def square(num):
    return num * num

result2 = square(4)
print("Square Result:", result2)

# -------------------------------
# 3. Using Returned Values
# -------------------------------

def multiply(x, y):
    return x * y

product = multiply(result1, result2)
print("Multiplication of results:", product)

# -------------------------------
# 4. Function with Strings
# -------------------------------

def greet(name):
    return "Hello, " + name

message = greet("Anushka")
print(message)

# -------------------------------
# 5. Avoid Hardcoding (Flexible Function)
# -------------------------------

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(100, 3)
print("Total Price:", total)