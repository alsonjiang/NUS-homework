"""
Question 2: Pizza Delivery 2.0
"""
def m_tight_print(m):
  for row in m:
    print(''.join(row))
  
def create_zero_matrix(n,m):
    return [[0 for i in range(m)] for j in range(n)]

class PizzaShop:
    def __init__(self, pos, name, radius, hour_s, hour_e):
        self.pos = pos
        self.name = name
        self.radius = radius
        self.hour_s = hour_s
        self.hour_e = hour_e

    def is_open(self, hour):
        return self.hour_s <= hour < self.hour_e

    def distance_square_to(self, i, j):
        return (self.pos[0] - i) ** 2 + (self.pos[1] - j) ** 2

    def can_deliver_to(self, i, j, hour):
        return self.distance_square_to(i, j) <= self.radius ** 2 and self.is_open(hour)


def pd_map(r, c, all_shops, hour):
    map_grid = [['.' for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            min_distance = float('inf')
            closest_shops = []

            for shop in all_shops:
                if shop.can_deliver_to(i, j, hour):
                    distance = shop.distance_square_to(i, j)
                    if distance < min_distance:
                        min_distance = distance
                        closest_shops = [shop]
                    elif distance == min_distance:
                        closest_shops.append(shop)

            if len(closest_shops) == 1:
                map_grid[i][j] = closest_shops[0].name[0]
            elif len(closest_shops) > 1:
                map_grid[i][j] = 'X'

    return map_grid


# Example Usage
all_shops = [
    PizzaShop([3, 3], 'Ace', 3, 8, 14),
    PizzaShop([6, 6], 'Bizza', 4, 12, 22)
]

# Print maps for different hours
hours = [10, 12, 16]
r, c = 10, 12

for hour in hours:
    delivery_map = pd_map(r, c, all_shops, hour)
    print(f"Map for hour {hour}:")
    for row in delivery_map:
        print(''.join(row))
    print("\n")


### Test data (do not modify)
all_shop = [PizzaShop([3,3], 'Ace', 3, 8, 14), PizzaShop([6,6], 'Bizza', 4, 12, 22)]
### Test cases (comment out or remove before copying to Coursemology)
#m_tight_print(pd_map(10, 12, all_shop, 10))
#m_tight_print(pd_map(10, 12, all_shop, 12))
#m_tight_print(pd_map(10, 12, all_shop, 16))
#print(pd_map(10, 12, all_shop, 10))