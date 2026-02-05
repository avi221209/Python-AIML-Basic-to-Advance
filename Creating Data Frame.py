import pandas as pd
data = {
    "Age": [22, 25, 30, 28],
    "Salary": [25000, 30000, 40000, 35000],
    "Purchased": [0, 1, 1, 0]
}

df = pd.DataFrame(data)
print(df)
