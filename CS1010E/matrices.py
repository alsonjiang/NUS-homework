import pprint
import matplotlib as plt
#formats lists of lists nicer in output
m2 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20]]
#pprint.pprint(m2)

#create a NxN identity matrix 
#having a matrix with all 0, except diagonal all 1
#square matrix -> num rows = num cols
def identityMatrix(N):
    output = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(1 if i==j else 0)
        output.append(row)
    return output

#pprint.pprint((identityMatrix(10)))

#tightprint
#same as NxN identity matrix, but in str, not lists
def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

#create RxC Zero matrix
def createZeroMatrix(r, c):
    output= []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output

m = createZeroMatrix(4,9)
#pprint.pprint(m)

#shorter code to create zero matrix
#downside = changing one specific index, eg [0][0], changes
#every first object of every list
def create_M(r, c):
    one_row = [0] * c
    return [one_row] * r
#hence,
def create_M(r, c):
    one_row = [0] * c
    return [one_row.copy() for _ in range(r)]
 
#matrix addition
def sumMatrix(m1, m2):
    r = len(m1)
    c = len(m1[0])
    output = createZeroMatrix(r, c)
    for i in range(r):
        for j in range(c):
            output[i][j] = m1[i][j] + m2[i][j]
    return output

#matrix transpose
def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

#matrix inverse


#determinant


#minor
#a minor of a matrix A is the determinant of some smaller square matrix


#maze solving!!!
#BFS (breadth first search)
from collections import deque
import random

def solve_maze(maze, start, end):
    # The queue for the BFS algorithm
    queue = deque([start])
    # A dictionary to keep track of where we came from
    came_from = {start: None}

    while len(queue) > 0:
        current = queue.popleft()

        # If we've reached the end, we're done
        if current == end:
            break

        # Get the neighbors of the current cell
        neighbors = get_neighbors(maze, current)

        for neighbor in neighbors:
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    # If we didn't find the end, there's no solution
    if end not in came_from:
        return None

    # Build the path from start to end
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

def get_neighbors(maze, cell):
    # Returns the accessible neighbors of a cell in the maze
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = cell[0] + dx, cell[1] + dy
        if (0 <= new_x < len(maze)) and (0 <= new_y < len(maze[0])) and maze[new_x][new_y] != 'X':
            neighbors.append((new_x, new_y))
    return neighbors

#create random maze 50/50 chance of blocked or path
#blocked== 1, path == 0
def createRandomMaze(n, m):
    # Initialize an empty maze
    maze = []
    for _ in range(n):
        row = []
        for _ in range(m):
            # For each cell, randomly choose between empty (0) and blocked (1)
            cell = random.choice(['0', '1'])
            row.append(cell)
        maze.append(row)
    return maze

def mTightPrint(maze):
    for row in maze:
        print(''.join(row))

new_maze = createRandomMaze(10,10)
mTightPrint(new_maze)

print(solve_maze(new_maze, (0,0), (9,9)))

def possibleNeighbours(matrix, i, j):
    height = len(matrix)
    width = len(matrix[0])

    allCandidates = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    output = []
    for candidates in allCandidates:
        if 0 <= candidates[0] < height:
            if 0 <= candidates[1] < width:
                if matrix[candidates[0]][candidates[1]] != 1:
                    output.append(candidates)
    return output

def isSolvable(maze):
    if maze[0][0] == 1:
        return False
    visited = [[0,0]] #record those positions we visited before
    S = [[0,0]] #all possible neighbours to try
    while S:
        position = S.pop()
        if position[0] == (len(maze)-1) and position[1] == (len(maze[0]) - 1):
            return True
        possible_neighbours = possibleNeighbours(maze, position[0], position[1])
        for new_position in possible_neighbours:
            if new_position not in visited:
                visited.append(new_position)
                S.append(new_position)
    
    return False


#how to check if maze is not solvable

#algorithm 2
#simplest / brute force -> store all possible routes in a collection then check which one has no blockage


#queue based logic
#how to get all binary numbers from 0 to n (example)
def get_all_binary(n):
    queue = [""]
    for _ in range(n):
        x = queue[0]
        queue.remove(x)
        y = x + '0'
        queue.append(y)
        z = x + '1'
        queue.append(z)

    return queue

#print(get_all_binary(3))


#=========================================================================================#
#tic-tac-toe game
# 1|2|3
# 4|5|6  --> positions -> coordinates (i, j)
# 7|8|9
#i = (position -1) // 3
#j = (position -1) % 3
#if only given (i, j), how to find the position?
#position = i x 3 + j + 1
#general form -> position = i x n + j + 1, for m x n matrix (row x cols), starting (0,0)
def printTTT(game):
    for i in range(3):
        print(f'{game[i][0]} | {game[i][1]} | {game[i][2]}')
        if i != 2:
            print('-----')

def tttGamePlay():
    game = createZeroMatrix(3, 3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i * 3 + j + 1 #numbering each position 
    player = 0
    piece = ['X', 'O']

    printTTT(game)
    for i in range(9):
        position = int(input(f'Player {piece[player]} move: ')) - 1
        game[position // 3][position % 3] = piece[player]
        player = 1 - player #switches the player (toggling)
        printTTT(game)

#problems. 1)can replace previous move. 2)no win condition
#tttGamePlay()

#soduku game for PE!!


#make a circle picture
def circlePic():
    l = 300
    center = 1/2
    pic = createZeroMatrix(1, 1)
    for i in range(l):
        for j in range(l):
            if (1/3)**2 < (i-center)**2 + (j-center)**2 < (1/2)**2:
                pic[i][j] = [0, 0, 255]
            else:
                pic[i][j] = [255, 0, 0]
    plt.imshow(pic)
    plt.show()

#circlePic()


#reading csv files easier method, no need strip(), split(), etc
#birth_file = open('(file_name)')
#birth_file_reader = csv.reader(birth_file)
#birth_data = list(birth_file_reader)

lst1 = ['bc','de','ya','ab','bq','bd']
lst2 = []
for x in lst1:
 lst2.append(tuple(x))
d = dict(lst2)
#print(d['b'])
#print(lst2)