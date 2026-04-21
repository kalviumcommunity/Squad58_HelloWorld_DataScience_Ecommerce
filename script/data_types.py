# Python Data Types Demonstration

# -------------------------------
# 1. Numeric Data Types
# -------------------------------

# Integer
num1 = 10

# Float
num2 = 3.5

print("Integer:", num1)
print("Float:", num2)

# Arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# -------------------------------
# 2. String Data Types
# -------------------------------

name = "Anushka"
message = "Hello"

print("Name:", name)
print("Message:", message)

# String concatenation
full_message = message + " " + name
print("Concatenated String:", full_message)

# -------------------------------
# 3. Mixing Numbers and Strings
# -------------------------------

age = 20

# This will cause error (commented intentionally)
# print("Age is " + age)

# Correct way (type conversion)
print("Age is " + str(age))

# Convert string to number
num_str = "50"
converted_num = int(num_str)

print("Converted Number:", converted_num)

# -------------------------------
# 4. Checking Data Types
# -------------------------------

print("Type of num1:", type(num1))
print("Type of num2:", type(num2))
print("Type of name:", type(name))
print("Type of converted_num:", type(converted_num))