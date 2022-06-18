# Me Computer, Mandalay.
# June 20, 2022
# exercise_13a.py
# random walk - 4 directionsrom random import random

from random import randrange
def main():
    printIntro()
    n = getInputs()
    finalPlace = runSims(n)
    printResults(n, finalPlace)

def printIntro():
    print("This program simulates a random walk. Every turn results in a ")
    print("random step forward. backward, left, or right. At the end the ")
    print("position relative to the start is given. The starting position ")
    print("is [x = 0, y = 0]. A positive x is a right movement, a negative")
    print("results in a left movement. A positive y is a forward movement,")
    print("a negative y is a backward movement. The final position is given")
    print("after the simulation has taken N steps, resulting in [x,y] ending.")

def getInputs():
    n = int(input("Enter the number of random steps to simulate: "))
    return n

def runSims(n):
    # inital starting positon is x= 0, y = 0
    place = [0, 0]
    # moves can be right [0], left [1], forward [2], backward [3] 
    direction = [0, 1, 2, 3]
    for i in range(n):
        move = direction[randrange(0, 4)]
        updatePlace(place, move)
    return place

def updatePlace(place, move):
    # change x value based on rand movement generated
    # 0 = right, 1 = left, 2 = forward, 3 = backward
    # x += 1     x -= 1    y += 1       y -= 1
    # place[0] = x, place[1] = y
    if move == 0:
        place[0] += 1
    elif move == 1:
        place[0] -= 1
    elif move == 2:
        place[1] += 1
    else:
        place[1] -= 1
    return place

def printResults(n, finalPlace):
    print("Out of {0} random steps, the net outcome was {1}.".format(n, \
        finalPlace))

if __name__ == '__main__': main()
