#The Collatz conjecture states that n will eventually become 1, 
#regardless of which positive integer n is chosen initially

#recursive
def collatzRecursive(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + collatzRecursive(n//2)

    else:
        return 1 + collatzRecursive(n*3+1)
    
print(collatzRecursive(3))


#iterative
def collatzIterative(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            steps += 1
        else:
            n= (n * 3) + 1
            steps += 1
    return steps

print(collatzIterative(3))