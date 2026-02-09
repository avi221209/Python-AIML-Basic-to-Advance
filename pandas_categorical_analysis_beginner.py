import pandas as pd

# ----------------------------------------
# Pandas: Categorical Data Analysis
# ----------------------------------------

# Sample dataset
data = {
    "Student": ["Amit", "Neha", "Rahul", "Priya", "Karan", "Neha"],
    "Course": ["Python", "Python", "Java", "Python", "Java", "Java"],
    "Grade": ["A", "B", "A", "C", "B", "A"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Count values in a categorical column
course_counts = df["Course"].value_counts()
print("\nCourse Count:")
print(course_counts)

# 2. Count grades
grade_counts = df["Grade"].value_counts()
print("\nGrade Count:")
print(grade_counts)

# 3. Map grades to numeric scores
grade_map = {
    "A": 90,
    "B": 75,
    "C": 60
}

df["Score"] = df["Grade"].map(grade_map)
print("\nData after mapping Grade to Score:")
print(df)

# 4. Average score per course
avg_score_course = df.groupby("Course")["Score"].mean()
print("\nAverage Score per Course:")
print(avg_score_course)
