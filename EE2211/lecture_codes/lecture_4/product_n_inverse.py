import numpy as np
from numpy.linalg import inv

X = np.array([[1, 4], [0, 4], [3, -2]]) # size 3 x 2
y = np.array([3, 0.5, 4]) # size 3

#print(y)
#print(y.shape)

y1 = np.array([[3], [0.5], [4]]) # size 3 x 1

#print(y1)
#print(y1.shape)

z = X.T@y # 2 x 3 times 3 = 2
print('Vector-matrix product')
print(z)

z1 = X.T@y1 # 2 x 3 times 3 x 1 = 2 x 1
print('Vector-matrix product')
print(z1)

print('matrix product')
X2 = np.array([[1, 4, 3], [0, 4, 2]]) # size 2 x 3
Q = X@X2 # 3 x 2 times 2 x 3 --> 3 x 3
print(Q)

print('matrix inverse')
X = np.array([[1, 4, 3], [0, 4, 2], [3, -2, 9]])
print(inv(X))