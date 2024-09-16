import numpy as np
import pandas as pd
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine = pd.read_csv(url, sep=';')

# Step 2: Prepare the data
# Target output
y = wine['quality']
# Input features
X = wine.drop('quality', axis=1)

# Split the data into training and testing sets
X_train = X.iloc[:1500]
X_test = X.iloc[1500:1599]
y_train = y.iloc[:1500]
y_test = y.iloc[1500:1599]

# Step 3: Perform Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Output learned parameters
print("Learned coefficients (weights):", model.coef_)
print("Intercept:", model.intercept_)

# Step 4: Perform prediction using the test set
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE) on test set:", mse)
