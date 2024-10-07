from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Given input matrix X
X = np.array([[1, 0, 1], [1, -1, 1]])

# Generate polynomial features up to degree 3
poly = PolynomialFeatures(degree=3, include_bias=True)
P = poly.fit_transform(X)

# Display the P-matrix
print("P-matrix for the given polynomial:\n", P)
