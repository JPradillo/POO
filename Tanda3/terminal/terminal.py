"""
Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono.
Los terminales se pueden llamar unos a otros y el tiempo de conversación corre para ambos.
A continuación se proporciona el contenido del programa principal que usa esta clase
y el resultado que debe aparecer por pantalla.

Los números de teléfono tienen que validarse como tales al crear el objeto
Solo dígitos, empiezan por 9, 6 o 7, su longitud es de nueve dígitos
No puede haber dos terminales con el mismo número.

Author: Jorge Pradillo Hinterberger
Date: 03/03/2024
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Terminal:
    __unavailable_numbers = []

    def __init__(self, number:str):
        if not Terminal.__number_ok(number):
            raise ValueError("El número introducido no es correcto.")
        if number in Terminal.__unavailable_numbers:
            raise ValueError("El número ya existe. Añade otro diferente.")
        Terminal.__unavailable_numbers.append(number)
        self.__number = number
        self.__time_talk = 0

    @property
    def number(self):
        return self.__number[:3] + " " + self.__number[3:5] + " " + self.__number[5:7] + " " + self.__number[7:9]

    @property
    def time_talk(self):
        return self.__time_talk

    def call(self, other: Terminal, seconds: int):
        if seconds < 0:
            raise ValueError("Los segundos no pueden ser negativos.")
        if other.__number == self.__number:
            raise ValueError("Un número no puede llamarse a si mismo.")
        self.__time_talk += seconds
        other.__time_talk += seconds

    def __str__(self):
        return f"No {self.number} - {self.__time_talk}s de conversación"

    @staticmethod
    def __number_ok(number: str):
        return len(number) == 9 and number[0] in "679" and number.isdigit()
