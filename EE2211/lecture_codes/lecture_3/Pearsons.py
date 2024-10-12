import numpy as np
from scipy.stats import pearsonr

# Example data
x = [10, 20, 30, 40, 50]
y = [12, 24, 33, 45, 58]

# Calculate Pearson's correlation coefficient
correlation, p_value = pearsonr(x, y)

print(f"Pearson's correlation coefficient: {correlation}")
print(f"P-value: {p_value}")
