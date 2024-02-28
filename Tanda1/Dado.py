"""
Programa con clase Dado que simula el funcionamiento de un dado con caras del 1 al 6
que tienen la misma probabilidad de salir y un programa de prueba.
"""

import random

FACES_OF_A_DIES = 6


class Dice:
    def __init__(self, faces=FACES_OF_A_DIES):
        self.__faces = faces

    def throw(self):
        return random.randint(1, self.__faces)


if __name__ == '__main__':
    dice1 = Dice()

    print(f"El resultado es {dice1.throw()}")
