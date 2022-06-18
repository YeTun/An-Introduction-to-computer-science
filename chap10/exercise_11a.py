# Me Computer, Mandalay.
# June 21, 2022
# exercise_11a.py

from card import Card
import random

def main():
    suitArray = ['Spades','Clubs','Diamonds','Hearts']
    n = eval(input("Enter the number of a cards to draw: "))
    
    score = 0
    for i in range(n):
        rank = random.randrange(1,14)
        suit = random.choice(suitArray)
        card = Card(rank, suit, score)
        card.BJValue()
        print(card.__str__())
        score = card.score
    
    print("The Black Jack value of your cards is {0}".format(card.score))

main()
