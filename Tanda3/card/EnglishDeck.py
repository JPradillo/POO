"""
Baraja inglesa que deriva de la clase Deck.

Author: Jorge Pradillo Hinterberger
Date: 06/03/2024
"""
from Tanda3.card.card import Card
from deck import Deck


class EnglishDeck(Deck):
    def __init__(self):
        values = "A 2 3 4 5 6 7 8 9 10 J Q K".split()
        suits = "SPADES HEARTS DIAMONDS CLUBS".split()
        cards = [Card(suit, value) for suit in suits for value in values]
        super().__init__(cards)

    def __len__(self, cards):
        return len(cards)