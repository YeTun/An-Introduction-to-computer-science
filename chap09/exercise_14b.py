# Me Computer, Mandalay.
# June 20, 2020
# exercise_14.py

#graphical program to trace random walk in 2 dimensions

import math as m
from random import random
from graphics import *

def main():
    n = eval(input("How many steps do you intend to take through the simulation? "))
    win = GraphWin("Random Walk", 600, 600)
    win.setCoords(-100, -100, 100, 100)
    for i in range (5):
        randWalk(n, win)
    input("Press enter key")
    win.close()

def randWalk(n, win):
    point2 = Point(0, 0)
    for i in range (n):
        x = point2.getX()
        y = point2.getY()

        point1 = simOneStep(x, y)
        point1.draw(win)
        line = Line(point2, point1)
        line.draw(win)
        point2 = point1

def simOneStep(x, y):
    angle = random() * 2 * m.pi
    x = x + m.cos(angle)
    y = y + m.sin(angle)
    point = Point(x, y)
    return point

if __name__ == '__main__': main()
