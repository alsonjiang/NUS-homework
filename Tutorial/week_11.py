#searching and sorting
from random import randint

#bubblesort -> O(n^2)
def bubble(array: list) -> list:
    for i in range(len(array) - 1):
        swapped = False

        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        
        if not swapped:
            break

    return array


L = [3, 2, 5, 5, 7, 1, 4]

n = 100000
L2 = [randint(0, 100000) for i in range(n)]


#binary search
#this implementation returns the index where we should insert our value in a sorted list
def binary_search(array: list, x: int) -> int:
    low = 0
    high = len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] < x: #if True, our target is in right half
            low = mid + 1
        else: #else, our target is in the left half
            high = mid
    return low

sorted_L = [1,2,3,4,5,6,8,9]
print(binary_search(sorted_L, 7))


#merge sort -> O(nlogn)
#divide = split array into 2 halves
#conquer = recursively sort the 2 halves
#combine = merge the sorted halves

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

#print(merge_sort(L2))