"""
Clase CardPlayer que simule un jugador de naipes. Un jugador tiene un nombre y un conjunto de naipes.
- Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
- Puede deshacerse de una carta.
- Puede recibir cartas.
"""
from typing import List
from card import Card
from deck import Deck
from typeguard import typechecked


@typechecked
class CardPlayer:
    def __init__(self, name: str):
        self.__name = name
        self.__cards = []

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards.copy()

    def receives_card(self, cards: List[Card]):     # Para listar un conjunto de objetos ⇾ List[Obj]
        self.__cards.extend(cards)                  # .extend para añadir una lista dentro de otra lista

    def steal_card(self, deck: Deck):
        card_take = deck.steal()
        self.__cards.append(card_take)

    def throw_card(self, card_to_throw: Card):
        if card_to_throw not in self.__cards:
            raise ValueError("¿Cómo vas a tirar una carta que no tienes?")
        self.__cards.remove(card_to_throw)

    def __str__(self):
        return f"nombre: {self.__name} \ncartas: {self.__cards}"
