# NumPy Arrays from Python Lists Demo

# -------------------------------
# 1. Import NumPy
# -------------------------------

import numpy as np


# -------------------------------
# 2. Python Lists (Input Data)
# -------------------------------

list_1d = [10, 20, 30, 40]
list_2d = [
    [1, 2, 3],
    [4, 5, 6],
]

print("Original Python 1D List:", list_1d)
print("Original Python 2D List:", list_2d)


# -------------------------------
# 3. Create NumPy Arrays from Lists
# -------------------------------

array_1d = np.array(list_1d)
array_2d = np.array(list_2d)

print("\nNumPy 1D Array:", array_1d)
print("NumPy 2D Array:\n", array_2d)


# -------------------------------
# 4. Inspect Array Properties
# -------------------------------

print("\n1D Array Shape:", array_1d.shape)
print("1D Array Data Type:", array_1d.dtype)
print("1D Array Dimensions:", array_1d.ndim)

print("\n2D Array Shape:", array_2d.shape)
print("2D Array Data Type:", array_2d.dtype)
print("2D Array Dimensions:", array_2d.ndim)


# -------------------------------
# 5. Basic Array Operations
# -------------------------------

array_addition = array_1d + 5
array_multiplication = array_1d * 2

print("\nArray + 5 (element-wise):", array_addition)
print("Array * 2 (element-wise):", array_multiplication)


# -------------------------------
# 6. List vs Array Behavior
# -------------------------------

print("\nPython List * 2 (repetition):", list_1d * 2)
print("NumPy Array * 2 (element-wise):", array_1d * 2)
