def cond_sum(op, init, pred, limit):
    res = init
    for i in range(limit):
        if pred(i) == True:
            res = op(res, i)
    return res

def add(x, y): #to be put into op
    return x + y

def satisfies_property(x): #to be put into pred
    if (x>0) and (x % 2 == 0):
        return True
    else:
        return False
    
def sum_even(n):
    return cond_sum(add, 0, satisfies_property, 2*n+2)

#print(sum_even(3))

""" short version of the above code, with lambdas to replace add and satisfies_property
def satisfies_property(x): #to be put into pred
    if (x>0) and (x % 2 == 0):
        return True
    else:
        return False
    
def sum_even(n):
    return cond_sum((lambda x,y: x+y), 0, (lambda x: True if (x>0) and (x%2==0) else False), 2*n+2)
"""

#similar function as above, but sum odd nums
def sum_odd(n):
    return cond_sum((lambda x, y: x+y), 0, (lambda x: True if x%2 == 1 and x>0 else False), 2*n+1)


def sum_squares(n):
    # Use cond_sum to sum the squares of the first n positive integers
    return cond_sum(lambda x, y: x+ y*y, 0, lambda x: True, n+1)

def factorial(n):
    return cond_sum((lambda x,y: x*y), 1, (lambda x: x>0), n+1)

