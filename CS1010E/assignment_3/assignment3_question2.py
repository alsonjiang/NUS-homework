import time
import sys
sys.setrecursionlimit(10**6)

#binomial without recursion
def get_factorial(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial

def binom_coeff(n,k):
    coefficient = get_factorial(n) // (get_factorial(k) * get_factorial(n-k))
    return coefficient

"""
start_time = time.perf_counter()
binom_coeff(100,5) #350000,90
end_time = time.perf_counter()
elapsed = end_time - start_time
print("completed in " + str(elapsed) + " seconds")
"""

#binomial with recursion
#n Choose k = (n-1 Choose k-1) + (n-1 Choose k)
def binom_coeff_recur(n,k):
    if (n == k) or (k == 0):
        return 1
    else:
        return binom_coeff_recur(n - 1, k - 1) + binom_coeff_recur(n - 1, k)
  
"""
start_time = time.perf_counter()
binom_coeff_recur(100,5)
end_time = time.perf_counter()
elapsed = end_time - start_time
print("completed in " + str(elapsed) + " seconds")
"""

#memoisation
def binom_coeff_memo(n, k, memo={}):
    if (n,k) in memo:
        return memo[(n,k)]

    if k == 0 or k == n:
        return 1

    result = binom_coeff_memo(n - 1, k - 1, memo) + binom_coeff_memo(n - 1, k, memo)
    memo[(n, k)] = result

    return result

start_time = time.perf_counter()
binom_coeff_memo(20000,10000)
end_time = time.perf_counter()
elapsed = end_time - start_time
print("completed in " + str(elapsed) + " seconds")
