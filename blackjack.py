""" My game of blackjack.
    Objects are used in later objects.
    Somewhat complex pattern of interaction among parts.
"""

import random


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
        #this puts those values into a string, which you need
    def __repr__(self):
        #this is what the representation will be when it's in a list
        return self.__str__()
    def call_rank(self):
        return self.rank

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
                 "King", "Ace"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        # o the deck is a set of one of every card in an array
        #because of the str and repr methods in the first one, we can print them
    def __str__(self):
        return "{}".format(self.cards)
        #this puts those values into a string, which you need
    def __repr__(self):
        #this is what the representation will be when it's in a list
        return self.__str__()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        #card = random(choice(self.cards)).pop()
        #return card
        return self.cards.pop(0)
        #This is dealing a random card.
class Hand:

    def __init__(self):
        self.hand = []
    def __str__(self):
        return "{}".format(self.hand)
        #this puts those values into a string, which you need
    def __repr__(self):
        #this is what the representation will be when it's in a list
        return self.__str__()
    def new_hand(self, deck):
        self.hand.append(deck.deal())
        self.hand.append(deck.deal())
    def hit(self, deck):
        self.hand.append(deck.deal())

#This is to make an Object using user inputs.  Assume they match the format.
    def enter_hand(self, rank, suit):
        new = Card(suit, rank)
        self.hand.append(new)

# new.enter_hand(input("Enter your card rank: "), input("Enter your card suit: "))
# new.enter_hand(input("Enter your card rank: "), input("Enter your card suit: "))
# print(new.hand)

#Score a hand
#with the Ace exception

    def score_blackjack_hand(self):
        scores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 1}
        scoring = []
        score = 0
        for item in self.hand:
            rank = item.call_rank()
            if rank == "Ace":
                scoring.append(rank)
            else:
                scoring.append(scores[rank])
        for item in scoring:
            if item != "Ace":
                score += item
            elif item == "Ace":
                if score > 10:
                    score += 1
                else:
                     score +=11
        return score


start = Deck()
print(start)
start.shuffle()
print(start)
new = Hand()
new.new_hand(start)

print(new)
print(new.score_blackjack_hand())
