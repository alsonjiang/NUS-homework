
def auspicious_number(n: int, bad: list) -> int:
    bad = [str(item) for item in bad]  # turn every digit in bad to string
    start, end = 10**(n-1), 10**n #generate range of digits of n digit numbers
    numbers = {i for i in range(start, end) if all(bad_digit not in str(i) for bad_digit in bad)}
    return len(numbers), numbers

#print(auspicious_number(1000, [4]))%1000000000
