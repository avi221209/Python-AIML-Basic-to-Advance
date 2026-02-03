import numpy as np

# ----------------------------------
# NumPy: Random Data & Linear Algebra
# ----------------------------------

# 1. Generate random data (e.g., sensor readings)
data = np.random.randint(1, 101, size=(4, 4))
print("Random Data Matrix:\n", data)

# 2. Sorting
print("\nRow-wise sorted data:\n", np.sort(data, axis=1))
print("\nColumn-wise sorted data:\n", np.sort(data, axis=0))

# 3. Filtering values greater than 50
filtered_values = data[data > 50]
print("\nValues greater than 50:", filtered_values)

# 4. Replace values less than 30 with 0
modified_data = data.copy()
modified_data[modified_data < 30] = 0
print("\nData after replacing values < 30 with 0:\n", modified_data)

# 5. Matrix operations
matrix_a = np.array([
    [2, 1],
    [3, 4]
])

matrix_b = np.array([
    [1, 2],
    [5, 6]
])

print("\nMatrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Matrix multiplication
matrix_mul = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication (A x B):\n", matrix_mul)

# 6. Determinant and inverse
determinant = np.linalg.det(matrix_a)
inverse = np.linalg.inv(matrix_a)

print("\nDeterminant of Matrix A:", determinant)
print("Inverse of Matrix A:\n", inverse)

# 7. Solving linear equations
# 2x +  y = 5
# 3x + 4y = 11
coefficients = np.array([[2, 1], [3, 4]])
constants = np.array([5, 11])

solution = np.linalg.solve(coefficients, constants)
print("\nSolution of linear equations [x, y]:", solution)
