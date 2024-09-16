import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# New data from the table
students_new = np.array([36, 26, 35, 39, 26, 30, 31, 38, 36, 38, 26, 26]).reshape(-1, 1)
books_new = np.array([31, 20, 34, 35, 20, 30, 30, 38, 34, 33, 20, 20])

# Linear regression model for the new data
model_new = LinearRegression()
model_new.fit(students_new, books_new)

# Regression equation coefficients for the new data
slope_new = model_new.coef_[0]
intercept_new = model_new.intercept_

# Predicting the number of books sold for 30 students in the new data
prediction_30_students_new = model_new.predict([[30]])[0]

# Purging duplicating data and refitting the line
unique_data_indices = np.unique(students_new, return_index=True)[1]
students_unique = students_new[unique_data_indices]
books_unique = books_new[unique_data_indices]

# Linear regression model for unique data
model_unique = LinearRegression()
model_unique.fit(students_unique, books_unique)

# Regression equation coefficients for unique data
slope_unique = model_unique.coef_[0]
intercept_unique = model_unique.intercept_

# Predicting the number of books sold for 30 students in the unique data
prediction_30_students_unique = model_unique.predict([[30]])[0]

# Plotting both regression lines for comparison
plt.scatter(students_new, books_new, color='blue', label='Original Data')
plt.plot(students_new, model_new.predict(students_new), color='red', label='Original Fit Line')
plt.plot(students_unique, model_unique.predict(students_unique), color='green', linestyle='--', label='Unique Fit Line')
plt.xlabel('Number of Registered Students')
plt.ylabel('Number of Books Sold')
plt.title('Comparison of Original and Unique Fitting Lines')
plt.legend()
plt.grid(True)
plt.show()

# Displaying results
print(f"Original Data Regression: Slope = {slope_new:.2f}, Intercept = {intercept_new:.2f}")
print(f"Predicted books sold for 30 students (Original Data): {prediction_30_students_new:.2f}")
print(f"Unique Data Regression: Slope = {slope_unique:.2f}, Intercept = {intercept_unique:.2f}")
print(f"Predicted books sold for 30 students (Unique Data): {prediction_30_students_unique:.2f}")
