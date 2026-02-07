import pandas as pd

# ------------------------------------
# Pandas: Date-wise Analysis (Beginner)
# ------------------------------------

# Creating sales data with dates
data = {
    "Date": [
        "2026-02-01", "2026-02-02", "2026-02-03",
        "2026-02-04", "2026-02-05"
    ],
    "Sales": [1200, 1500, 1100, 1800, 1600]
}

df = pd.DataFrame(data)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("Original Data:")
print(df)

# 1. Set Date as index
df.set_index("Date", inplace=True)
print("\nData with Date as Index:")
print(df)

# 2. Calculate daily sales change
df["Daily_Change"] = df["Sales"].diff()
print("\nDaily Sales Change:")
print(df)

# 3. Identify high sales days
high_sales = df[df["Sales"] > 1500]
print("\nHigh Sales Days:")
print(high_sales)

# 4. Calculate average sales
average_sales = df["Sales"].mean()
print("\nAverage Daily Sales:", average_sales)

# 5. Simple trend check
df["Trend"] = df["Daily_Change"].apply(
    lambda x: "Increase" if x > 0 else "Decrease" if x < 0 else "No Change"
)

print("\nSales Trend:")
print(df)
