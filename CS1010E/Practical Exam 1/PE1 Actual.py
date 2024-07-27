#start2:48pm

#part 1
def card_game_i(N: int, start_pos: int, start_dir: str, seq:str) -> int:
    #function that rotates the list to put the current player at the 
    #start and the opposite direction player after him
    def rotate(players, current_player):
        reverse = players.reverse()
        rotated = [current_player] + reverse[current_player:] + reverse[:current_player]
        return rotated
    
    #put all players in a list (0 to N)
    players = []
    for i in range(N):
        players.append(i)

    #define a current player to start
    current_player = players[start_pos]

    #check initial direction, redefine players positions
    players = rotate(players, current_player)

    #for every card, move on with list or rotate
    for i in range(seq):
        if i == 'D':
            current_player = players[start_pos+1]
        if i == 'R':
            players = rotate(players)

    return current_player
#print(card_game_i(5, 2, 'CCW', 'DDRDR'))

def card_game_r(N: int, start_pos: int, start_dir: str, seq:str) -> int:
    players = []
    #make a list of players
    for i in range(N):
        players.append(i)
    
    #define a current player
    current_player = players[start_pos]

    #make a list of the seq
    lst = list(seq)

    #base case
    if lst == []:
        return current_player
    
    if lst[0] == 'D':
        #move forward
    
    if lst[0] == 'R':
        #rotate list
    
    return card_game_r(N, current_player, start_dir, lst)
    

#print(card_game_r(5, 2, 'CW', 'DDRDR'))


#part 2
def find_parents(child_dna: str, dna_database: str) -> list:
    possible_matches = [] #split the child_dna up into its constituents
    parent_1 = [] #list of the first parent pair
    result = [] #final output 

    #get all constituents of child_dna 
    for index, value in enumerate(child_dna):
        possible_matches.append(child_dna[:index+1])

    #for every element, search database to see if it exist, save as parent 1
    for item in possible_matches:
        if item in dna_database:
            parent_1.append(item)

    #for every parent1, search data base for its potential pair, save to output
    for parent in parent_1:
        for dna in dna_database:
            if parent + dna == child_dna and (parent != dna):
                result.append((parent, dna))

    return result
    

#print(find_parents('ACGTA', ['ACT', 'TA', 'CGTA', 'ACG', 'A', 'ACGT']))
#print(find_parents('ATGATG', ['ATGAT', 'ACT', 'GAT', 'ATG', 'G']))


#task 3
#s= straw, w=wood, b=brick, h=attack 1 layer
def three_little_pigs_defence(seq: str) -> str:
    defenses = []
    output = ''
    for character in seq:
        if character == 'S':
            defenses.append('S')
        if character == 'W':
            defenses.append('W')
        if character == 'B':
            defenses.append('B')
        if character == 'H':
            if defenses == []:
                continue
            if defenses[-1] != 'B':
                defenses.pop(-1)
    
    for items in defenses:
        output += items
    
    return output

#print(three_little_pigs_defence('BSHHSWHS'))