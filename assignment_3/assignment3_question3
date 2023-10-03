import random #don't import in coursemo

def monte_carlo_pi(n):
    points_in_circle = 0
    points_in_square = 0

    for i in range(n):

        #randomly generates (x,y)
        x_coord = random.uniform(-1,1)
        y_coord = random.uniform(-1,1)

        #pythagoras theorem
        distance_from_origin = (x_coord * x_coord) + (y_coord * y_coord)
        distance_from_origin = distance_from_origin ** 0.5

        if distance_from_origin <= 1:
            points_in_circle += 1
        
        else:
            points_in_square += 1
    
    return 4 * (points_in_circle / n)

print(monte_carlo_pi(10000000))
