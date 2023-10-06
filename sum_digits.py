#sum up individual digits of a large number

#iterative
def sumDigitsIterative(n):
    result = 0
    while n > 0:
        result += n % 10 
        n = n //10

#recursive
def sumDigitsRecursive(n):
    if n == 0:
        return 0
    return n % 10 + sumDigitsRecursive(n // 10)