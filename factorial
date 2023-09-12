def fact(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    
    result = n * fact(n-1, memo)
    memo[n] = result
    return result