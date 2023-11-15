#part 1
def fib_3_r(n: int): 

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1
    
    if n > 2:
        previous_terms = fib_3_r(n-1) + fib_3_r(n-2) + fib_3_r(n-3)
        new_term = sum(previous_terms)
        return previous_terms + new_term
    
print(fib_3_r(5))




































#iterative and recursive

#reverse string
def reverseString(s):
    output = ''
    l = len(s)
    for i in range(l):
        output += s[l-i-1] #5-0-1, #5-1-1, ...
    return output

def reverseString2(s):
    output = ''
    for char in s:
        output = char + output #must be char + output
    return output

def reverseStringRecursive(s):
    if not s:
        return ''
    return reverseStringRecursive(s[1:]) + s[0]

#fibonacci
def super_fib_R(term2: int, n: int) -> list: #recursive super fib

    if n == 0:
        return []

    if n == 1: #base case, n == 1
        return [1]
    
    if n == 2: #base case, n == 2
        return [1, term2]
    
    if n > 2:
        previous_terms = super_fib_R(term2, n-1)
        new_term = sum(previous_terms)
        return previous_terms + [new_term]
    
def super_fib_I(term2: int, upper: int) -> list: #iterative super fib
    output = [1, term2]

    while True:
        next_term = sum(output)
        if next_term <= upper:
            output.append(next_term)
        else:
            break
            
    return output

#encryption/decryption
def encode_I(s1: str, s2: int, m: int) -> str: #iterative encode
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = '' #final output to be concat-ed
    count = 0 #used to iterate through s2

    for char in s1:
        transformed_char = letters.index(char) + ( int(s2[count]) * m ) 
        #take the corresponding digit in s2, turn to int, multiply by m, find this result in the letters list
        output += str(letters[transformed_char % len(letters)])
        #find the result in letters list with % to allowing list wrapping, turn to str, concat to output
        count += 1
        #add count to be able to iterate through next val of s2

    return output

def encode_I_shortcut(s1, s2, m): 
    ans = ''
    for i in range(len(s1)):
        ans += chr(ord('a') + ((ord(s1[i]) - ord('a') + (int(s2[i])*m))%26))
    return ans

def encode_R(s1: str, s2: int, m: int) -> str: #recursive encode
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if not s1:
        return ''
    
    transformed_char = letters.index(s1[0]) + ( int(s2[0]) * m )
    output = str(letters[transformed_char % len(letters)])
    return output + encode_R(s1[1:], s2[1:], m)


#map, filter, reduce
from functools import reduce

def sum_squares(n):
    #only return the values that are multiples of 2 or 3.
    lst= filter(lambda x: x%2 == 0 or x%3 == 0, range(1, n+1))
    #for every value in the lst
    return reduce(lambda accumulate, x: accumulate + x**2, lst, 0) 

def dot_product(a: list, b: list) -> int:
    ab = [a_vals * b_vals for a_vals, b_vals in zip(a, b)]  #lists elem-wise multiplication
    return reduce(lambda accumulate, val: accumulate + val, ab)

    #single line, without using for loops, only map and reduce
    #return reduce(lambda x, y: x + y, map(lambda a_vals, b_vals: a_vals * b_vals, list_a, list_b))

#count distinct values of x^2 % n, for 0 <= x <= n-1
def count_distinct_squares_mod_n(n):
    distinct_values = set()
    for x in range(n):  # x from 0 to n-1
        distinct_values.add(x**2 % n)
    return len(distinct_values)

# Example usage:
n = 4
#print(count_distinct_squares_mod_n(n))  # Output will be 2

#better version of the function above
def residue(n):
    lst_of_values = map(lambda x: (x**2)%n, range(n)) #every value from 0 to n-1, square and mod n.
    return len(set(lst_of_values)) #make list of calculated values into set, count length. 
    #this returns number of unique values

#question 4: sorting
#sort lower cases then concat w upper cases
def sort_strings(lst_strings):
    lower_cases = filter(str.islower, lst_strings)
    upper_cases = filter(str.isupper, lst_strings)

    lowercase_concatenated = reduce(lambda x, y: x + y, lower_cases, '')
    uppercase_concatenated = reduce(lambda x, y: x + y, upper_cases, '')

    return lowercase_concatenated + uppercase_concatenated


#I/O
#python I/O
def write_something():
    with open('my_file.txt', 'w') as f:
        f.write("This is my first line" + "\n")
        f.write("This is my second line" + "\n")

#rstrip(), lstrip(), split() to remove all invisible character like \n
def read_something():
    with open('my_file.txt', 'r') as f:
        for line in f:
            pass
            #print(line.rstrip('\n').split(','))

#subset
def find_subsets(s):
    subsets = []
    n = len(s)
    
    # There are 2^n subsets
    for i in range(2**n):
        # For each subset, check which elements are included
        subset = [s[j] for j in range(n) if (i & (1 << j)) > 0]
        subsets.append(subset)
        
    return subsets

#deep copy, flatten
def deepCount(seq):
    if seq == []:
        return 0
    elif type(seq) != list:
        return 1
    else:
        return deepCount(seq[0]) + deepCount(seq[1:])
    
#square every item, including those in lists in the list
def deepSquare(seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return seq*seq
    else:
        return [deepSquare(seq[0])] + deepSquare(seq[1:])

#increment every item by 1
def deepIncrement(seq):
    if seq == [] or seq == ():
        return seq
    elif type(seq) != list:
        return seq + 1
    else:
        return [deepIncrement(seq[0])] + deepIncrement(seq[1:]) 
    
#deep map!
def deepMap(func, seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return func(seq)
    else:
        return [deepMap(func,seq[0])] + deepMap(func, seq[1:])

lst = [1, 2, 3, [1, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]
res = deepMap(lambda x: x/2, lst)
#print(res)

#deep copy illustration
lst2 = lst.copy()
#this .copy() is a shallow copy
#changing lst items changes lst2 items as well

lst3 = deepMap(lambda x:x, lst)
#lst3 is a deep copy of lst
#changing lst items does NOT change lst3 items

#print(lst) #[1, 2, 3, [1, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]
lst[3][0] = 999
#print(lst2) #[1, 2, 3, [999, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]
#print(lst3) #[1, 2, 3, [1, 2], [2, 3, 4, [1, 2, 3]], [3, 4, 5]]

#purpose of deep copy -> copying directories 
#map() is a powerful function, solve graphs, n-dim, trees

#if I just want to output a list with all elements, stipped of nested lists
def flatten(seq):
    if seq == []:
        return seq
    elif type(seq) != list:
        return [seq]
    else:
        return flatten(seq[0]) + flatten(seq[1:])

flatten_lst = flatten(lst)
#print(flatten_lst) #[1, 2, 3, 999, 2, 2, 3, 4, 1, 2, 3, 3, 4, 5]

#matrices/ matrix/ 2D array

def m_tight_print(m):
  for row in m:
    print(''.join(row))
  
def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

#snake
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

#maze
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

#HOFs/ accumulate function
#need to make op -> operation
#and pred -> satisfies requirement
def cond_sum(op, init, pred, limit):
    res = init
    for i in range(limit):
        if pred(i) == True:
            res = op(res, i)
    return res

def add(x, y): #to be put into op
    return x + y

def satisfies_property(x): #to be put into pred
    if (x>0) and (x % 2 == 0):
        return True
    else:
        return False
    
def sum_even(n): #main function that calls HOF 
    return cond_sum(add, 0, satisfies_property, 2*n+2)


#tuple and tuple interleaving
def interleaved_tuple(tuple_a,tuple_b):
    interleaved = ()
    counter = 0

    for i, j in zip(tuple_a, tuple_b):
        interleaved += (i, j)
        counter += 1
    for i in range(counter,max(len(tuple_a), len(tuple_b))):
        if tuple_a not in interleaved:
            interleaved += (tuple_a[i],)
        if tuple_b not in interleaved:
            interleaved += (tuple_b[i],)

    return interleaved

def interleaved_tuple_adv(tuple_a,tuple_b):
    interleaved = ()
    len_a, len_b = len(a), len(b)
    max_len = max(len_a, len_b)

    for i in range(max_len):
        if i < len_a:
            interleaved += (tuple_a[i],)
        if i < len_b:
            interleaved += (tuple_b[i],)

    return interleaved


#product
#print(product('ab', 3))
#print(product('xyz', 2))
#['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
#['xx', 'xy', 'xz', 'yx', 'yy', 'yz', 'zx', 'zy', 'zz']
def product(s, n):
    if n == 0:
        return ['']  # Base case: single empty string for 0-length product
    if n == 1:
        return list(s)  # Base case: single characters for 1-length product
    
    # Get the product of s with n-1
    prev_product = product(s, n - 1)
    
    # Now, prepend each character of s to each item in the previous product
    result = []
    for char in s:
        for item in prev_product:
            result.append(char + item)
    
    return result


#past PE questions
#Pizza class extra functions
class PizzaShop:
    def __init__(self, pos, name, radius, hour_s, hour_e):
        self.pos = pos
        self.name = name
        self.radius = radius
        self.hour_s = hour_s
        self.hour_e = hour_e

    def is_open(self, hour):
        return self.hour_s <= hour < self.hour_e

    def distance_square_to(self, i, j):
        return (self.pos[0] - i) ** 2 + (self.pos[1] - j) ** 2

    def can_deliver_to(self, i, j, hour):
        return self.distance_square_to(i,`` j) <= self.radius and self.is_open(hour)


def pd_map(r, c, all_shops, hour):
    map_grid = [['.' for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            min_distance = float('inf')
            closest_shops = []

            for shop in all_shops:
                if shop.can_deliver_to(i, j, hour):
                    distance = shop.distance_square_to(i, j)
                    if distance < min_distance:
                        min_distance = distance
                        closest_shops = [shop]
                    elif distance == min_distance:
                        closest_shops.append(shop)

            if len(closest_shops) == 1:
                map_grid[i][j] = closest_shops[0].name[0]
            elif len(closest_shops) > 1:
                map_grid[i][j] = 'X'

    return map_grid


# Example Usage
all_shops = [
    PizzaShop([3, 3], 'Ace', 3, 8, 14),
    PizzaShop([6, 6], 'Bizza', 4, 12, 22)
]

# Print maps for different hours
hours = [10, 12, 16]
r, c = 10, 12

for hour in hours:
    delivery_map = pd_map(r, c, all_shops, hour)
    print(f"Map for hour {hour}:")
    for row in delivery_map:
        print(''.join(row))
    print("\n")


#prince map
import pprint
def crop_map(filename, minr: int, maxr: int, minc: int, maxc: int) -> list:
    map_data = []
    map_data_cropped = []
    with open(filename, 'r') as f:
        for line in f:
            map_data.append(line.strip())

    max_row, max_col = len(map_data), len(map_data[0]) #get boundaries

    #redefine input boundaries if they are out of bounds of current map
    minc = max(0, minc)
    maxc = min(max_col, maxc)
    minr = max(0, minr)
    maxr = min(max_row, maxr)
    
    map_data_cropped = [row[minc:maxc+1] for row in map_data[minr:maxr+1]] #edit map_data to keep only target ranges of rows and cols
    return map_data_cropped

#pprint.pprint(crop_map("./Practical Exam 2/22-23_sem1/map1.txt",5,9,3,25))

def island_area(filename, prince):
    # Initialize area to 0
    area = 0

    # Open and read the file
    with open(filename, 'r') as f:
        map_data = [list(line.strip()) for line in f] #same as for line.strip in f, append map_data 

    # Find the prince's position
    prince_pos = [(i, j) for i, row in enumerate(map_data) for j, cell in enumerate(row) if cell == prince]
    if not prince_pos: 
        return 0

    # Define the directions for DFS
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # DFS function
    def dfs(pos):
        nonlocal area #to access area variable at the top of the main function
        x, y = pos
        if not(0 <= x < len(map_data) and 0 <= y < len(map_data[0]) and (map_data[x][y] == '.' or map_data[x][y] == prince)):
            return
        area += 1
        map_data[x][y] = 'W'  # Mark as visited
        for dx, dy in directions:
            dfs((x + dx, y + dy))

    # Perform DFS from the prince's position
    for pos in prince_pos:
        dfs(pos)

    # Return the area
    return area

#print(island_area("./Practical Exam 2/22-23_sem1/map1.txt","A"))


def prince_map(filename, prince):
    # Open and read the file
    with open(filename, 'r') as f:
        map_data = [list(line.strip()) for line in f]

    # Find the prince's position
    prince_pos = [(i, j) for i, row in enumerate(map_data) for j, cell in enumerate(row) if cell == prince]
    if not prince_pos:
        return []

    # Define the directions for DFS
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize the boundaries
    minr, maxr, minc, maxc = float('inf'), float('-inf'), float('inf'), float('-inf')

    # DFS function
    def dfs(pos):
        nonlocal minr, maxr, minc, maxc
        x, y = pos
        if not(0 <= x < len(map_data) and 0 <= y < len(map_data[0]) and (map_data[x][y] == '.' or map_data[x][y] == prince)):
            return
        # Update the boundaries
        minr, maxr, minc, maxc = min(minr, x), max(maxr, x), min(minc, y), max(maxc, y)
        map_data[x][y] = 'W'  # Mark as visited
        for dx, dy in directions:
            dfs((x + dx, y + dy))

    # Perform DFS from the prince's position
    for pos in prince_pos:
        dfs(pos)

    # Crop the map to the boundaries and convert each row back to a string
    cropped_map = [''.join(row[minc:maxc+1]) for row in map_data[minr:maxr+1]]

    return cropped_map

#min. no. of turns (to clear list)

def min_no_of_turns(L: tuple) -> int:
    moves = 0 #to count number of moves

    if not L: #input is empty
        return 0
    
    else:
        lst = sorted(L) #sort the array in ascending order
        while lst: #while list is not empty [1, 1, 2, 3, 5, 6, 7, 8]
            max_length = 1
            max_index = 0

            #find the longest consecutive subsequence
            for i in range(len(lst)):
                current_length = 1
                while (i + current_length < len(lst)) and (lst[i + current_length] == lst[i] + current_length): 
                    #ensure subsequence does not exceed length of list AND ensure next elem is equal to one greater than current elem
                    current_length +=1 #extend the subsequence to cover next elem
                
                if current_length > max_length: #once found a new longest subsequence
                    max_length = current_length #update the max_length value
                    max_index = i #save the starting index of the new longest subsequence

            if max_length == 1: #no more consecutive subsequence, only individual numbers
                return moves + len(lst) 
                #num of moves to clear individual nums = length of the array *mindblown*
                #eg. [3,6,9] needs 3 moves to clear 3 nums
            
            #if there are subsequences available to clear
            lst = lst[:max_index] + lst[max_index + max_length:] 
            #returns everything before index to be cut, and everything after index+length of subsequence
            moves += 1

    return moves

#most expensive burger

def most_expensive_burger(money: int, price_dict: dict) -> tuple:
    #resulting burger
    burger = ''

    #sort dict in descending orderof price = item[1]
    sorted_ingredients = sorted(price_dict.items(), key=lambda item: item[1], reverse=True)
    
    #for every item = tuple, ingredient is index 0, price is index 1
    for ingredient, price in sorted_ingredients: #ingredient is a list of tuples -> ('A', 31)...etc
        if money >= price:
            burger += ingredient #add ingredient to burger str
            money -= price #subtract price of ingredient

    if burger: #if burger != '' (empty str)
        burger = 'B' + burger + 'B'

    return (burger, money)

#find treasure
def decipher_message(msg: str, guide: dict) -> str:
    output = ''
    for character in msg:
        if character in guide:
            output += guide[character]
        else:
            output += character
    
    return output


def decode_map(mapfile, ddict, outfile):
    with open(mapfile, "r") as f:
        encoded = f.read()
    
    decoded = decipher_message(encoded, ddict)

    with open(outfile, 'w') as f:
        f.write(decoded)


def find_treasure(mapfile):
    #list to contain rows and cols of the map
    map_data = []
    #open the map in read only
    with open(mapfile, 'r') as f:

        for line in f:
            map_data.append(line.strip()) #.strip() to remove \n

    #number of items in the list = rows
    #number of items in each item = cols
    rows, cols = len(map_data), len(map_data[0])

    #search for pattern 
    #  T    ->         (0,-1) 
    #T T T  -> (-1,0), (0,0), (1,0)
    #  T    ->         (0,1)
    for r in range(1, rows - 1):  
        for c in range(1, cols - 1):
            if (map_data[r][c] == 'T' and
                map_data[r - 1][c] == 'T' and
                map_data[r + 1][c] == 'T' and
                map_data[r][c - 1] == 'T' and
                map_data[r][c + 1] == 'T'):
                return (r, c)
    return None  

#ancestor/ ancestry tree
def is_ancestor(name1: str, name2: str, pdict: dict) -> bool:
  #if it is the same person
  if name1 == name2:
    return False

  while name2 in pdict: #this execution of checking to prevent out of bounds
      if pdict[name2] == name1: #parent found
          return True
      name2 = pdict[name2] #move up, define new child

  return False


def generate_ancestors(name, pdict): #function to return list of ancestors' names
  seen = []
  while name in pdict:
    seen.append(name)
    name = pdict[name]
  return seen
  

def is_related(name1: str, name2: str, pdict: dict) -> bool:
  #check if both names have ancestor-descendent relationship
  if is_ancestor(name1, name2, pdict) or is_ancestor(name2, name1, pdict):
    return True 

  #check if both names are from the same generation
  ancestors_1 = generate_ancestors(name1, pdict)
  ancestors_2 = generate_ancestors(name2, pdict)

  for name1_ancestors in ancestors_1:
     for name2_ancestors in ancestors_2:
        if name1_ancestors == name2_ancestors:
           return True
        
  return False

#assignment 6: Tic tac toe, pizza delivery map
def create_game_matrix(r: int, c: int) -> list:
    output = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output
#pprint.pprint(create_game_matrix(3,3))

#takes in a matrix, prints out the proper TTT grid with lines
#only 3x3 square matrix allowed
def print_TTT(game: list):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i !=2:
            print('-----')
#print_TTT(create_game_matrix(3,3))

#gameplay
def ttt_gameplay():
    game = create_game_matrix(3,3) #3x3 zero matrix
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1 #give every coordinate a position number
    player = 0

    print_TTT(game)
    for i in range(9): 
        print()
        valid_move = False
        while not valid_move:
            pos = int(input(f'Player {piece[player]} move:')) #input converted to int
            valid_move = check_valid_move(game,pos)
            if not valid_move: #if check_valid_move returns False
                print(f'Your move {pos} is not valid')
        pos -= 1
        game[pos//3][pos%3] = piece[player]
        winner = check_win(game)
        if winner:
            print(f'Player {winner} won!!! Game over.')
            print_TTT(game)
            return
        player = 1 - player
        print_TTT(game)

    print('No one won. It\'s a tie game.')

piece = ['X','O']
game1 = [[1,2,3],[4,5,6],[7,8,9]]
game2 = [['X',2,3],['X',5,6],['X',8,9]]
game3 = [['O',2,3],[4,'O',6],[7,'O',9]]
game4 = [['X',2,'X'],[4,'O',6],['X','O','X']]
game5 = [['X','X','O'],['X','O','X'],['O','X','X']]


def check_valid_move(game: list, inp: int) -> bool:
    if 1 <= inp <= 9: #check if digit is within 1 to 9
        i = (inp -1) // 3 #obtain i coordinate from input
        j = (inp -1) % 3 #obtain j coordinate from input
        if game[i][j] not in ['O', 'X']: #check if the position is not used
            return True
    return False

def check_win(game: list) -> str:
    #all possible win-con of rows, cols, and diagonals
    winning_condition = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)], #3 in a row for top, mid, and bot rows
        [(2,0), (2,1), (2,2)],

        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)], #3 in a row for left, mid, right cols
        [(0,2), (1,2), (2,2)],

        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)], #3 in a row for forward, backward diagonals
    ]
    
    for matches in winning_condition: #iterate over each match in win_con to check which one is fulfiled
        result = [] 
        for i, j in matches:
            result.append(game[i][j]) #get the symbol (or nothing) from game for each coordinate
        if result == ['X', 'X', 'X']:
            return 'X'
        if result == ['O', 'O', 'O']:
            return 'O'

    return '' #return empty string if none of the matches is a win


#euclidean distance = ((x1-x2)**2 + (y1-y2)**2)*0.5
def euclidean_distance(i: int, j: int, point_2: list) -> float:
    return ((i - point_2[0])**2 + (j - point_2[1])**2)**0.5


def pd_map(r: int, c: int, sites: list) ->list:
    homes = create_zero_matrix(r, c) #creates a r x c zero matrix
    for i in range(r):
        for j in range(c):
            #for every coordinate point, check euclidean distance to every pizza hut in sites
            distances = [euclidean_distance(i, j, site) for site in sites] #list of distances to all piza huts from one house
            nearest = min(distances) #get nearest pizza hut distance
            if distances.count(nearest) > 1: #more than one nearest pizza hut
                homes[i][j] = 'X'
            else:
                homes[i][j] = distances.index(nearest) #save the closest pizza hut number to the coordinate   
    return homes

#assignment 7: OOP
DEBUG_PRINT = True
def dprint(s):
  if DEBUG_PRINT:
    print(s)

### CONSTANT FOR MAGE
MANA_COST = 20
MANA_RECOVERY = 30


### BASE CHARACTER
#inherit whenever possible
#NOT to mod FIGHTER AND MAGE
#should NOT override superclass method
#call superclass methods whenever possible
class Character(): #base class
  def __init__(self):
    self.name = ''
    self.maxhp   = 800
    self.hp      = 800
    self.maxmana = 0
    self.mana    = 0
    self.str     = 0
    self.int     = 0
    self.cost    = 9999999999
    self.alive   = True

  def act(self, my_team, enemy): #character's action
    return

  def got_hurt(self, damage): #character takes dmg
    if damage >= self.hp:
      self.hp = 0
      self.alive = False
      dprint(self.name + ' died!')
    else:
      self.hp -= damage
      dprint(self.name +
           f' hurt with remaining hp {self.hp}.')

  
### FIGHTER
class Fighter(Character): #each turn inflct dmg = strength on rand opp
  def __init__(self):
    super().__init__()
    self.name  = 'Fighter'
    self.maxhp = 1200
    self.hp    = 1200
    self.str   = 100
    self.cost  = 100

  def act(self, my_team, enemy):
    target = rand_alive(enemy)
    dprint(f'Hurt enemy {target} by damage {self.str}.')
    enemy[target].got_hurt(self.str)

  
### MAGE
class Mage(Character): #cast spell = intelligence, cost 20 mana. if <20mana, meditate
  def __init__(self):
    super().__init__()
    self.name    = 'Mage'
    self.maxmana = 50
    self.mana    = 50
    self.cost    = 200
    self.int     = 400

  def cast(self, my_team, enemy):
    self.mana -= MANA_COST
    target = rand_alive(enemy)
    dprint(f'Strike enemy {target} with spell')
    enemy[target].got_hurt(self.int)
    
  def act(self, my_team, enemy):
    if self.mana < MANA_COST:
      self.mana += MANA_RECOVERY
      dprint(f'Mana recover to {self.mana}.')
    else:
      self.cast(my_team, enemy)

### BERSERKER
class Berserker(Fighter): #cost 200G, if HP <= 0.5HP(max) -> STR*2
  def __init__(self):
    super().__init__()
    self.name = 'Berserker'
    self.cost = 200
  
  def act(self, my_team, enemy):
    if self.hp <= (self.maxhp / 2):
      self.str = 200
      target = rand_alive(enemy)
      dprint('Berserk mode! Attack double!' )
      dprint(f'Hurt enemy {target} by damage {self.str}.')
      enemy[target].got_hurt(self.str) #this "does" the damage
    
    else:
      #normal attack if HP > half.
      self.str = 100
      super().act(my_team, enemy) 


### ARCHMAGE
class ArchMage(Mage):
  def __init__(self):
    super().__init__()
    self.name = 'ArchMage'
    self.cost = 600
  
  def act(self, my_team, enemy):
    if self.mana < MANA_COST: #not enough mana = meditate
      self.mana += MANA_RECOVERY
      dprint(f'Mana recover to {self.mana}.')

    else:
      if count_alive(my_team) == 1: #if archmage the only one alive, kaboom
        self.kaboom(enemy)
      else:
        self.cast(my_team, enemy) #normal attack
  
  def kaboom(self, enemy): #heavy damage to ALL enemies
    self.mana -= MANA_COST
    dprint(f'Cast KABOOM to every enemy')
    for target in enemy: #iterate through the whole enemy list
      target.got_hurt((self.int)*2) #this "does" the damage = 2*int


### NECROMANCER
class Necromancer(Mage): 
  def __init__(self):
    super().__init__()
    self.name = 'Necromancer'
    self.cost = 400

  def act(self, my_team, enemy):
    if count_dead(my_team) > 0: #if there are dead members, try res first
      if self.mana < MANA_COST: #if not enough mana = meditate
        self.mana += MANA_RECOVERY
        dprint(f'Mana recover to {self.mana}.')
      
      else: #res random member w half hp
        self.revive(my_team)
  
    else: #if all members alive = normal mage move
      super().act(my_team, enemy)

  def revive(self, my_team):
    self.mana -= MANA_COST
    target = rand_death(my_team) #target is an int, since rand_death() returns an int
    member = my_team[target] #get the target character from list 
    member.alive = True
    member.hp = member.maxhp // 2
    dprint(f'Reviving member {member} with {member.hp} hp')


#binary search proper
def binary_search(key: int, seq: list) -> bool:
    def helper(low, high):
        if low > high:
            return False
    
        mid = (low + high) // 2
        
        if key == seq[mid]:
            return True
        
        elif key < seq[mid]:
            return helper(low, mid-1)
        
        else:
            return helper(mid+1, high)
    
    return helper(0, len(seq)-1)

#sorting / sorts / bubblesort/ selection sort/merge sort
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