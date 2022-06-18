# Me Computer, Mandalay.
# June 20, 2022
# exercise_5.py

from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA1, winsB1 = normalVolley(n, probA, probB)
    winsA2, winsB2 = rallyVolley(n, probA, probB)
    printSummary(n, winsA1, winsB1, winsA2, winsB2)

def printIntro():
    print("This program is designed to compare the difference between Normal")
    print("and Rally scoring in a simulation of (n) games of Volleyball")
    print("given a probability (a number between 0 and 1) that reflects the")
    print("likelihood of a team winning the serve.")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def normalVolley(n, probA, probB):
    # Simulates a single game of volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    # Games to 15, can only score on own serve
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(i+1, probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def findService(x):
    if x % 2 == 0:
        return "B"
    else:
        return "A"

def simOneGame(x, probA, probB):
    # Simulates a single game of volleyball between players whose
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
        if serving == "B":
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise
    if a > 15 or b > 15:
        if abs(a-b) >= 2:
            return True
        else:
            return False
    else:
        return False

def rallyVolley(n, probA, probB):
    # Simulates a single game of volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(i+1, probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def findService(x):
    if x % 2 == 0:
        print(f"Serving B {x}")
        return "B"
    else:
        print(f"Serving A {x}")
        return "A"

def simOneGame(x, probA, probB):
    # Simulates a single game of volleyball between players whose
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
    if a > 25 or b > 25:
        if abs(a-b) >= 2:
            return True
        else:
            return False
    else:
        return False

def printSummary(n, winsA1, winsB1, winsA2, winsB2):
    # Prints a summary of wins for each players
    print("\nGames simulated: ", n)
    print("Results for Normal Volleyball to 15, score on own serve.")
    print("Wins for A: {0} ({1:0.1%})".format(winsA1, winsA1/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB1, winsB1/n))
    print()
    print("Results for Rally Volleyball to 25, score on any serve.")
    print("Wins for A: {0} ({1:0.1%})".format(winsA2, winsA2/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB2, winsB2/n))
    print()

    devA = (winsA2/n - winsA1/n)
    devB = (winsB2/n - winsB1/n)
    if (winsA1 > winsB1) and (winsA2 > winsB2):
        if devA > 0:
            print("Team A's advantage was magnified {0:0.1%} in their favor".format(devA))
            print("during the rally scoring match.")
        elif devA < 0:
            print("Team A's advantage was reduced {0:0.1%} in their favor".format(abs(devA)))
            print("during the rally scoring match.")
        else:
            print("The scoring differences were not statistically significant.")
    elif (winsB1 > winsA1) and (winsB2 > winsA2):
        if devB > 0:
            print("Team B's advantage was magnified {0:0.1%} in their favor".format(devB))
            print("during the rally scoring match.")
        elif devB < 0:
            print("Team B's advantage was reduced {0:0.1%} in their favor".format(abs(devB)))
            print("during the rally scoring match.")
        else:
            print("The scoring differences were not statistically significant.")
    else:
        print("Neither team's advantage was statistically significant.")
        print("If the initial probabilities were near equal, it is impossible to")
        print("derive significance from the data.")
        print("Try a larger sample size.")

if __name__ == '__main__': main()
