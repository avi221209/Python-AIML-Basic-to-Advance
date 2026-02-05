import numpy as np

# ----------------------------------
# NumPy: Time Series Style Analysis
# ----------------------------------

# Simulated daily temperatures for 15 days (°C)
temperatures = np.array([
    28, 30, 29, 31, 33,
    35, 34, 36, 37, 38,
    36, 35, 34, 33, 32
])

print("Daily Temperatures:", temperatures)

# 1. Basic statistics
print("\nAverage Temperature:", np.mean(temperatures))
print("Max Temperature:", np.max(temperatures))
print("Min Temperature:", np.min(temperatures))

# 2. Daily temperature change
daily_change = np.diff(temperatures)
print("\nDaily Temperature Change:", daily_change)

# 3. Identify heatwave days (> 35°C)
heatwave_days = temperatures > 35
print("\nHeatwave Days (True = Heatwave):", heatwave_days)

# 4. Rolling average (window size = 3)
window_size = 3
rolling_avg = np.convolve(
    temperatures,
    np.ones(window_size) / window_size,
    mode="valid"
)

print("\n3-Day Rolling Average:", rolling_avg)

# 5. Normalization (for ML readiness)
min_temp = temperatures.min()
max_temp = temperatures.max()

normalized_temp = (temperatures - min_temp) / (max_temp - min_temp)
print("\nNormalized Temperatures:", normalized_temp)

# 6. Trend detection (simple)
trend = np.sign(daily_change)
print("\nTemperature Trend (+1 rising, -1 falling):", trend)
