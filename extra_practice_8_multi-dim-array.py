import pprint

lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#snake game
def vertical_snake(L):
    final_output = ''
    for i in range(0, len(L[0])):
        final_output += collect_pattern(L, i)

    return final_output
   
def collect_pattern(L, column):
    output = ''
    for i in range(len(L)):
        output += L[i][column]

    if column % 2 == 0:
        return output
    else:
        return output[::-1] #reversed

#print(vertical_snake(lst))

#rotate clockwise = 1. transpose matrix (swap rows and cols)
#                   2. reverse order of elems in each row
def rotate_cw(matrix):
    #step 1
    transposed = [list(row) for row in zip(*matrix)]
    #step 2
    clockwise = [row[::-1] for row in transposed]

    return clockwise

#pprint.pprint(rotate_cw(lst))

#rotate counter clockwise
def rotate_ccw(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    matrix = transposed[::-1]
    return matrix

#pprint.pprint(rotate_ccw(lst))

#local maxima
def local_maximum(L):
    # Get the number of rows and columns
    rows, cols = len(L), len(L[0]) if L else 0
    
    # Function to get the value of a cell, returning -inf if out of bounds
    def get_value(i, j):
        if 0 <= i < rows and 0 <= j < cols:
            return L[i][j]
        return float('-inf')
    
    # Check if the current cell is a local maximum
    def is_local_maximum(i, j):
        value = L[i][j]
        # Check all four neighbors (up, down, left, right)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if value < get_value(i + di, j + dj):
                return False
        return True
    
    # Count the local maximums
    count = 0
    for i in range(rows):
        for j in range(cols):
            if is_local_maximum(i, j):
                count += 1
    return count

#n-Queen
def queens(L: list) -> bool:

    rows = len(L)

    #check rows and cols for more than one queen
    for i in range(rows):
        if sum(L[i]) > 1: #each row, more than one queen
            return False
        
        if sum(L[i][j] for j in range(rows)) > 1: #every cols, more than one queen
            return False
    
    #check diagonals
    for i in range(-rows + 1, rows):
        if sum(L[j][i + j] for j in range(max(0, -i), min(rows, rows - i)) if 0 <= i + j < rows) > 1:
            return False
        if sum(L[j][rows - 1 - i - j] for j in range(max(0, -i), min(rows, rows - i)) if 0 <= rows - 1 - i - j < rows) > 1:
            return False
        
    return True

L = [
    [0, 0, 1, 0], 
    [1, 0, 0, 0],
    [0, 0, 0, 1], 
    [0, 1, 0, 0]
     ]

print(queens(L))




#check diagonals from current position
def diagonals(current_x, current_y, L): #(0,0)
    positions = []
    rows, cols = len(L), len(L[0])
    top_right = (current_x-1, current_y+1) #(-1,1)
    top_left = (current_x-1, current_y-1) #(-1,-1)
    bottom_right = (current_x+1, current_y+1) #(1,1)
    bottom_left = (current_x+1, current_y-1) #(1,-1)
    possible_diagonal_positions = [top_right, top_left, bottom_right, bottom_left]

    for i in range(rows):
        for j in range(cols):
            if (i, j) in possible_diagonal_positions:
                positions.append((i,j))
                

    return positions


        
