import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data from the table
students = np.array([36, 28, 35, 39, 30, 30, 31, 38, 36, 38, 29, 26]).reshape(-1, 1)
books = np.array([31, 29, 34, 35, 29, 30, 30, 38, 34, 33, 29, 26])

# Scatter plot of the number of books sold versus the number of registered students
plt.scatter(students, books, color='blue', label='Data points')
plt.xlabel('Number of Registered Students')
plt.ylabel('Number of Books Sold')
plt.title('Scatter Plot of Books Sold vs. Registered Students')
plt.grid(True)
plt.show()

# Linear regression model
model = LinearRegression()
model.fit(students, books) #(x,y)

# Regression equation coefficients
slope = model.coef_[0]
intercept = model.intercept_

# Displaying the regression equation
regression_eq = f"Books Sold = {slope:.2f} * Students Registered + {intercept:.2f}"
print("Regression Equation:", regression_eq)

# Predicting the number of books sold for 30 and 5 students
prediction_30_students = model.predict([[30]])[0]
prediction_5_students = model.predict([[5]])[0]

print(f"Predicted books sold for 30 students: {prediction_30_students:.2f}")
print(f"Predicted books sold for 5 students: {prediction_5_students:.2f}")
