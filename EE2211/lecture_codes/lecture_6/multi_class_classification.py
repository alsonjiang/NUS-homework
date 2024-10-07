import numpy as np
from numpy.linalg import inv
from sklearn.preprocessing import OneHotEncoder

X = np.array([[1, 1, 1], [1, -1, 1], [1, 1, 3], [1, 1, 0]])
y_class = np.array([[1], [2], [1], [3]])

print("One-hot encoding manual")
y_onehot = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1]]) #manual one-hot encoding
print(y_class)
print(y_onehot)

print("One-hot encoding function")
onehot_encoder=OneHotEncoder(sparse_output=False) #auto one-hot encoding
#print(onehot_encoder)
Ytr_onehot = onehot_encoder.fit_transform(y_class) #applies the one-hot encoder on y_class (use fit_transform on training, transform on testing)
print(Ytr_onehot)

#reshaped = y_class.reshape(len(y_class), 1)
#print(reshaped)
#Ytr_onehot = onehot_encoder.fit_transform(reshaped)

## Linear Classification
print("Estimated W")
W = inv(X.T @ X) @ X.T @ Ytr_onehot #calculate weights on the encoded y
print(W)

X_test = np.array([[1, 6, 8], [1, 0, -1]]) #taking a new X
yt_est = X_test@W
print("Test")
print(yt_est)

yt_class = [[1 if y == max(x) else 0 for y in x] for x in yt_est ]
print("class label test")
print(yt_class)