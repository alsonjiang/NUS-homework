from turtle import *

def draw_polygon(d, n):
    internal_angle = ((n - 2) * 180) / n #check internal angles
    external_angle = 180 - internal_angle
    for i in range(n):
        forward(d)
        left(external_angle)


def draw_flower(d, n, p):
    new_angle = 360 / p
    for _ in range(p):
        draw_polygon(d, n)
        left(new_angle) #draw finish one and turn to a new angle

draw_flower(100,5,6)
