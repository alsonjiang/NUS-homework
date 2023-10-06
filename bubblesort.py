def bubble_sort(arr):
    for i in range(len(arr)): # Traverse through all elements in the list
        swapped = False  # To optimize and break early if inner loop didn't do any swaps

        # Traverse the list from 0 to n-i-1. Last i elements are already in place
        for j in range(0, len(arr)-i-1):

            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in inner loop, then the list is sorted
        if not swapped:
            break

    return arr

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90, 0, -10, 3]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)