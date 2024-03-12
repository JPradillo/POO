"""
Clase deck que simula un conjunto de cartas de naipes.
  - Inicialmente, tiene las cartas que le llegan con el constructor.
  - Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
  - Le pueden quitar la primera carta (robar).
  - Puede barajarse.

Author: Jorge Pradillo Hinterberger
Date: 05/03/2024
"""
import random
from typing import List
from card import Card
from typeguard import typechecked


@typechecked
class Deck:
    def __init__(self, cards: List[Card]):
        self.__cards = cards.copy()

    @property
    def how_many_cards(self):
        return len(self.__cards)

    def deal(self, player, number: int):
        self.__check_deal(number)

        # Repartimos y actualizamos las cartas
        top_cards = self.__cards[:number]
        player.receives_card(top_cards)
        self.__cards = self.__cards[number:]

    def __check_deal(self, number):
        if number < 0:
            raise ValueError("Tiene que haber cartas que pueda repartir.")
        if number > len(self.__cards):
            raise ValueError("No hay suficientes cartas")

    def steal(self):
        if len(self.__cards) == 0:
            raise ValueError("No hay cartas para robar.")
        return self.__cards.pop()

    def shuffle(self):
        random.shuffle(self.__cards)    # random.shuffle reordena la lista de forma aleatoria.

    def __str__(self):
        return str(self.__cards)
