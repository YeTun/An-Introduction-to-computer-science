# Me Computer, Mandalay.
# June 20, 2022
# exercise_4.py
# Simulation of a sanctioned volleyball game (rally scoring)

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(n, winsA, winsB)

def printIntro():
    print("This program simulates a sanctioned volleyball game between two")
    print('teams called "A" and "B". The abilities of each team is')
    print("indicated by a probability (a number between 0 and 1).")
    print("In this system, the team wins a rally is awarded a point,")
    print("even if they were not the serving team. Starting serve alternates each game.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(i+1, probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
        
        if (scoreA >= 27) or (scoreB >= 27):
            print(f"Very exciting math at {i+1}. Scores are {scoreA} and {scoreB}.")
    return winsA, winsB

def findService(x):
    if x % 2 == 0:
        return "B"
    else:
        return "A"

def simOneGame(x, probA, probB):
    # Simulates a single game or volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    # starting serve alternates each game
    serving = findService(x)
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
                scoreB += 1
        elif serving == "B":
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
                scoreA += 1
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise
    if (abs(a-b) >= 2) and (a >= 25 or b >= 25):
        return True
    else:
        return False

def printSummary(n, winsA, winsB):
    # Prints a summary of wins for each players
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
