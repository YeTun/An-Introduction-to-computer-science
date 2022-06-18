class Card:
    """This class represents a playing Card
    it returns a rank 1-13 (Aces count as 1),
    and a suit."""
    def __init__(self, rank, suit, score):
        self.rank = int(rank)
        self.suit = suit
        self.score = score

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        self.score = self.score + self.rank
        return self.score

    def __str__(self):
        if self.rank == 1:
            self.rank = 'Ace'
        elif self.rank == 11:
            self.rank = 'Jack'
        elif self.rank == 12:
            self.rank = 'Queen'
        elif self.rank == 13:
            self.rank = 'King'
        return '{0} of {1}'.format(self.rank, self.suit)