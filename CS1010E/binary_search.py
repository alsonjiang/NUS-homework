#binary search proper
def binary_search(key: int, seq: list) -> bool:
    def helper(low, high):
        if low > high:
            return False
    
        mid = (low + high) // 2
        
        if key == seq[mid]:
            return True
        
        elif key < seq[mid]:
            return helper(low, mid-1)
        
        else:
            return helper(mid+1, high)
    
    return helper(0, len(seq)-1)




#inefficient recursive implementation as you need to
#replicate the list over and over
def binary_search(key: int, seq: list) -> bool:
    if seq == []:
        return False
    
    mid = len(seq) / 2
    if key == seq[mid]:
        return True
    
    elif key < seq[mid]:
        return binary_search(key, seq[:mid])
    
    elif key > seq[mid]:
        return binary_search(key, seq[mid+1:])
    


    