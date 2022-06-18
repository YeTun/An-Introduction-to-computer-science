# Me Computer, Mandalay.
# June 20, 2020
# exercise_9.py
# Simulation of a blackjack game - estimate probability of a dealer bust
# for each starting card [ace - 10]

from random import randrange
def main():
    # print intro
    printIntro()
    # get number of simulations for each card
    n = getInputs()
    # for card in sequence
    startValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    for initialCard in startValues:
        # simulate games
        nDealerBusts = simulateGames(n, initialCard)
        # print results
        printResults(initialCard, n, nDealerBusts)

def printIntro():
    print("This program simulates the probability a dealer busts in a game")
    print("of blackjack. Dealer takes cards until they reach 17 or higher.")
    print("Ace is counted as 11 when it results in total between 17 and 21.")
    print("Otherwise the Ace is counted as 1. It runs simulations for each")
    print("possible starting card value [ace - 10/face card].")

def getInputs():
    n = int(input("How many games do you want to simulate? "))
    return n

def simulateGames(n, initialCard):
    nDealerBusts = 0
    for i in range(n):
        if simOneGame(initialCard):
            nDealerBusts += 1
    return nDealerBusts

def simOneGame(initialCard):
    # simulate one game
    # return True if dealer busts, else return False
    dealerHand = [initialCard]

    # initially draw 2 cards
    dealerHand.append(drawOne())

    # continue to draw until 17 or greater is hit
    while handValue(dealerHand) < 17:
        dealerHand.append(drawOne())
    # print(handValue(dealerHand))
    # if hand is > 21 dealer has busted
    return handValue(dealerHand) > 21

def handValue(hand):
    # takes in list of cards in hand & calculates value
    # ace is worth 10 if it results in hand between 17 & 21
    # face cards are worth 10
    # return True when game is over
    hasAce = "Ace" in hand
    total = 0
    for i in hand:
        if i in ["Jack", "Queen", "King"]:
            total += 10
        elif i == "Ace":
            total += 1
        else:
            total += i
    if hasAce and (total >= 7 and total <= 11):
        total += 10
    return total

def drawOne():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    card1 = randrange(0, 13, 1)
    return deck[card1]

def printResults(initialCard, n, nDealerBusts):
    print("If the dealer starts with an initial card: {0}".format(initialCard))
    print("Out of {0} games, the dealer busted {1} times.".format(n, nDealerBusts))
    print("This represents a {0:0.2%} the dealer will bust in any given game.".format(nDealerBusts / n))
    print()

if __name__ == '__main__': main()
