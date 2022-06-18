# target.py
# May 17, 2022
# A program to draw a target of any size and any number of rings of different color.

from graphics import *

def main():
    # single point of control that allows resizing of target
    squareside = 200
    r = (squareside / 2)
    center = Point((squareside/2),(squareside/2))

    # use this list to add or delete colors for simpler or more complex targets
    color = ["white", "black", "blue", "red", "yellow", "green"] 	

    win = GraphWin("Ready, Aim, Fire!", squareside, squareside)

    # len() is used so that a target of any number of circles can be drawn
    for i in range(len(color)):

        # len(0 is used to get the proportion of part to whole
        aim = Circle(center, r - (r * (i / len(color))))
        aim.setFill(color[i])
        aim.draw(win)
    
    # Wait for another click to exit
    win.getMouse()
    win.close()

main()
