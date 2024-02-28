"""
Crea una clase "Fraction" inmutable (solo getters para numerador y denominador)
Podemos hacer las siguientes operaciones:

- Construir un objeto Fracción pasándole al constructor el numerador y el denominador.
    * La fracción se construye simplificada, no se puede dividir por cero.
- Obtener resultado de la fracción (número real).
- Multiplicar la fracción por un número (el methods devuelve otra fracción, simplificada).
- Multiplicar, dividir, sumar y restar fracciones (los methods devuelven otra fracción, simplificada).
- Comparar fracciones entre sí o con enteros usando los operadores relacionales.

Author: Jorge Pradillo Hinterberger
Date: 11/02/2024
"""
from __future__ import annotations
from math import gcd
from typeguard import typechecked


@typechecked
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("El denominador no puede ser 0.")
        mcd = gcd(numerator, denominator)
        self.__numerator = numerator // mcd
        self.__denominator = denominator // mcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @property
    def result(self):
        return self.__numerator / self.__denominator

    def __mul__(self, other: (int, Fraction)):
        if isinstance(other, int):
            return Fraction(self.__numerator * other, self.__denominator)
        elif isinstance(other, Fraction):
            return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)
        else:
            raise TypeError("El valor no es correcto, debes introducir un entero u otra fracción.")

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other: Fraction):
        if isinstance(other, Fraction):
            return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other: Fraction):
        return Fraction(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __eq__(self, other: Fraction):
        return (self.__numerator, self.__denominator) == (other.__numerator, other.__denominator)

    def __ne__(self, other: Fraction):
        return not (self == other)

    def __lt__(self, other: Fraction):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __gt__(self, other: Fraction):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __le__(self, other: Fraction):
        return self.__numerator * other.__denominator <= other.__numerator * self.__denominator

    def __ge__(self, other: Fraction):
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"
