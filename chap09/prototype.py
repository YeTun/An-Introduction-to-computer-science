# prototype.py

from random import random

def simOneGame():
    scoreA = 0
    scoreB = 0
    serving = "A"
    for i in range(5):
        if serving == "A":
            if random() < .5:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < .5:
                scoreB += 1
            else:
                serving = "A"
        print(i+1, scoreA, scoreB)

if __name__ == "__main__":
    simOneGame()