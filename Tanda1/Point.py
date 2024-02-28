"""
Implementa una clase Point con sus atributos x e y. La clase debe contener:
su constructor, los getters y setters (propiedades)
un invert_coordinates() que invierta las coordenadas x e y del punto.

Además, la clase debe tener un __str__() para poder imprimir los puntos en formato “(x, y)”.
Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el method __str__()
imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto.

Author: Jorge Pradillo Hinterberger
Date: 18/01/2024
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = float(value)     # Al obligar a introducir un float, le da sentido al setter. No float = error

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = float(value)     # Al obligar a introducir un float, le da sentido al setter. No float = error

    def invert_coordinates(self):
        self.__x, self.__y = self.__y, self.__x
        return self.__x, self.__y

    def __str__(self):
        return f"'({self.__x}, {self.__y})'"

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.__x}, {self.__y})"
