"""
Clase Carta que simule una carta de naipes.
Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto de valores)

Author: Jorge Pradillo Hinterberger
Date: 04/03/2024
"""
from typeguard import typechecked


@typechecked
class Card:
    def __init__(self, values: str, suits: str):
        self.__values = values
        self.__suits = suits

    @property
    def values(self):
        return self.__values

    @property
    def suits(self):
        return self.__suits
