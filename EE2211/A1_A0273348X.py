import numpy as np
from numpy.linalg import inv

def A1_A0273348X(X, y):

    XT = np.transpose(X)
    XT_X = XT@X
    InvXTX = inv(XT_X)
    
    pre_multiply = InvXTX@XT
    w = pre_multiply@y

    return InvXTX, w