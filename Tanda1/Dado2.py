"""
Implementar otra clase Dado. Por defecto el dado tendrá 6 caras.
Tendremos tres formar de construir un dado
- uno al que no se le pasa nada e inicializa el dado al azar
- otro al que solo se le pasa que número tiene el dado en la cara superior
- otro con el número del dado en la cara superior y el número de caras del dado.
Implementa los getters, el method roll() que tirará el dado al azar y el __str__().
Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.

Author: Jorge Pradillo Hinterberger
Date: 28/01/24
"""
import random
DEFAULT_FACES = 6


class Dice:
    def __init__(self, top_face=random.randint(1, DEFAULT_FACES), faces=DEFAULT_FACES):
        if faces <= 0:
            raise ValueError("La cantidad de caras tiene que ser mayor a 4 ya que no existen dados con menos caras.")
        self.__faces = faces

        if top_face <= 0 or top_face > faces:
            raise ValueError("El valor introducido no es correcto ya que es mayor al número de caras que tiene el dado")
        self.__top_face = top_face

    @property
    def faces(self):
        return self.__faces

    @faces.setter
    def faces(self, value):
        self.__faces = value

    @property
    def top_face(self):
        return self.__top_face

    @top_face.setter
    def top_face(self, value):
        self.__top_face = value

    def roll_dice(self):
        self.__top_face = random.randint(1, self.__faces)

    def __str__(self):
        return f"El dado tiene {self.__faces} caras y la cara de arriba es {self.__top_face}."

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.__top_face}, {self.__faces})"
