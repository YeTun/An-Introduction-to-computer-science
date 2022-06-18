# Me Computer, Mandalay.
# June 20, 2020
# exercise_2c.py

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, shotA, shotB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shotA, shotB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilitites of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.")
    print("Player A serves first in the odd games of the match,")
    print("and player B serves first in the even games.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    shotA = shotB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(i+1, probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1        

        if scoreB == 0:
            # print(scoreA, scoreB)
            shotA += 1
        if scoreA == 0:
            # print(scoreA, scoreB)
            shotB += 1
    return winsA, winsB, shotA, shotB

def findService(x):
    # Player A serves first in the odd games
    if x % 2 == 0:
        return "B"
    else:
        return "A"

def simOneGame(x, probA, probB):
    # Simulates a single game of racquetball between players whoe
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = findService(x)
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        elif serving == "B":
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise  
    return a==15 or b==15 or (a==7 and b==0) or (a==0 and b==7)

def printSummary(winsA, winsB, shotA, shotB):
    # Prints a summary of wins for each players
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    print()
    print("Shutouts for A: {0} ({1:0.1%})".format(shotA, shotA/winsA))
    print("Shutouts for B: {0} ({1:0.1%})".format(shotB, shotB/winsB))

if __name__ == '__main__':  main()
