import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9",
        "10", "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, rank):
        if suit in suits:
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
         return self.suit

    def get_rank(self):
        return self.rank

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += " " + card.__str__()
        return "Deck contains" + result

class Hand:
    def __init__(self):
        self.cards = []
    def __str__(self):
        result = ""
        for card in self.cards:
            result += + card.__str__
        return "Hand contains" + result
    def add_card(self, card):
        self.cards.append(card)
    def get_value(self):
        value = 0
        contains_ace = False
        for card in self.cards:
            rank = card.get_rank()
            value += values[rank]
            if rank == "Ace":
                cotains_ace = True

        if value < 11 and contains_ace:
            value += 10
        return value
