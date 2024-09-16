import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Read Data
data = pd.read_csv('EE2211/Tutorial_5/GovernmentExpenditureonEducation.csv')

#X and Y axes
X = data[['year']].values  # Independent variable (features)
Y = data['recurrent_expenditure_total'].values  # Dependent variable (target)

#Model
model = LinearRegression()
model.fit(X, Y)

#Regression Coefficients
slope = model.coef_[0]
intercept = model.intercept_

#Regression Eqn
print(f"Regression Equation: Y = {slope:.2f} * X + {intercept:.2f}")

#Predict
X_new = np.array([[2021]])
Y_pred = model.predict(X_new)
print(f"Predicted expenditure for Year = 2021: {Y_pred[0]:.2f}")

#Plotting the data and regression line
plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()