# Me Computer, Mandalay.
# June 20, 2022
# exercise_11a.py
# probability of 5 of a kind - dice

from random import randrange
def main():
    # print intro
    printIntro()
    # get number of simulations
    n = getInputs()
    # run simulations
    nSuccess = runSims(n)
    # print results
    printResults(n, nSuccess)

def printIntro():
    print("This simulates the probability that rolling five 6-sided dice")
    print("results in 5 of a kind.")

def getInputs():
    n = int(input("Enter the number of rolls to test: "))
    return n

def runSims(n):
    nSuccess = 0
    for i in range(n):
        if rollFive():
            nSuccess += 1
    return nSuccess

def rollFive():
    one = randrange(1, 7, 1)
    two = randrange(1, 7, 1)
    three = randrange(1, 7, 1)
    four = randrange(1, 7, 1)
    five = randrange(1, 7, 1)
    # print("{0} {1} {2} {3} {4}".format(one, two, three, four,five))
    return one == two == three == four == five

def printResults(n, nSuccess):
    print("Out of {0} rolls, {1} were five of a kind.".format(n, nSuccess))
    print("The proability of five of a kind was: {0:0.2%}".format(nSuccess / n))

if __name__ == '__main__': main()
