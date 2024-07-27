#question 1

def how_many_male(faculty):
    males = 0

    lst = [i for i in faculty]
    for item in lst:
        if item == 'M':
            males += 1
        else:
            continue

    return males

def how_many_female(faculty):
    females = 0

    lst = [i for i in faculty]
    for item in lst:
        if item == 'F':
            females += 1
        else:
            continue

    return females

def gender_balance(faculty):
    if how_many_male(faculty) > how_many_female(faculty):
        return "male"
    elif how_many_female(faculty) > how_many_male(faculty):
        return "female"
    else:
        return "balanced"

#print(how_many_male('MMFMFFMMMF'))
#print(how_many_female('MMFMFFMMMF'))
#print(gender_balance("MMFMFFMMMF"))

#===================================================================#

#question 2
def catepillar(n):
    output = ''
    for i in range(n-1):
        output += 'Q'
    return output + '6'

#print(catepillar(4))

def catepillar_with_backside(n):
    output = ''
    for i in range(n-2):
        output += 'Q'
    return 'c' + output + '6'

#print(catepillar_with_backside(10))


        