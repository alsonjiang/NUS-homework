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
model_w_bias = LinearRegression(fit_intercept=True)
model_w_bias.fit(X, Y)

#Regression Coefficients
slope = model_w_bias.coef_[0]
intercept = model_w_bias.intercept_

#Regression Eqn
print(f"Regression Equation: Y = {slope:.2f} * X + {intercept:.2f}")

#Predict
X_new = np.array([[2021]])
Y_pred = model_w_bias.predict(X_new)
print(f"Predicted expenditure for Year = 2021: {Y_pred[0]:.2f}")

#Plotting the data and regression line
plt.scatter(X, Y, color='blue', label='Data points')
plt.plot(X, model_w_bias.predict(X), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()