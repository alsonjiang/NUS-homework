#order: white, yellow, red
#formula: (i + j − 2) % 3
def calculate_areas(w_list:list, h_list:list) -> tuple:

    #initialize colours
    white, yellow, red = 0, 0, 0

    if w_list is None:
        if h_list is None:
            return 0
    
    for widths in w_list:
        for heights in h_list:
            areas = widths * heights
            colour = (widths + heights - 2) % 3

            if colour == 0:
                white += 1
            elif colour == 1:
                yellow += 1
            else:
                red += 1

    return (white,yellow,red)

w_list = [1, 1, 1]
h_list = [1, 1, 1]
print(calculate_areas(w_list,h_list))

    
