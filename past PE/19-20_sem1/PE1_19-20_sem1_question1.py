def sum_digit_square_I(n: int) -> int:
    output = 0

    while n > 0:
        #digit -> last digit of the number
        digit = n % 10

        #compute square of that digit, add to output
        output += digit * digit

        #remove the digit from the number
        n //= 10

    return output

#print(sum_digit_square_I(123456))

def sum_digit_square_R(n: int) -> int:
    output = 0

    if n <= 0:
        return 0
    
    else:
        digit = n % 10
        output += digit * digit
        return output + sum_digit_square_R(n//10)

#print(sum_digit_square_R(987654321))

def is_happy_number(n: int) -> bool:
    seen = {}

    sum = sum_digit_square_I(n)

    #mark result and itself as seen
    seen[sum] = 1
    seen[n] = 1

    while sum != 1 or sum != 7:
        if seen[sum] == 1: #if number is seen before
            return False #not happy number
        else:
            seen[sum] = 1 #add number to seen dict
            sum = sum_digit_square_I(sum) #re-run SDS with the new number

    return True

print(is_happy_number(7))

def all_happy_numbers(n: int, m: int) -> list:
    lst = []

    for number in range(min(n, m), max(n, m)):
        if is_happy_number(number) == True:
            lst.append(number)      

    return sorted(lst)

#print(all_happy_numbers(1, 70))
