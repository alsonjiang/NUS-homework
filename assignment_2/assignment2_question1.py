from turtle import *

def straight_and_turn(distance):
    forward(distance)
    left(90)

def draw_square(d):
    for i in range(4):
        straight_and_turn(d)
        i += 1

draw_square(100)