import numpy as np
from numpy.linalg import inv
from numpy.linalg import matrix_rank
from sklearn.preprocessing import PolynomialFeatures

X = np.array([ [0, 0], [1, 1], [1, 0], [0, 1]]) #4x2
y = np.array([[-1], [-1], [1], [1]]) #4x1

## Generate polynomial features
order = 2
poly = PolynomialFeatures(order)
print(poly)

P = poly.fit_transform(X)
print("matrix P")
print(P)
print("***************************************")
#print(matrix_rank(P))
#PY = np.vstack((P.T, y.T))
#print(matrix_rank(PY.T))
## dual solution m < d (without ridge)
w_dual = P.T @ inv(P @ P.T) @ y
print("Under-determined system")
print("Unique constrained solution, no ridge")
print(w_dual)
print("***************************************")
print("Approximation with dual ridge regression")
print(P.shape)
reg_L2 = 0.0001*np.identity(P.shape[0]) #number of rows of P = Dual I
print(reg_L2)
w_dual_ridge = P.T @ (inv(P @ P.T + reg_L2)) @ y
print(w_dual_ridge)
print("***************************************")
## primal ridge
print("Approximation with primal ridge regression")
print(P.shape)
reg_L = 0.0001*np.identity(P.shape[1]) #number of columns of P = Primal I
print(reg_L)
w_primal_ridge = inv(P.T @ P + reg_L) @ P.T @ y
print(w_primal_ridge)