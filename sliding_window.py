def slidingWindow(arr: list[str], target: list[str]) -> int:
    window_size = len(target)
    
    # Check if array length is less than target length
    if len(arr) < window_size:
        return -1

    for i in range(len(arr) - window_size + 1):
        subarray = arr[i:i + window_size]
        if subarray == target:
            return i  # Return starting index of the matching subarray
        
    # If no match is found, return -1
    return -1

#array = [1,2,3,4,5,6]
array = ["W", "T", "T", "W", "T", "T", "T"]
match = ['T', 'T', 'T']
print(slidingWindow(array, match))