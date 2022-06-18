# Me Computer, Mandalay.
# June 20, 2022
# exercise_1b.py
# Simulation of a racquetball game

from random import random

def main():
    printIntro()
    probA, probB, n, matches = getInputs()
    winsA, winsB = simNGames(matches, n, probA, probB)
    printSummary(matches, winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.")
    print("Player A serves first in the odd games of the match,")
    print("and player B serves first in the even games.")

def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    matches = int(input("How many matches per game? ")) 
    return a, b, n, matches

def simNGames(matches, n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        matchesA, matchesB = simOneMatch(matches, probA, probB)        
        if matchesA > matchesB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        # print(f" - - Wins A: {winsA} Wins B: {winsB} - - ")
    return winsA, winsB

def simOneMatch(matches, probA, probB):
    matchesA = matchesB = 0
    matchCount = 1
    while not(matchOver(matches, matchesA, matchesB)):
        # alternate serving, A serves odd matches, B serves even
        if (matchCount % 2 != 0):
            serving = "A"
        else:
            serving = "B"
        
        scoreA, scoreB = simOneGame(serving, probA, probB)
        if scoreA > scoreB:
            matchesA += 1
        else:
            matchesB += 1
        matchCount += 1        
        # print(f" - Matches A: {matchesA} Matches B: {matchesB} - ")
    return matchesA, matchesB

def matchOver(matches, a, b):
    # a and b represent scores for a racquetball matches
    # must win by 2
    # returns True if the game is over, False otherwise.
    return (a > matches / 2 or b > matches / 2) and (abs(a - b) >= 2)

def simOneGame(serving, probA, probB):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    print(f"Game - Score A: {scoreA} Score B: {scoreB}")
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # must win by 2
    # returns True if the game is over, False otherwise.
    return (a >= 15 or b >= 15) and (abs(a - b) >= 2)

def printSummary(matches, winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print(f"\n{n} games ({matches} games per match) simulated.")
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))

if __name__ == '__main__': main()
