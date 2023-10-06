'''
def is_unique(seq) -> bool:
    #count the number of duplicates
    count = 0
    
    #double pointers
    i, j = 0, len(seq) - 1

    while i <= len(seq) - 1 and j >= 0 and i < j:
        i_char = seq[i]
        j_char = seq[j]

        if i_char == j_char:
            count += 1
            i += 1
            j -= 1
        
        else:
            i += 1
        
        j -= 1
    
    if count == 0:
        return True
  
    return False
'''

def is_unique(seq) -> bool:
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] == seq[j]:
                return False
    return True

#print(is_unique(['a','b',3,True,999,'a']))
#print(is_unique([1,2,3,4]))

#not allowing len() and range()
def is_unique_complicated(seq) -> bool:
    for i, item1 in enumerate(seq):
        for item2 in enumerate(seq):
            if item1 == item2[1] and i != item2[0]:  # If items are the same and indices are different
                return False
    return True

#print(is_unique_complicated(['a','b',3,True,999,'a']))