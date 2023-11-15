#task 1
def sum_of_3(L: tuple, n: int) -> bool:
    #find all possible triplets of numbers by finding subsets of 
    #L and discarding subsets that len() != 3
    number_triplets = [item for item in find_subsets(L) if len(item) == 3]
    sums_of_triplets = []
    for triplets in number_triplets:
        sums_of_triplets.append(sum(triplets))
    
    return (n in sums_of_triplets) #True if n is inside, False otherwise

def find_subsets(s):
    subsets = []
    n = len(s)
    
    # There are 2^n subsets
    for i in range(2**n):
        # For each subset, check which elements are included
        subset = [s[j] for j in range(n) if (i & (1 << j)) > 0]
        subsets.append(subset)
        
    return subsets

#print(sum_of_3((11,14,13,12), 39))
#print(sum_of_3(tuple(range(1,1000)),2500))