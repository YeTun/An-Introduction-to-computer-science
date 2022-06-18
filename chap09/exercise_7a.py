# Me Computer, Mandalay.
# June 20, 2022
# exercise_7a.py

# 2, 3, or 12 the player loses
# 7 or 11 the player wins
# Any other roll initiates roll for points
# Roll for 7 (loss) or 11 (win)

from random import randrange

def main():
    # print intro
    printIntro()
    # get inputs
    n = getInputs()
    # sim games
    nWins = simGames(n)
    # print results
    printResults(n, nWins)

def printIntro():
    print("This program simulates a craps games using a pair of 6-sided die.")
    print("The user inputs the number of games to simulate and the program")
    print("calculates the estimated probability based on the games simulated.")
    print("The rule is if the initial roll is 2, 3, or 12 the player loses.")
    print("If the initial roll is 7 or 11 the player wins. Otherwise, the ")
    print("player rolls for a point, trying to re-roll the initial value, ")
    print("however if the player rolls 7 before - they lose.")

def getInputs():
    # get the number of games to simulate
    n = int(input("Enter the number of craps games to simulate: "))
    return n

def simGames(n):
    # sims n games of craps
    # returns number of wins (nWins)
    nWins = 0
    for i in range(n):
        if simOneGame():
            nWins += 1
    return nWins

def simOneGame():
    # sim one game of craps
    # return True if won, false if lost 
    result, initalRoll = initialRoll()
    while type(result) != bool:
        roll = randrange(2, 13, 1)
        #print(roll)
        if roll == initalRoll:
            result = True
        elif roll == 7:
            result = False
        else:
            continue
    #print("W(True) L(False): {0} Initial Roll: {1}".format(
    #    result, initalRoll))
    return result

def initialRoll():
    # first roll of the die
    # if roll is 2, 3, 12 return loss and roll
    # if roll is 7 or 11 return win and roll
    # if other, return n/a and roll
    roll = randrange(2, 13, 1)
    if roll == 2 or roll == 3 or roll == 12:
        return False, roll
    elif roll == 7 or roll == 11:
        return True, roll
    else:
        return "n/a", roll

def printResults(n, nWins):
    # prints the results of the simulation
    print("Out of {0} games simulated there were {1} games won.".format(n, nWins))
    print("The win percentage is {0:0.1%}.".format(nWins / n))

if __name__ == '__main__': main()
