import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Given data points
x_train = np.array([-10, -8, -3, -1, 2, 8]).reshape(-1, 1)
y_train = np.array([5, 5, 4, 3, 2, 2])

# Polynomial Regression - 3rd Order
poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x_train)

# Fitting the polynomial model
poly_model = LinearRegression()
poly_model.fit(x_poly, y_train)

# Predict for a test point x = 9
x_test = np.array([[9]])
x_test_poly = poly.transform(x_test)
y_pred_poly = poly_model.predict(x_test_poly)[0]

# Linear Regression
lin_model = LinearRegression()
lin_model.fit(x_train, y_train)

# Predict for the same test point x = 9 using linear regression
y_pred_linear = lin_model.predict(x_test)[0]

# Generate points for plotting
x_range = np.linspace(min(x_train) - 1, max(x_train) + 1, 100).reshape(-1, 1)
x_range_poly = poly.transform(x_range)
y_poly = poly_model.predict(x_range_poly)
y_linear = lin_model.predict(x_range)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(x_train, y_train, color='red', label='Data Points')
plt.plot(x_range, y_poly, label='3rd-Order Polynomial Fit', color='blue')
plt.plot(x_range, y_linear, label='Linear Fit', color='green', linestyle='--')
plt.scatter(x_test, y_pred_poly, color='blue', s=100, label=f'Poly Prediction at x=9: {y_pred_poly:.2f}')
plt.scatter(x_test, y_pred_linear, color='green', s=100, label=f'Linear Prediction at x=9: {y_pred_linear:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('3rd-Order Polynomial Regression and Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

# Displaying predictions
print(f"Prediction using 3rd-Order Polynomial Model at x=9: {y_pred_poly:.2f}")
print(f"Prediction using Linear Model at x=9: {y_pred_linear:.2f}")
