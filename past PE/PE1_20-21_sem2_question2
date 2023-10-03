#start = UU or UG
#end = AC or AA
def rna_segment(rna: str) -> str:
    rna = list(rna)
    start_1, start_2, end_1, end_2 = ['U','U'], ['U','G'], ['A','C'], ['A','A']
    segmented = ''

    #fixed sliding window
    #find starting point of all the starts and ends
    start_index = []
    end_index = []

    window_size = 2

    #The number of positions to slide the window across
    positions = len(rna) - window_size + 1

    for i in range(positions):
        window = rna[i:i+window_size]

        #either starts found
        if window == start_1 or window == start_2:
            start_index.append(i)
        
        #either ends found
        if window == end_1 or window == end_2:
            end_index.append(i)
    
    #FIRST occurence of starts and ends
    for i in range(min(start_index), min(end_index)+2):
        segmented += rna[i]

    return segmented

#print(rna_segment('GUUGAAGUACAAAG'))


def poly_property(poly: str) -> str:
    poly = poly.upper()

    acidic_count = 0
    basic_count = 0
    polar_count = 0
    non_polar_count = 0

    for char in poly:
        if char == "F" or char == "P" or char == "Q":
            acidic_count += 1
        elif char == "M" or char == "A" or char == "C" or char == "R":
            basic_count += 1
        elif char == "S" or char == "T" or char == "Y":
            polar_count += 1
        elif char == "L" or char == "O":
            non_polar_count += 1
        else:
            continue

    if acidic_count == basic_count:
        if polar_count > non_polar_count:
            return 'Polar'

    if acidic_count > basic_count:
        return 'Acidic'
    
    if acidic_count < basic_count:
        return 'Basic'
    

    return 'Neutral'

#print(poly_property('YSF'))


