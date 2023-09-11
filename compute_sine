import math

#factorial
def fact(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    
    result = n * fact(n-1, memo)
    memo[n] = result
    return result
 
#Taylor Series (iterative)
def sineIterative(x,k):
    result = 0
    for n in range(0,k):
        result += ((-1)**n / fact(2*n+1) * x**(2*n+1))
    return result

print(sineIterative(math.pi/6,10))

#recursive
def sineRecursive(x,k):
    if k < 0:
        return 0
    return sineRecursive(x,k-1) + ((-1)**k / fact(2*k+1) * x**(2*k+1))

print(sineRecursive(math.pi/6,10))
