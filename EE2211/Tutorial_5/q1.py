import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

x = np.array([[-10], [-8], [-3], [-1], [2], [8]])
y = np.array([[5], [5], [4], [3], [2], [2]])

# (a) Linear regression with a bias term (intercept)
model_with_bias = LinearRegression(fit_intercept=True) #auto bias adding and model fitting y=mx+c
model_with_bias.fit(x, y)
y_pred_with_bias = model_with_bias.predict(x)

# (b) Linear regression without a bias term (intercept)
model_without_bias = LinearRegression(fit_intercept=False)
model_without_bias.fit(x, y)
y_pred_without_bias = model_without_bias.predict(x)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred_with_bias, color='red', linestyle='-', label='With Bias (Intercept)')
plt.plot(x, y_pred_without_bias, color='green', linestyle='--', label='Without Bias (No Intercept)')
plt.title('Linear Regression with and without Bias (Intercept)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Displaying coefficients and intercepts for analysis
print("With Bias (Intercept): Coefficient =", model_with_bias.coef_[0], "Intercept =", model_with_bias.intercept_)
print("Without Bias (No Intercept): Coefficient =", model_without_bias.coef_[0], "Intercept =", model_without_bias.intercept_)

#(c)Adding a bias term allows the line to shift vertically, which helps to fit the data better, 
#especially when the data points do not pass through the origin. Without a bias term, the regression line is forced to pass through the origin, 
#which may lead to a less accurate fit if the true relationship does not pass through (0,0).