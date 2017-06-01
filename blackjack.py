
import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9",
            "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
        #this puts those values into a string, which you need
    def __repr__(self):
        #this is what the representation will be when it's in a list
        return self.__str__()

class Deck:
    def __init__(self):
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
    scores: {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "Jack": 10,
        "Queen": 10, "King": 10}
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

#This is to make an Object using user inputs.  Assume they match.
    def enter_hand(self, card):
        card1 = input("Enter your card: ")
            if card1 in self.cards:
                self.hand.append(card1)
        #I don't know if this works.

    def score_blackjack_hand(self, hand):
        

#Score a hand
#with the Ace exception
