def rotate(bouquet: tuple, step: int) -> tuple:
    bouquet_lst = list(bouquet)
    rotated = [i for i in bouquet_lst[step:] + bouquet_lst[:step]]

    return rotated

#print(rotate(("R", "P", "W", "W", "P", "R", "R", "R"), 3))

def flower_I(bouquet: tuple, k: int) -> str:
    bouquet_lst = list(bouquet)
    flowers_gifted = bouquet_lst[k-1] #first rose, kth from start
    bouquet_lst = rotate(bouquet_lst, k-1)

    for i in range(len(bouquet_lst)):
        bouquet_lst = rotate(bouquet_lst, k)
        print(bouquet_lst)
        flowers_gifted += bouquet_lst[3]
    
    return flowers_gifted
    
print(flower_I(("R", "P", "W", "W", "P", "R", "R", "R"), 3))
#W R R P P R W R

def flower_R(bouquet: tuple, k: int) -> str:
    pass

def pink_rose(bouquet: tuple) -> int:
    pass