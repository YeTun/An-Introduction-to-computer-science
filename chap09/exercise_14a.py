# Me Computer, Mandalay.
# June 20, 2022
# exercise_14a.py
# random walk - in any direction

from random import random, randrange
from math import pi, cos, sin
from graphics import *

def main():
    win = openWin()
    printIntro(win)
    n = int(getInputs(win))
    # textToWin(n, win, Point(250, 400))
    runSims(n, win)
    # wait for click
    clickToContinue(win)

def openWin():
    win = GraphWin("Random Walk", 500, 500)
    win.setBackground(color_rgb(68, 101, 56))
    win.setCoords(0, 0, 100, 100)
    return win

def printIntro(win):
    horizontalPosition = 50
    verticalPosition = 95
    one = textToWin("This program illustrates a random walk in any direction from the last", 
        win, Point(horizontalPosition, verticalPosition))
    # move next line down
    verticalPosition -= 3
    two = textToWin("position. User inputs the number of 'steps' to take from the initial", 
        win, Point(horizontalPosition, verticalPosition))
    verticalPosition -= 3
    three = textToWin("center point. Each step is approximately 1/20 of the window size.", 
        win, Point(horizontalPosition, verticalPosition))
    clickToContinue(win)
    one.undraw()
    two.undraw()
    three.undraw()

def textToWin(string, win, position):
    # take string, print to designated graphics window, centereed at position
    t = Text(position, string)
    t.draw(win)
    return t

def clickToContinue(win):
    center = Point(50, 50)
    one = textToWin("Click to continue...", win, center)
    win.getMouse()
    one.undraw()

def getInputs(win):
    horizontalPosition = 50
    verticalPosition = 20
    one = textToWin("Enter the number of iterations below....", 
        win, Point(horizontalPosition, verticalPosition))
    verticalPosition -= 5
    entry = Entry(Point(horizontalPosition, verticalPosition), 5)
    entry.draw(win)
    clickToContinue(win)
    one.undraw()
    entry.undraw()
    return entry.getText()

def runSims(n, win):
    x = 50
    y = 50
    start = Point(x, y)
    drawPoint(start, win, 250)
    for i in range(n):
        angle = random() * 2 * pi
        newX = x + 4 * cos(angle)
        newY = y + 4 * sin(angle)
        newPt = Point(newX, newY)
        drawLine(start, newPt, win, i)
        drawPoint(newPt, win, i)
        x = newX
        y = newY
        start = Point(x, y)

def drawPoint(p, win, i):
    pt = Circle(p, 1)
    r = randrange(0, 251, 1)
    g = randrange(0, 251, 1)
    b = randrange(0, 251, 1)
    pt.setFill(color_rgb(r, g, b))
    pt.draw(win)
    return pt

def drawLine(pt1, pt2, win, i):
    l = Line(pt1, pt2)
    r = randrange(0, 251, 1)
    g = randrange(0, 251, 1)
    b = randrange(0, 251, 1)
    l.setFill(color_rgb(r, g, b))
    l.draw(win)

if __name__ == '__main__': main()

