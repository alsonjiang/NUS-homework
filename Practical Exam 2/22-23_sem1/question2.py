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

print(island_area("./Practical Exam 2/22-23_sem1/map1.txt","A"))


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

##################################################################################
def preparemaps(): # run this to generate two text file, map1.txt and map2.txt 
    m1 = ['WWWWWWWWWWWWWWWWWW.WWWWWWW', 
         'WWWWWWWW.WWWWWWWW...WWWWWW', 
         'WWWWW...WWWWWWWWWW.B..WWWW', 
         'WWWWWWW.WWWWWWWWW...WWWWWW', 
         'WWWWWWW.....WWWWWWWW..WWWW', 
         'WWW.......WWWWWWWWWWWWWWWW', 
         'WWWW...A..WWWWWWWWWWW..WWW', 
         'WWWWW.....WWWWWWWW...WWWWW', 
         'WWWWWWW..WWWWWWWWW.C.WWWWW', 
         'WWWW..WWWWWWWWWWWW...WWWWW', 
         'WW....WWWWWWWWWWWWWWWWWWWW', 
         'WWW.WWWWWWWWWWWWWWWWWWWWWW'] 
    map1file = open('map1.txt','w') 
    for r in m1: 
        map1file.write(r+'\n') 
    m2 = ['WWWWWWWWWWWWWWW.WWWWWWW', 
         'WWWWW.WWWWWWWW...WWWWWW', 
         'WWWWWWWWWWWWWWW.B..WWWW', 
         'WWWW.WW.WWWWWW...WWWWWW', 
         'WWWW...WWWWWWWWWW..WWWW', 
         'W......WWWWWWWWWWWWWWWW', 
         'W...A..WWWWWWWWWWW..WWW', 
         'WW.....WWWWWWWW...WWWWW', 
         'WWWWWWWWWWWWWWWWWWWWWWW'] 
    map2file = open('map2.txt','w') 
    for r in m2: 
        map2file.write(r+'\n') 
 
#This will read in a file and covert it into a 2D array 
#You do not need to use it if you have another way to solve Part 2 
#However, if you use this code, please remember to include in your submission 
def readmap(filename):  
    f = open(filename) 
    m = [] 
    for line in f: 
        m.append(list(line.rstrip('\n'))) 
    return m