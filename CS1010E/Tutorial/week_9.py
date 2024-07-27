#Multi-dim arrays
from pprint import pprint
from random import randint

#create zero matrix:
def create_zero_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([0] * cols)

    return matrix

#print(create_zero_matrix(2,3))


#part 1: matrix

#task 1 -> transpose, matrix m (r x c) becomes matrix m (c x r)
mat = [[1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
      [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
      [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]]

def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    output = [[0 for _ in range(rows)] for _ in range(cols)] #create transposed zero matrix (cols x rows)
    for i in range(rows):
        for j in range(cols):
            output[j][i] = matrix[i][j]
    return output


def transpose_one_liner(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


#pprint(transpose_one_liner(mat))
#pprint(transpose(mat))


#task 2 -> matrix multiplication
#multiply row of 1st array by col of 2nd array 
#m1 col == m2 row for operation to work.

mat_1 = [[1,2,3],[5,6,7],[9,10,11],[13,14,15]] #M x N = 4x3
mat_2 = [[4,3,2,1,8,1],[1,2,3,4,3,1],[5,6,7,8,1,2]] #N x P = 3x6

def matrix_multiplication(m1, m2):
    m1_row, m1_col = len(m1), len(m1[0]) 
    m2_row, m2_col = len(m2), len(m2[0]) 

    m3 = [[0 for _ in range(m2_col)] for _ in range(m1_row)] #resultant = M x P =  4x6

    for i in range(m1_row):
        for j in range(m2_col):
            for k in range(m1_col):
                m3[i][j] += m1[i][k] * m2[k][j]
    
    return m3

#pprint(matrix_multiplication(mat_1,mat_2))


#task 3 -> minor matrix
#remove row i and column j of a given matrix to form a minor matrix

mat_3 = [[21, 25, 29, 33, 17, 9],
        [61, 69, 77, 85, 65, 25],
        [101, 113, 125, 137, 113, 41],
        [141, 157, 173, 189, 161, 57]]

def minor_matrix(array, i, j):
    minor = []
    new_rows = array[:i] + array[i+1:] #cut the unwanted row, i
    for rows in new_rows:
        new_cols = rows[:j] + rows[j+1:]
        minor.append(new_cols)
    
    return minor

def minor_matrix_one_liner(array: list, i: int, j: int) -> list:
    return [row[:j] + row[j+1:] for row in (array[:i]+array[i+1:])]

#print(minor_matrix_one_liner(mat_3, 2, 3))
#print(minor_matrix(mat_3, 2, 3))


#task 4: determinant
#must be a square matrix
#if the minor is not 2x2 -> recursion

def determinant(array: list) -> int:

    def find_determinant(array):
        result = 0
        if len(array) == 1: #1x1
            return array[0][0]
        if len(array) == 2: #2x2
            return (array[0][0] * array[1][1]) - (array[0][1] * array[1][0])
        else:
            for i in range(rows):
                result += ((-1) ** i) * array[0][i] * find_determinant(minor_matrix(array, 0, i)) #need to use minor matrix function + recursion
        
        return result
        
    rows, cols = len(array), len(array[0])

    if rows != cols: #if not square matrix
        return "Cannot be found"
    else:
        return find_determinant(array)
    

m = [[6,1,1],[4,-2,5],[2,8,7]]
#print(determinant(m))


#part 2: maze

#task 1 -> create random maze
#0 = path, 1 = blocked, M x N matrix
def create_random_maze(rows: int, cols: int) -> list:
    matrix = create_zero_matrix(rows, cols)
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = randint(0,1)
    return matrix    

#pprint(create_random_maze(5,2))

#task 2 -> maze solving
#check neighbours & returns a list of possible coords to go to
#up, down, left, right from current coord
def possibleNeighbours(matrix: list, i: int, j: int, max_r: int, max_c: int) -> list:
    valid_neighbours = [] #coords OK to go next
    possible_neighbours = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]] #up, down, left, right from current coord
    #max_rows, max_cols = len(matrix) - 1, len(matrix[0]) - 1 #matrix boundaries
    for neighbours in possible_neighbours:
        if (0 <= neighbours[0] <= max_r) and (0 <= neighbours[1] <= max_c): #check if within boundaries
            if matrix[neighbours[0]][neighbours[1]] == 0: #check if path is 0 == clear
                valid_neighbours.append(neighbours) #append valid move to output
    
    return valid_neighbours #returns a list


#returns T or F if a maze is solvable (able to go from (0,0) to (m-1, n-1))
def isSolvable(maze: list) -> bool:
    max_row, max_col = len(maze) - 1, len(maze[0]) - 1

    if maze[0][0] == 1: #check if starting point is blocked
        return False 
    
    visited = [[0,0]] #initialise a list of visited coords
    S = [[0,0]] #all possible neighbours we want to try

    while S: #while there is still a coord to try...
        position = S.pop() #removes a coord in S and returns it as a position
        if (position[0] == max_row) and (position[1] == max_col): #endpoint reached
            return True
        
        possible_moves = possibleNeighbours(maze, position[0], position[1], max_row, max_col) #check UDLR for moves
        for moves in possible_moves:
            if moves not in visited:
                visited.append(moves)
                S.append(moves)

    return False


maze = create_random_maze(15,30)
print(maze)
print(isSolvable(maze))    