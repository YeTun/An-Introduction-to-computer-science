# Me Computer, Mandalay.
# June 20, 2022
# exercise_12a.py
# random walk - 2 directions - forward and back

from random import random
def main():
    printIntro()
    n = getInputs()
    finalPlace = runSims(n)
    printResults(n, finalPlace)

def printIntro():
    print("This program simulates a random walk. Every turn results in a ")
    print("random step forward or backward. At the end the position relative")
    print("is given as a +/- integer. The starting position is 0. A positive")
    print("outcome means net the result was foward, and visa versa.")

def getInputs():
    n = int(input("Enter the number of random steps to simulate: "))
    return n

def runSims(n):
    place = 0
    for i in range(n):
        if random() < 0.50:
            place -= 1
        else:
            place += 1
    return place

def printResults(n, finalPlace):
    print("Out of {0} random steps, the net outcome was {1}.".format(n, \
        finalPlace))

if __name__ == '__main__': main()
