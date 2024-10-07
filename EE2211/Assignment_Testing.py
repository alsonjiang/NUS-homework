import numpy as np
from numpy.linalg import inv
#from A1_A0273348X import A1_A0273348X as grading
import A2_A0273348X as grading

"""
j = np.array([
    [1, 1],
    [4, 2],
    [4, 6],
    [3, -6],
    [0, -10]
])
    
k = np.array([
    [-3],
    [2],
    [1],
    [5],
    [4]
])
"""

if __name__ == '__main__':

    #inverse, w_cap = grading(j, k)
    #print(np.shape(k))
    #print(inverse)
    #print(np.shape(w_cap))
    #print(w_cap)

    X_train, y_train, X_test, y_test, Ytr, Yts, Ptrain_list, Ptest_list, w_list, error_train_array, error_test_array = grading.A2_A0273348X(5)
    print(X_test)
