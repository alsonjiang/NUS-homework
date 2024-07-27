#tuple L will only be +ve integers or nothing
#+ve integers can be any integer > 0

def min_no_of_turns(L: tuple) -> int:
    moves = 0 #to count number of moves

    if not L: #input is empty
        return 0
    
    else:
        lst = sorted(L) #sort the array in ascending order
        while lst: #while list is not empty [1, 1, 2, 3, 5, 6, 7, 8]
            max_length = 1
            max_index = 0

            #find the longest consecutive subsequence
            for i in range(len(lst)):
                current_length = 1
                while (i + current_length < len(lst)) and (lst[i + current_length] == lst[i] + current_length): 
                    #ensure subsequence does not exceed length of list AND ensure next elem is equal to one greater than current elem
                    current_length +=1 #extend the subsequence to cover next elem
                
                if current_length > max_length: #once found a new longest subsequence
                    max_length = current_length #update the max_length value
                    max_index = i #save the starting index of the new longest subsequence

            if max_length == 1: #no more consecutive subsequence, only individual numbers
                return moves + len(lst) 
                #num of moves to clear individual nums = length of the array *mindblown*
                #eg. [3,6,9] needs 3 moves to clear 3 nums
            
            #if there are subsequences available to clear
            lst = lst[:max_index] + lst[max_index + max_length:] 
            #returns everything before index to be cut, and everything after index+length of subsequence
            moves += 1

    return moves

#print(min_no_of_turns((1, 8, 3, 6, 5, 7, 2, 1)))