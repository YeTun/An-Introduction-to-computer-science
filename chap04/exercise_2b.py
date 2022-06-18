# Me Computer, Mandalay.
# June 15, 2022
# exercise_2.py
# A program that creates an archery target

from graphics import *

def main():
    # Creates the window for the Archery Target
    win = GraphWin("Archery Target", 300, 300)
    win.setCoords(-5, -5, 5, 5)
    center = Point(0, 0)

    # Draws 1st ring - white - maximum radius
    radius = 5
    first = Circle(center, radius)
    first.setFill("white")
    first.setOutline("black")
    first.draw(win)

    # Draws 2nd Ring - black - radius-1
    radius -= 1
    second = Circle(center, radius)
    second.setFill("black")
    second.setOutline("black")
    second.draw(win)

    # Draws 3nd Ring - blue - radius-1
    radius -= 1
    third = Circle(center, radius)
    third.setFill("blue")
    third.setOutline("black")
    third.draw(win)

    # Draws 4nd Ring - red - radius-1
    radius -= 1
    fourth = Circle(center, radius)
    fourth.setFill("red")
    fourth.setOutline("black")
    fourth.draw(win)

    # Draws 5nd Ring (center) - yellow - radius-1
    radius -= 1
    fifth = Circle(center, radius)
    fifth.setFill("yellow")
    fifth.setOutline("black")
    fifth.draw(win)

    # Get click to quit and close window
    endText = Text(center, "Click again to quit.")
    endText.draw(win)
    win.getMouse()
    win.close()

main()