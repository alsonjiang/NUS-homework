import numpy as np
from sklearn.linear_model import LinearRegression


# Step 1: Prepare the data
X = np.array([[3, -1, 0], [5, 1, 2], [9, -1, 3], [-6, 7, 2], [3, -2, 0]])  # Feature vectors (5x3)
Y = np.array([[1, -1], [-1, 0], [1, 2], [0, 3], [1, -2]])  # Target vectors (5x2)
#(5x3)(3x2)=(5x2)

# Step 2: Perform Linear Regression with Multiple Outputs
model = LinearRegression()
model.fit(X, Y)

# Coefficients (weights) and intercept
weights = model.coef_
intercept = model.intercept_

print("Weights (coefficients):\n", weights)
print("Intercept:", intercept)

# Step 3: Predict the value of y when x = [8, 0, 2]
x_new = np.array([[8, 0, 2]])
y_pred = model.predict(x_new)

print("Predicted value of y for x = [8, 0, 2]:", y_pred)



