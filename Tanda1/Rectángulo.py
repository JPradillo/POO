"""
Implementa la clase Rectángulo (determinado por dos objetos Point) que además de su constructor
Tendrá dos methods para calcular su área y su perímetro que tienes que transformar en propiedades.
Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos
Que muestre el área y perímetro de dicho rectángulo.

Author: Jorge Pradillo Hinterberger
Date: 18/01/2024
"""

from Point import Point
from typeguard import typechecked


@typechecked    # Lanza una excepción TypeError si no se ingresa un valor con el tipo establecido en el parámetro
class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, value: Point):
        if not isinstance(value, Point):  # Es casi una necesidad para asegurarnos que no es solo un entero lo que manda
            raise TypeError("El valor indicado no es una instancia de la clase Point")
        self.__p1 = value

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("El valor indicado no es una instancia de la clase Point")
        self.__p2 = value

    @property
    def area(self):
        return self.base * self.height

    @property
    def height(self):
        return abs(self.p1.y - self.p2.y)

    @property
    def base(self):
        return abs(self.p1.x - self.p2.x)

    @property
    def perimeter(self):
        return self.base * 2 + self.height * 2

    def __str__(self):
        return f"Rectángulo: {self.base()}x{self.height()}"

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.__p1}, {self.__p2})"
