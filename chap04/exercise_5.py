# Me Computer, Mandalay.
# June 15, 2022
# exercise_5.py
# A simple graphics program that draws 5 dice

from graphics import *

def main():
    # Creates the window for picture of 5 dice in straight
    win = GraphWin("Dice Straight", 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground("black")

    diceColor = "green"
    dotColor = "black"
    diceX1 = 0.5
    diceY1 = 5.5

    # Create dice 1
    d1 = Rectangle(Point(diceX1, diceY1), Point(diceX1 + 1, diceY1 + 1))
    d1.setFill(diceColor)
    d1.draw(win)
    d1One = Circle(Point(1, 6), 0.25)
    d1One.setFill(dotColor)
    d1One.draw(win)

    # Create dice 2
    d2 = Rectangle(Point(diceX1 + 1.5, diceY1), Point(diceX1 + 2.5, diceY1 + 1))
    d2.setFill(diceColor)
    d2.draw(win)
    d2One = Circle(Point(2.25, 6), 0.15)
    d2One.setFill(dotColor)
    d2One.draw(win)
    d2Two = Circle(Point(2.75, 6), 0.15)
    d2Two.setFill(dotColor)
    d2Two.draw(win)

    # Create dice 3
    d3 = Rectangle(Point(diceX1 + 3, diceY1), Point(diceX1 + 4, diceY1 + 1))
    d3.setFill(diceColor)
    d3.draw(win)
    d3One = Circle(Point(3.75, 6.25), 0.15)
    d3One.setFill(dotColor)
    d3One.draw(win)
    d3Two = Circle(Point(4.25, 6.25), 0.15)
    d3Two.setFill(dotColor)
    d3Two.draw(win)
    d3Three = Circle(Point(4, 5.75), 0.15)
    d3Three.setFill(dotColor)
    d3Three.draw(win)

    # Create dice 4
    d4 = Rectangle(Point(diceX1 + 4.5, diceY1), Point(diceX1 + 5.5, diceY1 + 1))
    d4.setFill(diceColor)
    d4.draw(win)
    d4One = Circle(Point(5.25, 6.25), 0.15)
    d4One.setFill(dotColor)
    d4One.draw(win)
    d4Two = Circle(Point(5.75, 6.25), 0.15)
    d4Two.setFill(dotColor)
    d4Two.draw(win)
    d4Three = Circle(Point(5.25, 5.75), 0.15)
    d4Three.setFill(dotColor)
    d4Three.draw(win)
    d4Four = Circle(Point(5.75, 5.75), 0.15)
    d4Four.setFill(dotColor)
    d4Four.draw(win)

    # Create dice 5
    d5 = Rectangle(Point(diceX1 + 6, diceY1), Point(diceX1 + 7, diceY1 + 1))
    d5.setFill(diceColor)
    d5.draw(win)
    d5One = Circle(Point(diceX1 + 6.2, diceY1 + .25), 0.15)
    d5One.setFill(dotColor)
    d5One.draw(win)
    d5Two = Circle(Point(diceX1 + 6.8, diceY1 + .25), 0.15)
    d5Two.setFill(dotColor)
    d5Two.draw(win)
    d5Three = Circle(Point(diceX1 + 6.2, diceY1 + .75), 0.15)
    d5Three.setFill(dotColor)
    d5Three.draw(win)
    d5Four = Circle(Point(diceX1 + 6.8, diceY1 + .75), 0.15)
    d5Four.setFill(dotColor)
    d5Four.draw(win)
    d5Five = Circle(Point(diceX1 + 6.5, diceY1 + .5), 0.15)
    d5Five.setFill(dotColor)
    d5Five.draw(win)

    # End Program
    # endText = Text(Point(5, 5), "Click again to quit.")
    # endText.setFill("red")
    # endText.setSize(36)
    # endText.draw(win)
    win.getMouse()
    win.close()

main()
