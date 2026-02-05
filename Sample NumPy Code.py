import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# Basic operations
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))

# Reshaping
reshaped = arr1.reshape(5, 1)
print("Reshaped Array:\n", reshaped)

# Array arithmetic
print("Array * 2:", arr1 * 2)

# Indexing & slicing
print("First element:", arr1[0])
print("Slice:", arr1[1:4])
