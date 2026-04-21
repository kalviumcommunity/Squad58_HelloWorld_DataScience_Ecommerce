# Python Loops Demo: for and while

# -------------------------------
# 1. For Loop (fixed iterations)
# -------------------------------

print("For Loop Example:")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print("Number:", num)

# Using range
print("\nFor Loop with range:")
for i in range(1, 6):
    print("Value:", i)

# -------------------------------
# 2. While Loop (condition-based)
# -------------------------------

print("\nWhile Loop Example:")
count = 1

while count <= 5:
    print("Count:", count)
    count += 1   # important to avoid infinite loop

# -------------------------------
# 3. Break and Continue
# -------------------------------

print("\nBreak Example:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# -------------------------------
# 4. Avoiding Infinite Loops
# -------------------------------

print("\nLoop Safety Example:")
x = 1

while x <= 3:
    print("Safe loop:", x)
    x += 1

print("Loop ended successfully")