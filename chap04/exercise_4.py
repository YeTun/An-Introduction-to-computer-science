# Me Computer, Mandalay.
# June 15, 2022
# exercise_4.py
# A simple graphics program that draws a winter scene

from graphics import *

def main():
    # Creates the window for Christmas card
    win = GraphWin("Christmas Card", 500, 500)
    win.setCoords(0, 0, 10, 10)
    center = Point(5, 5)
    win.setBackground("black")

    # Draw snow on the ground
    snow = Rectangle(Point(0, 0), Point(10, 5))
    snow.setFill("white")
    snow.draw(win)

    # Draw tree
    tree = Polygon(Point(2, 3), Point(4, 7), Point(6, 3))
    tree.setFill("green4")
    tree.draw(win)

    # Draw stump
    stump = Rectangle(Point(3.5, 1), Point(4.5, 3.25))
    stump.setFill("brown4")
    stump.draw(win)

    # Draw snowman
    snowmanBase = Circle(Point(8, 6), 1)
    snowmanBase.setFill("white")
    snowmanBase.draw(win)
    snowmanMid = Circle(Point(8, 7.5), 0.75)
    snowmanMid.setFill("white")
    snowmanMid.draw(win)

    # End Program
    # endText = Text(center, "Click again to quit.")
    # endText.setFill("red")
    # endText.setSize(36)
    # endText.draw(win)
    win.getMouse()
    win.close()

main()
