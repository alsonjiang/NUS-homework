def rotate(bouquet: tuple, step: int) -> tuple:
    bouquet_lst = list(bouquet)
    rotated = [i for i in bouquet_lst[step:] + bouquet_lst[:step]]

    return rotated

#print(rotate(("R", "P", "W", "W", "P", "R", "R", "R"), 7))

def flower_I(bouquet: tuple, k: int) -> str:
    bouquet_lst = list(bouquet)
    flowers_gifted = []
    while bouquet_lst is not []:
        flowers_gifted.append(bouquet_lst[k])
        bouquet_lst.remove(bouquet_lst[k])
        bouquet_lst = rotate(bouquet_lst, k)

    return flowers_gifted

print(flower_I(("R", "P", "W", "W", "P", "R", "R", "R"), 3))


def flower_R(bouquet: tuple, k: int) -> str:
    pass

def pink_rose(bouquet: tuple) -> int:
    pass