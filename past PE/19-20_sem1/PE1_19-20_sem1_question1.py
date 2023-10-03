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

def is_happy_number(n: int, seen = []) -> bool:
    sum = sum_digit_square_I(n)

    if sum == 1:
        return True

    if sum in seen:
        return False

    else:
        return is_happy_number(sum, seen.append(sum))


#print(is_happy_number(849))

def all_happy_numbers(n: int, m: int) -> list:
    lst = [1,3,4,5, 2]

    return sorted(lst)


print(all_happy_numbers(1, 70))
