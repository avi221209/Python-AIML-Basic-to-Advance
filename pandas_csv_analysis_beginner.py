import pandas as pd

# ------------------------------------
# Pandas: CSV File Analysis (Beginner)
# ------------------------------------

# Create sample data and save to CSV (one-time)
data = {
    "Employee": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "Salary": [30000, 45000, 42000, 50000, 32000]
}

df = pd.DataFrame(data)
df.to_csv("employee_data.csv", index=False)

# Read CSV file
df = pd.read_csv("employee_data.csv")

print("Employee Data:")
print(df)

# 1. Basic statistics
print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

# 2. Group by department
dept_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(dept_salary)

# 3. Employees earning above average
above_avg = df[df["Salary"] > df["Salary"].mean()]
print("\nEmployees earning above average salary:")
print(above_avg)
