#property realty agent
#neighbour = 8 locaions next to current home 
#buyable vs unbuyable

def buyable_map(filename) -> str:
    map_data = []
    output = ''

    with open(filename, 'r') as f:
        for line in f:
            map_data.append(line.strip())

    rows, cols = len(map_data), len(map_data[0])

    def get_value(i, j): #function to get a value of a valid specified cell
        if 0 <= i <= rows and 0 <= j <= cols:
            return map_data[i][j]
        
    #function to compare current cell with neighbouring cells
    def check_neighbours(current_cell_value, current_x_coord, current_y_coord):
        for neighbouring_x_coords, neighbouring_y_coords in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (1,1)]:
            if current_cell_value == get_value(current_x_coord + neighbouring_x_coords, current_y_coord + neighbouring_y_coords):
                return False #all neighbours have the same value, not buyable
            elif get_value(current_x_coord + neighbouring_x_coords, current_y_coord + neighbouring_y_coords) == 'X':
                return True #neighbours have 'X' at their house, buyable
            elif get_value(current_x_coord+neighbouring_x_coords, current_y_coord+neighbouring_y_coords) != current_cell_value:
                if get_value(current_x_coord+neighbouring_x_coords, current_y_coord+neighbouring_y_coords) in [0,1,2,3,4,5,6,7,8,9]:
                    return True
        return False

    for i in range(rows):
        for j in range(cols):
            if map_data[i][j] in ['X']: #if current house is X
                output += 'X'
            elif check_neighbours(map_data[i][j], i, j) == True:
                output += str(map_data[i][j])
            elif check_neighbours(map_data[i][j], i, j) == False:
                output += '.'

    return output

print(buyable_map('Practical Exam 2/21-22_sem1/pmap1.txt'))


def buyable_map_Ryan(filename):

    buyable = ''
    f = open(filename,'r')
    rows =f.readlines()
    f.close()

    max_R = len(rows)
    max_C = len(rows[0])

    """
    def in_range (R,C):
        if R > max_R or R<0:
            return False
        if C > max_C or C<0:
            return False
        return True
    """

    def in_range (R,C):
        if 0 <= R < max_R and 0 <= C < max_C:
            return True
        else:
            return False

    def check_surroundings(R,C,self):
        
        for x in range (R-1,R+2):
            for y in range(C-1,C+2):
                if (in_range(x,y) == True) and (rows[x][y] != self):
                    return True
        return False
                
    for i in range (max_R):
        temp = ''
        for j in range(max_C):
            self = rows[i][j]
            if check_surroundings(i,j,self) == True or (self == 'X'):
                temp += self
            else:
                temp += '.'
        buyable += (temp + '\n')
    
    return buyable
                

print(buyable_map_Ryan('Practical Exam 2/21-22_sem1/pmap1.txt'))










#skeleton code and prep for part 2
def create_map_file(): 
    pmap1list =  ['0000011111', 
     '0000X11111', 
     '0000111111', 
     '000X111111', 
     '0001111111', 
     '0222111111', 
     '2222211111', 
     '2222222111', 
     '2222222211', 
     '2222222222', 
     '2222222222'] 
    pmap2list = ['000000X22222', 
     '00000X222222', 
     'XXXXX2222222', 
     '111122222222', 
     '111122222222', 
     '111X22222222', 
     '111222222222', 
     '111222222222', 
     '11X222222222', 
     '112222222222'] 
    f1 = open("pmap1.txt","w") 
    for line in pmap1list: 
        f1.write(line+'\n') 
    f1.close() 
    f2 = open("pmap2.txt","w") 
    for line in pmap2list: 
        f2.write(line+'\n') 
    f2.close() 
create_map_file() 
def buyable_map(filename): 
    return 
#print(buyable_map('pmap1.txt')) 
#print(buyable_map('pmap2.txt')) 
