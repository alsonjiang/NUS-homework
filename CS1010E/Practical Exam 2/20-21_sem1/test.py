#game of life question
def create_zero_matrix(n, m):
  return [[0 for i in range(m)] for j in range(n)]

#3.1 add cells
def add_cells(board, cell_list):
    n, m = len(board), len(board[0]) #get rows and cols of board
    for x, y in cell_list:
        if (0 <= x <= n) and (0 <= y <= m):
            board[x][y] = 1

#3.2 simulate
#every step is a new board based on current cells' evolutions

def neighbour(board, i, j):
    result = 0
    n, m = len(board), len(board[0])

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == y == 0: #skip checking middle cell
                continue 
            if (0 <= x+i <= n) and (0 <= y+j <= m):
                result += board[x+i][y+j] #add 1 if neighbour is 1

    return result

def step(board):
    n, m = len(board), len(board[0])
    new_board = create_zero_matrix(m, n) #create new unfilled board
    for i in range(n):
        for j in range(m):
            neighbour_cells = neighbour(board, i, j) #checks neighbour cells

            if (board[i][j] == 1) and (2 <= neighbour_cells <= 3):
                new_board[i][j] = 1
            
            elif (board[i][j] == 0) and (neighbour_cells == 3):
                new_board[i][j] = 1
    
    return new_board



