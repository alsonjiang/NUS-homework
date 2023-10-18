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

circlePic()


#reading csv files easier method, no need strip(), split(), etc
#birth_file = open('(file_name)')
#birth_file_reader = csv.reader(birth_file)
#birth_data = list(birth_file_reader)