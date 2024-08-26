import numpy as np
from numpy.linalg import inv

def A1_A0273348X(X, y):
    """
    Input type
    :X type: numpy.ndarray
    :y type: numpy.ndarray

    Return type
    :InvXTX type: numpy.ndarray
    :w type: numpy.ndarray
   
    """
#     X = np.array([[1,1],[4,2],[5,6],[3,-6],[0,-10]])
#     y = np.array([[-3],[2],[1],[6],[4]])
    InvXTX = inv(X.T@X) 
    w = inv(X.T@X)@X.T@y
    
    # your code goes here
    pass

    # return in this order
    return InvXTX, w