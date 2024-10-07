import numpy as np
from numpy.linalg import inv

#over determined, m > d (rows > cols, samples > features)
#solve with (XT.X)inv.XT * y

X = np.array([[1, 1], [1, -1], [1, 0]]) #3x2
y = np.array([1, 0, 2]) #3
w = inv(X.T @ X) @ X.T @ y
print(w)