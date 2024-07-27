from turtle import *

def draw_polygon(d, n):
    if n >= 3:
        internal_angle = ((n - 2) * 180) / n #check internal angles
        external_angle = 180 - internal_angle #turtle takes angle from straight ahead
        for i in range(n):
            forward(d)
            left(external_angle)
    else:
        pass


draw_polygon(200,4)


"""
def draw_polygon(d, n):
    internal_angle = ((n - 2) * 180) // n #check internal angles
    external_angle = 180 - internal_angle #turtle takes angle from straight ahead
    turtle_movement(d, n, external_angle)

def turtle_movement(distance, sides, angle):
    for i in range(sides):
        forward(distance)
        left(angle)
"""