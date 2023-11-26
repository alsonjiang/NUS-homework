#check prime
def checkPrime(n):
    for i in range(2, n):
        if divisible(n, i):
            return False
    return True

def divisible(n, m):
    return n % m == 0 #return True if can divide fully (no remainders)

#exercise
#given a number n, find a prime >= n
def findPrimeGE(n):
    while checkPrime(n) != True:
        n += 1
    return n


#burger recursion
def burger(string):
    cost = 0
    cost_dict = {'B': 0.5, 'P': 2} #etc

    if not string:
        return cost
    
    else:
        try:
            cost += cost_dict[string[0].upper()]
            return burger(string[1:]) + cost
        
        except:
            print(f'An ingredient is not in the list: {string[0]}')
            return cost

#challenge A
def final_sum_recursive(n):
    # Base case: if n is a single digit, return n
    if n < 10:
        return n

    # Recursive case: sum the digits and make a recursive call
    return final_sum_recursive(sum(int(digit) for digit in str(n)))


print(final_sum_recursive(52634))






