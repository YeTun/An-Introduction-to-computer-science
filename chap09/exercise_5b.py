# Me Computer, Mandalay.
# June 20, 2022
# exercise_5.py
# Simulation of a volleyball game to compare rally scoring versus only scoring when serving

from random import random

def main():
    printIntro()
    matches, sets, probA, probB = getInputs()
    
    # turn rally scoring on
    rally = 1
    rallyWinsA, rallyWinsB, rallySoGA, rallySoGB, rallySoSA, rallySoSB = simMatches(matches, sets, rally, probA, probB)
    
    # turn rally scoring off
    rally = 0 
    servingWinsA, servingWinsB, servingSoGA, servingSoGB, servingSoSA, servingSoSB = simMatches(matches, sets, rally, probA, probB)
    
    print("Rally scoring stats:")
    printOutro(rallyWinsA, rallyWinsB, rallySoGA, rallySoGB, rallySoSA, rallySoSB)
    
    print("Serve scoring stats:")
    printOutro(servingWinsA, servingWinsB, servingSoGA, servingSoGB, servingSoSA, servingSoSB)

def printIntro():
    print("This program compares the effect of rally scoring versus only")
    print("scoring while holding the serve in volleyball games to 25.")
    print("The winner must win by 2 or more points. By simulating games")
    print("between players A and B where the ability of each player is")
    print("indicated by a probability [number between 0 and 1] that the")
    print("player wins a point. The program compares the number of wins")
    print("for each player in the different systems.")

def getInputs():
    # get necessary inputs from user
    probA = float(input("What is the probability that player A wins point when serving? "))
    probB = float(input("What is the probability that player B wins point when serving? "))
    matches = int(input("Enter the number of matches to simulate: "))
    sets = int(input("Enter the number of sets per match: "))
    return matches, sets, probA, probB

def simMatches(matches, sets, rally, probA, probB):
    # simulates loop of matches [length given by user] of between player A & B
    # returns winsA and winsB, shutout sets a/b, and shutout games a/b
    winsA = winsB = 0
    shutOutSetsA = shutOutSetsB = 0
    shutOutGA = shutOutGB = 0
    for i in range(matches):
        setsA = setsB = 0
        setsA, setsB, shutOutGamesA, shutOutGamesB = simOneSet(sets, rally, probA, probB)
        if setsA > setsB:
            winsA += 1
        else:
            winsB += 1
        if setsA > setsB and setsB == 0:
            shutOutSetsA += 1
            shutOutGA += shutOutGamesA
        if setsB > setsA and setsA == 0:
            shutOutSetsB += 1
            shutOutGB += shutOutGamesB
    return winsA, winsB, shutOutGA, shutOutGB, shutOutSetsA, shutOutSetsB

def simOneSet(sets, rally, probA, probB):
    # simulates loop of sets until one player wins > 50% of possible sets
    # returns sets won by A / B as well as games won by shutout
    setsA = setsB = 0
    shutOutGamesA = shutOutGamesB = 0
    count = 1
    while not (matchOver(sets, setsA, setsB)):
        # player A serves odd games
        if count % 2 != 0:
            serve = "A"
        else:
            serve = "B"
        gamesA = gamesB = 0
        gamesA, gamesB = simOneGame(rally, serve, probA, probB)
        if gamesA > gamesB:
            setsA += 1
        else:
            setsB += 1
        if gamesA > gamesB and gamesB == 0:
            shutOutGamesA += 1
        if gamesB > gamesA and gamesA == 0:
            shutOutGamesB += 1
        count += 1 
        #print("Sets A: {0} Sets B: {1} S/O Games A: {2} S/O Games B: {3}".format(
        #    setsA, setsB, shutOutGamesA, shutOutGamesB))
    return setsA, setsB, shutOutGamesA, shutOutGamesB

def matchOver(sets, setsA, setsB):
    # tests if player A or B has won more than 50% of sets in match
    return (setsA > sets / 2 or setsB > sets / 2)

def simOneGame(rally, serving, probA, probB):
    # simulates single game of volleyball between players A & B
    # abilities are represented by probabilities, scoring can either be
    # rally (rally = 1) or only while holding serve (rally = 0)
    # returns the final score of the match
    scoreA = scoreB = 0
    while not (gameOver(scoreA, scoreB)):
        # for rally scoring
        if rally == 1:
            if (serving == "A"):
                if random() < probA:
                    scoreA += 1
                else:
                    scoreB += 1
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    scoreA += 1
                    serving = "A"
        # for scoring while holding serve
        else:
            if serving == "A":
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
        # print("A:{0} B:{1}".format(scoreA, scoreB))
    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    return (scoreA >= 25 or scoreB >= 25) and (abs(scoreA - scoreB) >= 2)

def printOutro(winsA, winsB, soGA, soGB, soSA, soSB):
    print("A won {0} matches [win pct: {1}].".format(winsA, winsA / (winsA + winsB)))
    print("A shutout {0} games and {1} sets.".format(soGA, soSA))
    print("B won {0} matches [win pct: {1}].".format(winsB, winsB / (winsA + winsB)))
    print("B shutout {0} games and {1} sets.".format(soGB, soSB))

if __name__ == '__main__': main()
