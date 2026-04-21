# Python Collections Demo: Lists, Tuples, Dictionaries

# -------------------------------
# 1. Lists (mutable)
# -------------------------------

numbers = [10, 20, 30, 40]

print("Original List:", numbers)

# Access element
print("First element:", numbers[0])

# Modify element
numbers[1] = 25

# Add element
numbers.append(50)

# Remove element
numbers.remove(30)

print("Updated List:", numbers)

# -------------------------------
# 2. Tuples (immutable)
# -------------------------------

coordinates = (5, 10, 15)

print("\nTuple:", coordinates)

# Access element
print("First value:", coordinates[0])

# Try modifying (will cause error if uncommented)
# coordinates[0] = 100

print("Tuples are immutable (cannot be changed)")

# -------------------------------
# 3. Dictionaries (key-value pairs)
# -------------------------------

student = {
    "name": "Anushka",
    "age": 20,
    "course": "Data Science"
}

print("\nDictionary:", student)

# Access value
print("Name:", student["name"])

# Modify value
student["age"] = 21

# Add new key
student["city"] = "Delhi"

print("Updated Dictionary:", student)

# -------------------------------
# 4. Choosing the Right Structure
# -------------------------------

print("\nUse Lists for ordered and changeable data")
print("Use Tuples for fixed data")
print("Use Dictionaries for key-value structured data")