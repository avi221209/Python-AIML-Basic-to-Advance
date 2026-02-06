import pandas as pd

# --------------------------------
# Pandas: Data Cleaning (Beginner)
# --------------------------------

# Creating a DataFrame (simulating CSV data)
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Price": [55000, 20000, None, 52000, 21000],
    "Quantity": [2, 5, 3, None, 4]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull())

# 2. Fill missing values
df["Price"].fillna(df["Price"].mean(), inplace=True)
df["Quantity"].fillna(1, inplace=True)

print("\nData after filling missing values:")
print(df)

# 3. Calculate total price
df["Total_Price"] = df["Price"] * df["Quantity"]
print("\nData after adding Total_Price column:")
print(df)

# 4. Grouping data
grouped = df.groupby("Product")["Total_Price"].sum()
print("\nTotal Sales per Product:")
print(grouped)

# 5. Sorting
sorted_data = df.sort_values(by="Total_Price", ascending=False)
print("\nSorted by Total_Price:")
print(sorted_data)
