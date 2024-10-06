import numpy as np
from numpy import linalg

"""
#question 1
#even-determined
#X is invertible as it is full rank and it's det != 0
X = np.array([
    [1, 1],
    [3, 2],
])

y = np.array([
    [0],
    [1],
])

invX = np.invert(X)
w = invX@y
print(w)
"""

"""
#question 2
#even-determined
#X is not-invertible as it is not full rank and it's det = 0
X = np.array([
    [1, 2],
    [3, 6],
])

y = np.array([
    [0],
    [1],
])

invX = np.invert(X)
w = invX@y
k = invX@X
print(w)
"""

#question 3
#over-determined
X = np.array([
    [1, 2],
    [2, 4],
    [1, -1],
])

#print(np.linalg.det(X))
print(X.shape)


