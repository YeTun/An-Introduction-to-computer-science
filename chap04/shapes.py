# shapes.py
# June 15, 2022
# page 90

from graphics import *

def main():
    # Open a graphic window
    win = GraphWin("Shapes")

    # Draw a red circle centered at point (100, 100) with radius 30
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)

    # Put a textual label in the center of the circle
    label = Text(center, "Red Circle")
    label.draw(win)

    # Draw a square using a Rectangle object
    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)

    # Draw a line segment using a Line object
    line = Line(Point(20, 20), Point(180, 165))
    line.draw(win)

    # Draw an oval using the Oval object
    oval = Oval(Point(20, 150), Point(180, 199))
    oval.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()
