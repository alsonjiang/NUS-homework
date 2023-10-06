
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
<<<<<<< HEAD
    #height of map start from -4 to remove legends at bottom of map
    height = -4
    with open(mapfile, "r") as f:
        
        length = f.readline
        for lines in f:
            height += 1


    return length, height
=======
    with open(mapfile, 'r') as f:
        map_data = [list(line.strip()) for line in f]
>>>>>>> f8fabc1ef68f68cbdf607887e756b6a6cd4d7416

    rows, cols = len(map_data), len(map_data[0])

    for r in range(1, rows - 1):  # We start from 1 and end at rows - 1 to avoid index out of bounds
        for c in range(1, cols - 1):
            # Check for the tree pattern
            if (map_data[r][c] == 'T' and
                map_data[r - 1][c] == 'T' and
                map_data[r + 1][c] == 'T' and
                map_data[r][c - 1] == 'T' and
                map_data[r][c + 1] == 'T'):
                return (r, c)
    return None  # If no treasure found


d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', 
'2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 
'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', 
'#': ' '}

#decode_map("assignment_5/encoded_mapB.txt", d1, "assignment_5/decoded_mapB.txt")
print(find_treasure("assignment_5/decoded_map.txt"))