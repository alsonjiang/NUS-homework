import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error
##

X = np.array([[1, -9], [1, -7], [1, -5], [1, 1], [1, 5], [1, 9]])
Y = np.array([[-6], [-6], [-4], [-1], [1], [4]])

w = inv(X.T @ X) @ X.T @ Y #solving overdetermined systems (aka, tall)
#print(w)

Xnew = np.array([1, -1])

Ynew = Xnew@w
#print(Ynew)

## difference
print("Mean squared error between Y and Xw")

Ytest=X@w
#"solving for Y" 

#difference between solved Y and actual Y
MSE = np.square(np.subtract(Ytest,Y)).mean()
print(MSE)

MSE = mean_squared_error(Ytest,Y)
print(MSE)
