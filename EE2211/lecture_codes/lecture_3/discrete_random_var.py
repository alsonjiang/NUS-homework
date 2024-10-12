import numpy as np

# Example data
data = [128, 219, 316, 189, 512, 98, 155, 110, 468, 177, 203, 73, 252]

# Calculate expected value (mean)
expected_value = np.mean(data)

# Calculate variance
variance = np.var(data, ddof=0)  # population variance, use ddof=1 for sample variance

# Calculate standard deviation
std_deviation = np.std(data, ddof=0)  # population std deviation, use ddof=1 for sample std deviation

print(f"Expected Value (Mean): {expected_value}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
