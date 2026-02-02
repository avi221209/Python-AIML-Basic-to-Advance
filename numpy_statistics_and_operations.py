import numpy as np

# -----------------------------
# NumPy Statistics & Operations
# -----------------------------

# Creating a 2D array (e.g., student marks)
marks = np.array([
    [78, 85, 90],
    [88, 76, 92],
    [69, 80, 75],
    [95, 91, 89]
])

print("Marks Matrix:\n", marks)

# Shape of array
print("\nShape:", marks.shape)

# Statistical operations
print("\nOverall Mean:", np.mean(marks))
print("Overall Median:", np.median(marks))
print("Overall Standard Deviation:", np.std(marks))

# Axis-wise operations
print("\nAverage marks per student:", np.mean(marks, axis=1))
print("Average marks per subject:", np.mean(marks, axis=0))

# Maximum and minimum
print("\nHighest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))

# Boolean masking (students scoring above 85)
high_scores = marks > 85
print("\nMarks above 85:\n", high_scores)

# Extracting actual values above 85
print("\nValues above 85:", marks[marks > 85])

# Adding bonus marks
bonus_marks = marks + 5
print("\nMarks after bonus:\n", bonus_marks)

# Clipping marks to max 100
final_marks = np.clip(bonus_marks, 0, 100)
print("\nFinal Marks (Clipped to 100):\n", final_marks)
