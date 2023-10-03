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
    
#print(is_unique(['a','b',3,True,999,'a']))

#not allowing len() and range()
def is_unique_complicated(seq) -> bool:
    #count the number of duplicates
    count = 0

    #double pointers
    i, j = 0, -1
    while i != -1 and j >= 0 and i < j:
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

print(is_unique_complicated(['a','b',3,True,999,'a']))