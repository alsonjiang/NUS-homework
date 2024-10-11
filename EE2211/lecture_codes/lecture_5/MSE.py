import numpy as np
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error

'''
# Define matrices X and Y
X = np.array([[50, 10], [40, 7], [65, 12], [70, 5], [75, 4]])
Y = np.array([[9, 3], [6, 7], [5, 6], [3, 1], [2, 9]])

# Calculate the weights using the normal equation
w = inv(X.T @ X) @ X.T @ Y
print("Calculated Weights (W):\n", w)

# Predict new values for the input X
Ytest = X @ w

# Calculate and print MSE for each column separately
for i in range(Y.shape[1]):
    #MSE_column = mean_squared_error(Ytest[:, i], Y[:, i])
    MSE_column = np.square(np.subtract(Ytest[:, i], Y[:, i])).mean()
    print(f"Mean Squared Error for Column {i+1} of Y: {MSE_column:.4f}")

Xnew = np.array([[62,8]])
Ynew = Xnew @ w
print(Ynew)
'''

X = np.array([[1, 50, 10], [1, 40, 7], [1, 65, 12], [1, 70, 5], [1, 75, 4]])
y = np.array([[9, 3], [6, 7], [5, 6], [3, 1], [2, 9]])

w = inv(X.T @ X) @ X.T @ y

if w is not None:
    error = X@w - y
    print('\nerror is:')
    print(error)
    print('\nleast square error is:')
    error_mat = error.T @ error / len(error)
    print(error_mat)