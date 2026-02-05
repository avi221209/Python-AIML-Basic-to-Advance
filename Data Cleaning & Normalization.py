import numpy as np

# ----------------------------------------
# NumPy: Data Cleaning & Normalization
# ----------------------------------------

# Dataset with missing values (NaN)
data = np.array([
    [25, 50000, 1],
    [30, np.nan, 0],
    [45, 72000, 1],
    [np.nan, 61000, 0],
    [35, 58000, 1]
], dtype=float)

print("Original Data:\n", data)

# 1. Handling missing values (replace NaN with column mean)
col_means = np.nanmean(data, axis=0)
indices = np.where(np.isnan(data))
data[indices] = np.take(col_means, indices[1])

print("\nData after filling missing values:\n", data)

# 2. Min-Max Normalization (age & salary columns)
age_salary = data[:, :2]

min_vals = age_salary.min(axis=0)
max_vals = age_salary.max(axis=0)

min_max_normalized = (age_salary - min_vals) / (max_vals - min_vals)

print("\nMin-Max Normalized Data:\n", min_max_normalized)

# 3. Z-score Normalization
mean_vals = age_salary.mean(axis=0)
std_vals = age_salary.std(axis=0)

z_score_normalized = (age_salary - mean_vals) / std_vals

print("\nZ-score Normalized Data:\n", z_score_normalized)

# 4. Outlier detection using Z-score
threshold = 2
outliers = np.abs(z_score_normalized) > threshold

print("\nOutlier Matrix (True = Outlier):\n", outliers)
