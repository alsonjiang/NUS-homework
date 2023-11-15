#super fibonacci sequence
#recursive
def super_fib_R(term2: int, n: int) -> list:

    if n == 0:
        return []

    if n == 1: #base case, n == 1
        return [1]
    
    if n == 2: #base case, n == 2
        return [1, term2]
    
    if n > 2:
        previous_terms = super_fib_R(term2, n-1)
        new_term = sum(previous_terms)
        return previous_terms + [new_term]
    
#print(super_fib_R(10, 10))

#iterative
def super_fib_I(term2: int, upper: int) -> list:
    output = [1, term2]

    while True:
        next_term = sum(output)
        if next_term <= upper:
            output.append(next_term)
        else:
            break
            
    return output

#print(super_fib_I(4, 100))

#smallest second
def smallest_second(n: int):
    
