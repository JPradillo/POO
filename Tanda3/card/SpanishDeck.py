"""
Baraja española que deriva de la clase Deck.

Author: Jorge Pradillo Hinterberger
Date: 06/03/2024
"""
from Tanda3.card.card import Card
from deck import Deck


class SpanishDeck(Deck):
    def __init__(self):
        values = "1 2 3 4 5 6 7 Sota Caballo Rey".split()
        suits = "OROS COPAS ESPADAS BASTOS".split()
        cards = [Card(suit, value) for suit in suits for value in values]
        super().__init__(cards)

    def __len__(self, cards):
        return len(cards)