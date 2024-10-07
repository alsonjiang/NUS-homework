import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_rank
from numpy.linalg import det

#under determined, m < d (rows < cols, samples < features)
#solve with XT.(X.XT)inv * y

X = np.array([[1, 2, 3], [1, -2, 3]]) #2x3
y = np.array([2, 1]) #2
w = X.T @ inv(X@ X.T) @ y
print(w)
