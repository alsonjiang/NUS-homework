from functools import reduce

def sum_squares(n):
    #only return the values that are multiples of 2 or 3.
    lst= filter(lambda x: x%2 == 0 or x%3 == 0, range(1, n+1))
    #for every value in the lst
    return reduce(lambda accumulate, x: accumulate + x**2, lst, 0) 

#print(sum_squares(3))

def dot_product(a: list, b: list) -> int:
    ab = [a_vals * b_vals for a_vals, b_vals in zip(a, b)]  #lists elem-wise multiplication
    return reduce(lambda accumulate, val: accumulate + val, ab)

    #single line, without using for loops, only map and reduce
    #return reduce(lambda x, y: x + y, map(lambda a_vals, b_vals: a_vals * b_vals, list_a, list_b))
#print(dot_product([4, 3], [2, 1]))


#count distinct values of x^2 % n, for 0 <= x <= n-1
def count_distinct_squares_mod_n(n):
    distinct_values = set()
    for x in range(n):  # x from 0 to n-1
        distinct_values.add(x**2 % n)
    return len(distinct_values)

# Example usage:
n = 4
print(count_distinct_squares_mod_n(n))  # Output will be 2

#better version of the function above
def residue(n):
    lst_of_values = map(lambda x: (x**2)%n, range(n)) #every value from 0 to n-1, square and mod n.
    return len(set(lst_of_values)) #make list of calculated values into set, count length. 
    #this returns number of unique values


#question 4: sorting
#sort lower cases then concat w upper cases
def sort_strings(lst_strings):
    lower_cases = filter(str.islower, lst_strings)
    upper_cases = filter(str.isupper, lst_strings)

    lowercase_concatenated = reduce(lambda x, y: x + y, lower_cases, '')
    uppercase_concatenated = reduce(lambda x, y: x + y, upper_cases, '')

    return lowercase_concatenated + uppercase_concatenated

#print(sort_strings(['AA', 'dd', 'C', 'b']))


def find_subsets(s):
    subsets = []
    n = len(s)
    
    # There are 2^n subsets
    for i in range(2**n):
        # For each subset, check which elements are included
        subset = [s[j] for j in range(n) if (i & (1 << j)) > 0]
        subsets.append(subset)
        
    return subsets


def distinct_substrings(s):
    unique_substrings = set()

    for i in range(len(s)): #A A A A, 0 to 3
        for j in range(i+1, len(s)+1): #1 to 3
            unique_substrings.add(s[i:j])

    return len(unique_substrings) #A A A A