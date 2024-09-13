import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error
##

X = np.array([[1, 3], [1, 4], [1, 10], [1, 6], [1, 7]])
Y = np.array([[0, 5], [1.5, 4], [-3, 8], [-4, 10], [1, 6]])

w = inv(X.T @ X) @ X.T @ Y
#print('W')
#print(w)

Xnew = np.array([[1, 2]])
Ynew = Xnew@w #solving for a new value of Y using obtained weights, w
#print('Ynew')
#print(Xnew)
#print(Xnew.shape)
#print(Ynew)

Ytest= X@w #solving for initial Y using obtained weights, w
#print('Ytest')
#print(Ytest)

plt.plot(X[:,1], Y[:,0], 'o', label = 'Y1')
plt.plot(X[:,1], Y[:,1], 'x', label = 'Y2')
plt.plot(X[:,1], Ytest[:,0])
plt.plot(X[:,1], Ytest[:,1])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()