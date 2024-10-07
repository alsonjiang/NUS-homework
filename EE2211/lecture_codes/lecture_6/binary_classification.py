import numpy as np
from numpy.linalg import inv

X = np.array([[1,-9], [1,-7], [1,-5], [1,1], [1,5], [1, 9]]) #6x2
y = np.array([[-1], [-1], [-1], [1], [1], [1]]) #6x1
## Linear regression for classification
w = inv(X.T @ X) @ X.T @ y #find weights for overdetermined system
print("Estimated w")
print(w)

Xt = np.array([[1,-2]]) #new data point
y_predict = Xt @ w #calculate new target
print("Predicted y")
print(y_predict)

y_class_predict = np.sign(y_predict) #predict class
print("Predicted y class")
print(y_class_predict)