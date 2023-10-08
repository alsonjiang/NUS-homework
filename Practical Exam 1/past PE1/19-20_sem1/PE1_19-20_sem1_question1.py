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
    seen = []
    if n < 10:
        if n == 1 or n == 7:
            return True
        else:
            return False

    else:
        while n >= 10:
            result = sum_digit_square_I(n)
            if result < 10:
                break 
            else:
                if result in seen:
                    return False
                else:
                    seen.append(result)
                    result = sum_digit_square_I(result)

#print(is_happy_number(97))

def all_happy_numbers(n: int, m: int) -> list:
    lst = []

    for number in range(min(n, m), max(n, m)):
        if is_happy_number(number) == True:
            lst.append(number)      

    return sorted(lst)

#print(all_happy_numbers(1, 70))
