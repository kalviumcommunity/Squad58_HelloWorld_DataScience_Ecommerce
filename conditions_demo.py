# Python Conditional Statements Demo

# -------------------------------
# 1. Basic if statement
# -------------------------------

num = 10

if num > 5:
    print("Number is greater than 5")

# -------------------------------
# 2. if-else statement
# -------------------------------

age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# -------------------------------
# 3. if-elif-else statement
# -------------------------------

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# -------------------------------
# 4. Logical operators
# -------------------------------

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Using OR
temperature = 35

if temperature > 30 or temperature < 10:
    print("Extreme weather condition")

# Using NOT
is_logged_in = False

if not is_logged_in:
    print("User is not logged in")