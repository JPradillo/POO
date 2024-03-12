"""
Crea la clase abstracta Vehicle.
Contiene los atributos de clase vehicles_created y total_kilometers
También el atributo de instancia kilometers_traveled.

Además, un method para viajar (travel) que incremente los kilómetros recorridos.

Author: Jorge Pradillo Hinterberger
Date: 29/02/2024
"""
from abc import ABC
from typeguard import typechecked


@typechecked
class Vehicle(ABC):
    # Variables de clase
    __vehicles_created = 0
    __total_kilometers = 0.0

    def __init__(self):
        Vehicle.__vehicles_created += 1
        self.__kilometers_traveled = 0.0

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

    def travel(self, distance: float):
        if distance < 0:
            raise ValueError("La distancia no puede ser negativa.")

        Vehicle.__total_kilometers += distance
        self.__kilometers_traveled += distance

    def __repr__(self):
        return f"{self.__class__.__name__} (kilómetros recorridos -> {self.kilometers_traveled})"

    def __str__(self):
        return f"El {self.__class__.__name__} recorrió {self.__kilometers_traveled}"
