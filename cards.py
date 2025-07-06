""" Module for playing cards.

Defines two classes: Card and Deck. Card and Deck can be used
to create a deck of playing cards for different card games.
"""

from random import shuffle

class Card:
    """ A playing card with a suit and a value. """

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        if 2 <= value <= 10:
            self.name = str(value)
        else:
            card_names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
            self.name = card_names[value]

    def __str__(self):
        return self.name + " of " + self.suit


class Deck:
    """ A standard deck of 52 playing cards. """

    def __init__(self):
        self.cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for value in range(2, 15):
                self.cards.append(Card(value, suit))
        shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop()
        raise RuntimeError("NO MORE CARDS IN DECK : EMPTY")
