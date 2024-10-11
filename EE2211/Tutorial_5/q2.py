import numpy as np

# Training data
X_train = np.array([[1, 0, 1], [2, -1, 1], [1, 1, 5]])  # Features matrix (3 x 3)
y_train = np.array([1, 2, 3])  # Output vector (3 x 1)

# Test data without bias
X_test_without_bias = np.array([[-1, 2, 8], [1, 5, -1]])

# Function to compute weights without bias
def linear_regression_without_bias(X, y):
    #Both formula below works (either over-determined or simply X_inv)
    #W = np.linalg.inv(X.T @ X) @ X.T @ y
    W = np.linalg.inv(X) @ y 
    return W

# Calculate weights without bias
weights_without_bias = linear_regression_without_bias(X_train, y_train)

# Predict the outputs for test data without bias
y_test_without_bias = X_test_without_bias @ weights_without_bias

# Print predictions without bias
print("Predictions without bias term:", y_test_without_bias)


# Include bias term by adding a column of ones to the feature matrix
X_train_with_bias = np.c_[np.ones(X_train.shape[0]), X_train]
X_test_with_bias = np.c_[np.ones(X_test_without_bias.shape[0]), X_test_without_bias]

# Function to compute weights with bias
def linear_regression_with_bias(X, y):
    #under-determined formula
    W = X.T @ np.linalg.inv(X @ X.T) @ y
    return W

# Calculate weights with bias
weights_with_bias = linear_regression_with_bias(X_train_with_bias, y_train)

# Predict the outputs for test data with bias
y_test_with_bias = X_test_with_bias @ weights_with_bias

# Print predictions with bias
print("Predictions with bias term:", y_test_with_bias)
