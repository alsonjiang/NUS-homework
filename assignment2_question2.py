from turtle import *

def draw_polygon(d, n):
    internal_angle = ((n - 2) * 180) // n #check internal angles
    external_angle = 180 - internal_angle #turtle takes angle from straight ahead
    for i in range(n):
        forward(d)
        left(external_angle)


draw_polygon(200,6)


