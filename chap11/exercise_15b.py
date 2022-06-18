from deck import Deck
from hand import Hand

def main():
    # suitArray = ['Spades','Clubs','Diamonds','Hearts']
    # n = eval(input("Enter the number of a cards to draw: "))
    # score = 0
    # for i in range(n):
    #     rank = random.randrange(1,14)
    #     suit = random.choice(suitArray)
    #     card = Card(rank, suit, score)
    #     card.BJValue()
    #     print(card.__str__())
    #     score = card.score
    # print("The Black Jack value of your cards is {0}".format(card.score))

main()

deck = Deck(suits, ranks)
deck.newDeck()
deck.shuffle()
#print(deck.deck)
print(deck.dealCard())
print(deck.removed)
print(deck.cardsLeft())
print(type(deck.deck))