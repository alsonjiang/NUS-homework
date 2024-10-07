import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error

X = np.array([[1, 3], [1, 4], [1, 10], [1, 6], [1, 7]]) #5x2
Y = np.array([[0, 5], [1.5, 4], [-3, 8], [-4, 10], [1, 6]]) #5x2

w = inv(X.T @ X) @ X.T @ Y
print('W')
print(w)

Xnew = np.array([[1, 2]]) #1x2
Ynew = Xnew@w #1x2
print('Ynew')
print(Ynew)

print('Xnew')
print(Xnew)
print(Xnew.shape)

Ytest= X@w #calculate y using weights
print('Ytest')
print(Ytest)

#plotting y based on features. Two features in y = two lines
plt.plot(X[:,1], Y[:,0], 'o', label = 'Y1')
plt.plot(X[:,1], Y[:,1], 'x', label = 'Y2')
plt.plot(X[:,1], Ytest[:,0]) #first column of y
plt.plot(X[:,1], Ytest[:,1]) #second column of y
plt.xlabel('X')
plt.ylabel('Y')
plt.show()