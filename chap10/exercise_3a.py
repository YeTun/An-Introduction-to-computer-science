# Me Computer, Mandalay.
# June 21, 2022
# exercise_3.py
# Three Button Monte. Should draw 3 buttons Door 1, Door 2, Door 3
# One door is the winner, prompt user to select a door
# Guess the right door and win, guess the wrong door lose and reveal the winning door

from graphics import *
from random import randrange
from button import Button

def main():
    win = setupGraph()
    
    door1 = Button(win, Point(1, 4.5), 1, 2, "Door 1")
    door2 = Button(win, Point(2.5, 4.5), 1, 2, "Door 2")
    door3 = Button(win, Point(4, 4.5), 1, 2, "Door 3")

    quitButton = Button(win, Point(2.5, 0.5), 1, 0.5, "Quit")

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        winner = randrange(1, 4)
        if ((door1.clicked(pt) and winner == door1.setValue(1)) or 
            (door2.clicked(pt) and winner == door2.setValue(2)) or
            (door3.clicked(pt) and winner == door3.setValue(3))):
            winnerButton = Button(win, Point(2.5, 2.5), 3, 1, "Winner")
        else:
            loserButton = Button(win, Point(2.5, 2.5), 3, 1, "Loser, Correct Answer: {0}".format(winner))
        pt = win.getMouse()
    win.close()

def setupGraph():
    win = GraphWin("3 Door Monty", 500, 600)
    win.setBackground("white")
    win.setCoords(0.0, 0.0, 5.0, 6.0)
    return win

main()

