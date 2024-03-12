"""
- Clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya no hace falta modificar).
- Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar esto).
- El coste por minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos.
- La tarifa se puede cambiar.
- Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada.
- El total tarificado debe aparecer con dos decimales.

Author: Jorge Pradillo Hinterberger
Date: 03/03/2024
"""
from Tanda3.terminal.terminal import Terminal
from typeguard import typechecked
from enum import Enum


@typechecked
class Mobile(Terminal):
    __Rate = Enum("Rate", "RATA MONO BISONTE")
    __PRICE_RATA = 0.06
    __PRICE_MONO = 0.12
    __PRICE_BISONTE = 0.30

    def __init__(self, number: str, rate: str):
        if not Mobile.exists_rate(rate):
            raise ValueError(f"La tarifa indicada no existe. Pruebe de nuevo.")
        super().__init__(number)
        self.__rate = Mobile.__Rate[rate.upper()]
        self.__price = 0

    @classmethod
    def exists_rate(cls, rate: str):
        for r in cls.__Rate:
            if r.name == rate.upper():
                return True
        return False

    @property
    def price(self):
        return self.__price

    @property
    def rate(self):
        return self.__rate.name

    def call(self, other: Terminal, seconds: int):
        super().call(other, seconds)
        minutes = seconds / 60
        match self.__rate:
            case Mobile.__Rate.RATA:
                minute_price = self.__PRICE_RATA
            case Mobile.__Rate.MONO:
                minute_price = self.__PRICE_MONO
            case Mobile.__Rate.BISONTE:
                minute_price = self.__PRICE_BISONTE
        self.__price += minutes * minute_price

    def __str__(self):
        return super().__str__() + f" - tarificados {self.__price:.2f} euros."
