import pprint
############################################
## DO NOT MODIFY THIS PORTION OF CODE!!!! ##
############################################

#creates a r x c zero matrix
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

############################################
########### End of do not modify ###########
############################################

############
## Task 1 ##
############

def check_valid_move(game: list, inp: int) -> bool:
    if 1 <= inp <= 9: #check if digit is within 1 to 9
        i = (inp -1) // 3 #obtain i coordinate from input
        j = (inp -1) % 3 #obtain j coordinate from input
        if game[i][j] not in ['O', 'X']: #check if the position is not used
            return True
    return False

# print(check_valid_move(game1, 4))
# print(check_valid_move(game1, 10))
# print(check_valid_move(game2, 4))
# print(check_valid_move(game4, 4))
# print(check_valid_move(game5, 4))
# print(check_valid_move(game2, 1))
# print(check_valid_move(game5, -9))

############
## Task 2 ##
############

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

# print(check_win(game1))
# print(check_win(game2))
# print(check_win(game3))
# print(check_win(game4))
# print(check_win(game5))

#############################################################
## Uncomment and run ttt_gameplay() below to test the game ##
#############################################################

# ttt_gameplay()
