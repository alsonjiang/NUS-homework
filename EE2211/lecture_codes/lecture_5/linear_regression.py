import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error

#X = np.array([[1, -9], [1, -7], [1, -5], [1, 1], [1, 5], [1, 9]]) #6x2 overdetermined
X = np.array([[50, 10], [40, 7], [65, 12], [70, 5], [75, 4]])
#Y = np.array([[-6], [-6], [-4], [-1], [1], [4]]) #6x1
Y = np.array([[9, 3], [6, 7], [5, 6], [3, 1], [2, 9]])

w = inv(X.T @ X) @ X.T @ Y
print(w)

Xnew = np.array([62, 8]) #2
Ynew = Xnew@w
print(Ynew)

## difference
print("Mean squared error between Y and XW") #actual y and calculated y (with weights)
Ytest=X@w

#two ways to do MSE!
MSE = np.square(np.subtract(Ytest,Y)).mean() #formula?
print(MSE)

MSE = mean_squared_error(Ytest,Y) #built in function
print(MSE)