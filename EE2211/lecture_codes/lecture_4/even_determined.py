import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from numpy.linalg import matrix_rank

#even determined, m = d (rows = cols, samples = features)
#solve with w = X_inverse*y

X = np.array([[1, 1], [1, -2]]) #2x2
y = np.array([4, 1]) #2
#print(y.shape)
w = inv(X) @ y #2x2 . 2 = 2
#print(w)

#print('more examples')
X = np.array([[1, 4, 2], [0, 4, 3], [3, 4, 9]]) #3x3
y = np.array([39, 40, 50]) #3
w = inv(X) @ y #3x3 . 3 = 3
#print(w)

print('rank')
X = np.array([[1, 4, 2], [0, 4, 3], [1, 8, 5]]) #rank 2
y = np.array([1, 0, 1])
#print(matrix_rank(X))