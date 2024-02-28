"""
Clase que almacena duraciones de tiempo (Duration).
Los objetos de esta clase son intervalos de tiempo y se crean de la forma:
- t1 = Duration(1, 20, 30): almacenará 1 hora, 20 minutos y 30 segundos.
- t2 = Duration(2, 75, -10): almacenará 3 horas, 14 minutos y 50 segundos.
- t3 = Duration(t2): almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y methods para:
- Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
- Sumar y restar segundos, minutos u horas (se cambia el objeto actual).
- Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10 h 35 m 5 s.

Author: Jorge Pradillo Hinterberger
Date: 31/01/24
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Duration:
    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and (minutes, seconds) == (None, None):   # Si llega un único parámetro
            other = hours
            self.__hours = other.hours
            self.__minutes = other.minutes
            self.__seconds = other.seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds
            self.__to_seconds()

    def __to_seconds(self):
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("Los segundos no pueden ser negativos. ¿¡Cómo vamos a viajar al pasado!?")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    def __total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        aux = Duration(value, self.__minutes, self.__seconds)
        self.__hours, self.__minutes, self.__seconds = aux.__hours, aux.__minutes, aux.__seconds

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        aux = Duration(self.hours, value, self.__seconds)
        self.__hours, self.__minutes, self.__seconds = aux.__hours, aux.__minutes, aux.__seconds

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        aux = Duration(self.hours, self.__minutes, value)
        self.__hours, self.__minutes, self.__seconds = aux.__hours, aux.__minutes, aux.__seconds

    def __str__(self):
        return f"{self.hours:02d}h {self.minutes:02d}m {self.seconds:02d}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hours:02d}, {self.minutes:02d}, {self.seconds:02d})"

    def add_seconds(self, seconds: int):
        self.seconds += seconds

    def add_minutes(self, minutes: int):
        self.minutes += minutes

    def add_hours(self, hours: int):
        self.hours += hours
                
    def sub_seconds(self, seconds: int):
        self.seconds -= seconds

    def sub_minutes(self, minutes: int):
        self.minutes -= minutes

    def sub_hours(self, hours: int):
        self.hours -= hours

    # Sobrecarga de methods
    def __add__(self, other: Duration):
        return Duration(self.__hours + other.__hours, self.__minutes
                        + other.__minutes, self.__seconds + other.__seconds)

    def __sub__(self, other: Duration):
        return Duration(self.__hours - other.__hours, self.__minutes
                        - other.__minutes, self.__seconds - other.__seconds)

    def __eq__(self, other: Duration):
        return (self.__hours, self.__minutes, self.__seconds) == (other.__hours, other.__minutes, other.__seconds)

    def __lt__(self, other: Duration):
        return self.__total_seconds() < other.__total_seconds()

    def __gt__(self, other: Duration):
        return self.__total_seconds() > other.__total_seconds()

    def __le__(self, other: Duration):
        return self.__total_seconds() <= other.__total_seconds()

    def __ge__(self, other: Duration):
        return self.__total_seconds() >= other.__total_seconds()

    def __ne__(self, other: Duration):
        return self.__total_seconds() != other.__total_seconds()


if __name__ == "__main__":
    t1 = Duration(1, 20, 30)
    t2 = Duration(2, 75, -10)
    t3 = Duration(t2)
    print(f"t1: {t1}\nt2: {t2}\nt3: {t3.__repr__()}\n")

    print(Duration(1, 8, 57) + Duration(12, 52, 3))

    print(f"\n{t3 - t1}\n")
    print(f"t2 != t1 = {t2 != t1}")
    print(f"t2 == t1 = {t2 == t2}")
    print(f"t2 > t1 = {t2 > t1}")
    print(f"t2 < t1 = {t2 < t1}")
    print(f"t2 >= t1 = {t2 >= t1}")
    print(f"t2 <= t1 = {t2 <= t1}")
