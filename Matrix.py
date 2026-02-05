import numpy as np

# Create array (student marks)
marks = np.array([78, 85, 90, 66, 72])

# Basic properties
print("Shape:", marks.shape)
print("Total Students:", marks.size)

# Statistics
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Pass students (>=70)
passed = marks[marks >= 70]
print("Passed Students Marks:", passed)

# Bonus marks (+5)
updated_marks = marks + 5
print("Marks after Bonus:", updated_marks)

# Reshape example
matrix = np.arange(1, 7).reshape(2, 3)
print("2D Matrix:\n", matrix)

# Matrix operation
print("Matrix Transpose:\n", matrix.T)
