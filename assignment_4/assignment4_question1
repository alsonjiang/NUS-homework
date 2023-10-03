#cs = [3, -9, 1, 2] -> coefficients of [x^0, x^1, x^2, x^3]
#vp = 2 -> x = 2

def calc_poly(const_seq: list or tuple, var_poly: int or float) -> int or float:

    #create a new list for mutability, in case input is a tuple
    new_seq = [i for i in const_seq]

    #result of all calculations, an integer
    result = 0

    #calculate result, using index of list as powers of polynomial
    for item, value in enumerate(new_seq):
        value = value * (var_poly ** item)
        #new_seq[item] = value
        result += value

    #check for float, return result
    if type(result) is float:
        return round(result, 2)
    
    else:
        return result


print(calc_poly((3, -9, 1, 2), 2))