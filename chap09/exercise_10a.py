# Me Computer, Mandalay.
# June 20, 2022
# exercise_10a.py
# Estimating pi

from random import random
def main():
    # print intro
    printIntro()
    # get number of simulations
    n = getInputs()
    # run simulations
    h = runSims(n)
    # print results
    piEstimate = 4 * (h / n)
    printResults(n, h, piEstimate)

def printIntro():
    print("This program approximates pi by simulating a 2x2 square and circle")
    print("with a radius of 2. The program randomly generates n points inside")
    print("the square. If the point is inside the circle radius it counts as")
    print("a hit. Finally it approximates pi by multiplying the ratio of hits")
    print("by 4.")

def getInputs():
    n = int(input("Enter the number of attempts to generate: "))
    return n

def runSims(n):
    h = 0
    for i in range(n):
        # generate x and y coordinates
        x = 2 * random() - 1
        y = 2 * random() - 1
        # print("X: {0} Y: {1}".format(x, y))
        # check if point is inside the inscribed circle
        if x ** 2 + y ** 2 <= 1:
            h += 1
    return h

def printResults(n, h, piEstimate):
    print("Based on results of {0} points with {1} inside the inscirbed circle".format(n, h))
    print("Pi is approximately: {0}.".format(piEstimate))

if __name__ == '__main__': main()
