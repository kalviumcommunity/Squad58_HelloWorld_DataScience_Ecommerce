# Python Functions Demo

# -------------------------------
# 1. Defining a Function
# -------------------------------

def greet():
    print("Hello, welcome to Python functions!")

# Calling function
greet()

# -------------------------------
# 2. Function with Parameters
# -------------------------------

def add_numbers(a, b):
    result = a + b
    print("Sum:", result)

add_numbers(5, 10)

# -------------------------------
# 3. Function with Return Value
# -------------------------------

def multiply(x, y):
    return x * y

result = multiply(4, 5)
print("Multiplication Result:", result)

# -------------------------------
# 4. Function with Strings
# -------------------------------

def full_name(first, last):
    return first + " " + last

name = full_name("Anushka", "Bhatt")
print("Full Name:", name)

# -------------------------------
# 5. Function Scope
# -------------------------------

global_var = "I am global"

def scope_demo():
    local_var = "I am local"
    print(global_var)
    print(local_var)

scope_demo()

# print(local_var)  # This would cause an error (local variable)