#part 1
def fib_3_r(n: int) -> int: 

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1
    
    if n > 2:
        return fib_3_r(n-1) + fib_3_r(n-2) + fib_3_r(n-3) 
    
#print(fib_3_r(20))

def fib_3_i(n: int) -> int:
    output = [0, 1, 1]

    for i in range(3, n):
        new_term = output[i-1] + output[i-2] + output[i-3]
        output.append(new_term)
    
    final_sum = output[-1] + output[-2] + output[-3]

    return final_sum

#print(fib_3_i(20))

def sliding_window(array: list, window_size: int) -> int:
    #function searches for past n terms and add up.
    sub_array = array[-1 - window_size: ]
    return sum(sub_array)


def fibn_i(i: int, n: int) -> int:
    output = [0]
    for _ in range(0, n-1): #build the initial n-1 sequence
        output.append(1)
    
    for _ in range(n, i+1):
        new_term = sliding_window(output, n-1) #new term is the sum of past n terms
        output.append(new_term)

    return output[-1] #only return last digit of seq

print(fibn_i(13,5))

def fibn_r(i: int, n: int) -> int:
    output = [0]

    if i == 0:
        return output

    if i < n:
        output.append(1)
        return fibn_r(i-1, n) + output
    
    if i == n:
        new_term = sliding_window(output, n-1)
        output.append(new_term)
        return fibn_r(i-1, n) + output
    
    if i > n:
        return fibn_r(i-1, n) + output
    
#print(fibn_r(14,7))



#part 2
def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

def pizza_map(r: int, c: int, shops: list):
    board = create_zero_matrix(r, c) #a grid of all houses
    able_to_deliver = []

    for i in range(r):
        for j in range(c): #for every house on the grid
            for shop in shops: #for every shop in the list
                if shop.delivery_status(i, j): #use method to return T/F
                    able_to_deliver.append(shop.name) 
                else:
                    continue
                    
            if len(able_to_deliver) == 1: #only one shop True
                board[i][j] = able_to_deliver[0][:1] #only get first initial of shop
                able_to_deliver = [] #clear list
            
            elif len(able_to_deliver) > 1: #more than one shop True
                board[i][j] = 'X'
                able_to_deliver = [] #clear list

            else: #all shops False
                board[i][j] = '.'

    return board             
             
     
class Pizza_Shop: 
    def __init__(self, x, y, max_dist, name) -> None:
        self.x = x
        self.y = y
        self.max_dist = max_dist
        self.name = name
    
    def delivery_status(self, i, j) -> bool:
        #this method calculates manhattan distance from itself to a given house(i,j)
        #it then sees if the house is within its max distance or not
        manhattan = abs(self.x - i) + abs(self.y - j)
        if manhattan <= self.max_dist:
            return True
        else:
            return False
        

def mtp(m):
    for row in m:
        print(''.join(map(str, row)))

shops = [
    Pizza_Shop(3,3,3,'Ace Pizza'),
    Pizza_Shop(6,6,5, 'Bear Pizza')
]

#mtp(pizza_map(10,12,shops))

allPS = [Pizza_Shop(20,10,8, 'Amazing Pizza'), 
         Pizza_Shop(29,31,13, 'Beloved Pizza'),
         Pizza_Shop(38,20,10, 'Cute Pizza'),
         Pizza_Shop(45,55,20, 'Delicious Pizza'),
         Pizza_Shop(10,58,5, 'Elegant Pizza'),
         Pizza_Shop(35,68,7, 'Fancinating Pizza'),
         Pizza_Shop(32,60,11, 'Good Pizza')
]


#part 3
#find number of ways he can get to A, B
#first initialise the board 
def n_ways(A: int, B: int) -> int:
    board = create_zero_matrix(A, B)
    return board

#print(n_ways(1,2))

def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

#helper functions from tutorial 
def possibleNeighbours(matrix, i, j):
    height = len(matrix)
    width = len(matrix[0])

    allCandidates = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    output = []
    for candidates in allCandidates:
        if 0 <= candidates[0] < height:
            if 0 <= candidates[1] < width:
                if matrix[candidates[0]][candidates[1]] != 'blocked':
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