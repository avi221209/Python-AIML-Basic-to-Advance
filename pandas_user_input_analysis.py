import pandas as pd

# ------------------------------------
# Pandas: User Input Analysis (Beginner)
# ------------------------------------

# Taking user input
names = []
scores = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    score = int(input(f"Enter score of {name}: "))
    names.append(name)
    scores.append(score)

# Creating DataFrame
df = pd.DataFrame({
    "Name": names,
    "Score": scores
})

print("\nStudent Data:")
print(df)

# Basic analysis
print("\nAverage Score:", df["Score"].mean())
print("Highest Score:", df["Score"].max())
print("Lowest Score:", df["Score"].min())

# Result classification
df["Result"] = df["Score"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nFinal Result:")
print(df)
