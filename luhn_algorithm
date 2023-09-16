#Luhn algorithm is a checksum algorithm 
#typically used to validate a credit card numbers

def luhn(num):
    #turn num to a string, for character in num, turn to int, add to lst
    lst = [int(char) for char in str(num)]

    #sum of all numbers in lst
    total = 0

    check_digit = 0

    #double every second digit from rightmost
    #-1 to -11, every -2 index
    for i in range(-1, -len(lst)-1, -2):
        lst[i] *= 2

    for i in range(-1, -len(lst)-1, -2):
        if lst[i]%10 == 0:
            if lst[i] == 10:
                lst[i] = 1
            if lst[i] == 0:
                lst[i] = 0
        elif lst[i]%10 == lst[i]:
            lst[i] = lst[i]
        elif lst[i]%10 == lst[i] - 10:
            lst[i] = 1 + (lst[i]%10)

    for i in range(len(lst)):
        total += lst[i]
    
    check_digit = (10 - (total % 10)) % 10
        
    return check_digit

print(luhn(1234567890))

