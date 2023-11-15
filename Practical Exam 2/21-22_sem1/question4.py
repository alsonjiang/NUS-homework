#martian DNA
#child DNA is digit product of parent DNA

def child_DNA(d):
    res = 1
    while d:
        res *= d%10 #last digit
        d //= 10 #remove last digit
    return res
#print(child_DNA(262))

#after giving birth, parent DNA will mutate to 
#smallest integer that produce same digit product of child
def parent_mutated_DNA(d):
    children = child_DNA(d) #get the children DNA he produces
    possible_multiples = [children/integer for integer in range(1,10)] #gets a list of float and int multiples, i want the smallest int
    integer_multiples = [numbers for numbers in possible_multiples if numbers == int(numbers)] #shortlists only integers from the prev list
    smallest_integer_multiple = int(min(integer_multiples)) #take the smallest int possible
    mutation = str(smallest_integer_multiple) + str(children//smallest_integer_multiple) #concat the str of the smallest int with the other multiple
    
    return int(mutation) #turn into int-type

#print(parent_mutated_DNA(262))

def isMartian(d):
    pass


