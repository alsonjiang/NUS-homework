### PE 02

"""
Question 3: Game of Life
"""
def create_zero_matrix(n, m):
  return [[0 for i in range(m)] for j in range(n)]


def m_tight_print(m):
  for row in m:
    print(''.join(map(str,row)))


def m_tight_print_gof(m):
  for row in m:
    print(''.join(map(lambda x: '#' if x == 1 else '_',row)))

"""
3.1 Add cells
  Write the function to add cells
"""
#each cell with 1 or less neighbours DIES
#each cell with 4 or more neighbours DIES
#each cell with 2 or 3 neighbours LIVES
#each cell (previously empty) with 3 neighbours becomes populated
def add_cells(board, cell_list):
  n,m = len(board),len(board[0])
  #n = rows, m = cols of the board = boundary

  for x,y in cell_list: #x=1st idx of every tup, y=2nd idx of every tup
    if 0 <= x < n and 0 <= y < m: #if both the x and y coord are inside the defined board
      board[x][y] = 1 #light up that coord


### Test data (do not modify)
very_long_house = [(5,6),(5,7),(5,8),(5,9),(5,10),(6,5),(6,8),(6,11),(7,5),(7,6),(7,10),(7,11)]
board = create_zero_matrix(2, 3)

### Test cases (comment out or remove before copying to Coursemology)
add_cells(board, [(1,2), (1,1), (1,0)])
#m_tight_print(board)
##add_cells(board, [(0,1), (1,1)])
##m_tight_print(board)


"""
3.2 Simulate
  Write the function to
  simulate game of life
"""
def neighbour(board,i,j): #given coord (i,j), check neighbouring cells
  res = 0
  n,m = len(board),len(board[0])
  for x in range(-1,2): #-1, 0, 1    
    for y in range(-1,2): 
      if x == y == 0: #skips center cell
        continue
      if 0 <= x+i < n and 0 <= y+j < m: #ensure neighbouring cells checked are within board boundaries
        res += board[x+i][y+j] #adds 1 to res if neighbours are 1
  return res

def step(board): #takes in a board, checks conditions, adds or deletes cells
  n,m = len(board),len(board[0]) #n=rows, m=cols of board (boundary)
  res = create_zero_matrix(n, m) #creates a new unfilled board with same dim
  for i in range(n):
    for j in range(m):
      nb = neighbour(board,i,j) #calculates how many neighbours the cell (i,j) has
      if board[i][j] == 1 and 2 <= nb <= 3: #following lines fulfil game conditions
        res[i][j] = 1
      elif board[i][j] == 0 and nb == 3: #if cell is 0 and has 3 neighbours, it comes alive
        res[i][j] = 1
  return res

### Test data (do not modify)
board0 = [[1,1,0,0],
          [1,1,1,1],
          [0,1,0,0]]
### Test cases (comment out or remove before copying to Coursemology)
##m_tight_print(board0)
##board1 = step(board0)
##m_tight_print(board1)
##board2 = step(board1)
##m_tight_print(board2)
