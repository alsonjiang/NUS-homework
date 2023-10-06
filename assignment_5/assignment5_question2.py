
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


def sliding_window():
    pass



def find_treasure(mapfile):
    #height of map start from -4 to remove legends at bottom of map
    height = -4
    with open(mapfile, "r") as f:
        
        length = f.readline
        for lines in f:
            height += 1


    return length, height




d1 = {'D': 'W', '1': 'W', 'Z': 'W', 'C': 'T', '3': 'T', 'F': 'T', '0': '.', 
'2': '.', '4': '.', 'B': '^', '+': '^', ';': '^', 'Q': 'E', '7': 'E', '8': 'E', 
'X': 'M', 'P': 'M', '!': 'M', '(': ':', ')': ':', '9': ':', '*': ' ', '|': ' ', 
'#': ' '}

#decode_map("assignment_5/encoded_mapB.txt", d1, "assignment_5/decoded_mapB.txt")
print(find_treasure("assignment_5/decoded_map.txt"))