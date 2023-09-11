from time import perf_counter
import sys

def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n,memo = {}) -> int:
    if n < 2:
        return n
    
    if n in memo:
        return memo[n]
    
    else:
        result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = result
        return result

if __name__ == '__main__':
    sys.setrecursionlimit(10_000)
    start = perf_counter()
    #result = fibonacci(50)
    result = fibonacci_memo(5000)
    end = perf_counter()

    print(result)
    print(f"{end-start} seconds")