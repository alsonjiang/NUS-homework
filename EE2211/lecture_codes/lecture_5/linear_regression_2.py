import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error

X = np.array([[1, 1, 1], [1, -1, 1], [1, 1, 3], [1, 1, 0]]) #4x3
Y = np.array([[1, 0], [0, 1], [2, -1], [-1, 3]])
w = inv(X.T @ X) @ X.T @ Y
print("the estimated w")
print(w)

Xnew = np.array([[1, 6, 8], [1, 0, -1]]) #2x3
Ynew = Xnew@w
print("testing Ynew")
print(Ynew)

## difference
print("Mean squared error between Y and XW")
Ytest=X@w

MSE = np.square(np.subtract(Ytest,Y)).mean()
print(MSE)

MSE = mean_squared_error(Ytest,Y)
print(MSE)