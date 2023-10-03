"""
def auspicious_number(n: int, bad: list) -> int:
    for val in bad:
        val = str(val)
    numbers = {i for i in range(0, int('9'*n) + 1)}

    return bad

print(auspicious_number(2,[1,2,3]))

"""
def count_auspicious_numbers(n, bad, current='', count=0):
    # Base case: if the current number has n digits, increment the count
    if len(current) == n:
        count += 1
        return count
    
    for i in range(10):  # digits from 0 to 9
        if i in bad or (i == 0 and len(current) == 0):  # skip bad digits or leading zeros
            continue
        
        # Add the current digit to the number and recurse
        count = count_auspicious_numbers(n, bad, current + str(i), count)
    
    return count

def auspicious_number(n, bad):
    # Convert bad digits to a set for faster lookups
    bad = set(bad)
    return count_auspicious_numbers(n, bad)

# Test the function
n = 2
bad = [1,3]
result = auspicious_number(n, bad)
print(result)  # Output: 72
