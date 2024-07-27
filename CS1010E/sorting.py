#sorting properties
#in-place: uses a small, constant amt of extra storage space, ie O(1) space
#stability: maintain relative order of items with equal keys, ie values


#selection sort
#from an unordered seq, pick a smallest (or largest)
#ensure that it is the smallest (or largest)
#remove it from the seq
#append it to a new seq, either from left to right, or right to left
a = [4,12,3,1,11]
sorted_seq = []

while a: # this means while a is not []
    smallest = a[0]
    for element in a:
        if element < smallest: #go through seq, see what is smallest
            smallest = element
    a.remove(smallest) #remove the smallest from seq
    sorted_seq.append(smallest) #append to sorted list

#time: worst, avg, best = O(n^2)
#space: O(1)
#in-place: NO (possible)
#stable: YES (maybe)

###########################################################################################

#merge sort (recursive)
#split into two halves and sort. combine halves.
#repeat with each half
#finally compare first elements of sorted stacks
#add each first element in order to a new seq

#first observation: base case n<2, return lst
#otherwise: divide lst into 2, sort each of them, merge

#how to merge? compare first elem, take smaller of the two
#repeat until no more elem
def merge_sort(lst: list) -> list:
    if len(lst) < 2: #base case, if lst only has 1 or 0 elem = sorted
        return lst
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid]) #sort left
    right = merge_sort(lst[mid:]) #sort right
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right: #while left and right != []
        if left[0] < right[0]:
            result.append(left.pop(0)) #appends the first elem from left lst while removing it from left lst
        else:
            result.append(right.pop(0)) #same but for right side

    result.extend(left)
    result.extend(right)
    return result

#time: worst, avg, best = O(nlogn)
#space: O(n)
#in-place: NO (possible)
#stable: YES

###########################################################################################

#bubble sort
def bubble_sort(arr):
    for i in range(len(arr)): # Traverse through all elements in the list
        swapped = False  # To optimize and break early if inner loop didn't do any swaps

        # Traverse the list from 0 to n-i-1. Last i elements are already in place
        for j in range(0, len(arr)-i-1):

            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True #flagging 

        # If no two elements were swapped in inner loop, then the list is sorted
        if not swapped:
            break

    return arr

#best used for small number of items
#best: n average: n^2, worst n^2

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90, 0, -10, 3]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


#bisection (binary sort)
#complexity: logn


#qSort (similar to Python's)