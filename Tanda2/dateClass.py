"""
Nos hemos enterado de que la clase datetime.date ha sido comprometida.
Tenemos que crear una clase nueva para almacenar fechas locales (Date).
En este caso la clase será mutable (los objetos pueden cambiar el día, mes o año).

Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:
  f1 = Date(1, 10, 2020) --> almacena el 1 de Octubre de 2020
  f2 = Date(f1) --> almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Crea methods para:

Sumar y restar días a la fecha.
Restar fechas. Devuelve el número de días comprendidos entre ambas.
Comparar la fecha almacenada con otra.
Saber si el año de la fecha almacenada es bisiesto.
Obtener el día de la semana de una fecha concreta.
El method __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

Author: Jorge Pradillo Hinterberger
Date: 28/02/2024
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Date:
    def __init__(self, day, month=None, year=None):
        if isinstance(day, Date) and month is None and year is None:
            date = day
            self.__day, self.__month, self.__year = date.__day, date.__month, date.__year
        elif isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if not Date.__is_ok(day, month, year):
                raise ValueError("Alguno de los datos introducidos en la fecha no es correcto.")
            self.__day, self.__month, self.__year = day, month, year
        else:
            raise TypeError("La fecha se ha introducido con parámetros erróneos.")

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value: int):
        if not self.__is_ok(value, self.__month, self.__year):
            raise ValueError(f"El día {value} es incorrecto.")
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value: int):
        if not self.__is_ok(self.__day, value, self.__year):
            raise ValueError(f"El mes {value} es incorrecto.")
        self.__month = value

    @property
    def month_name(self):
        month_names = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                       "Octubre", "Noviembre", "Diciembre")
        return month_names[self.__month - 1]

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if not self.__is_ok(self.__day, self.__month, value):
            raise ValueError(f"El año {value} es incorrecto.")
        self.__year = value

    def to_iso_format(self):
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}"

    def is_leap(self):
        return self.__is_leap(self.year)

    def weekday(self):
        total_days = self - Date(1, 1, 1)     # Sabemos que el 1/1/1 fue lunes.
        return total_days % 7

    def __add__(self, value: int):
        if value < 0:
            return self - abs(value)
        new_date = Date(self)      # DateClass se puede sustituir por self.__class__
        for _ in range(value):
            new_date = new_date.__add_day()
        return new_date

    def __add_day(self):
        day, month, year = self.__day + 1, self.__month, self.__year
        if day > Date.__month_days(month, year):
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
        return Date(day, month, year)

    def __sub__(self, value: (int, Date)):
        if isinstance(value, Date):
            return self.__subtract_date(value)
        if value < 0:
            return self + abs(value)
        return self.__subtract_days(value)

    def __subtract_date(self, other: Date):
        if self < other:
            date1, date2 = self, other
            sign = -1
        else:
            date1, date2 = other, self
            sign = 1
        days = 0
        while date1 < date2:
            date1 += 1
            days += 1
        return sign * days

    def __subtract_days(self, n: int):
        new_date = Date(self)
        for _ in range(n):
            new_date = new_date.__subtract_day()
        return new_date

    def __subtract_day(self):
        day, month, year = self.__day - 1, self.__month, self.__year
        if day == 0:  # mes anterior
            month -= 1
            if month == 0:  # nos vamos al año anterior
                month = 12
                year -= 1
            day = Date.__month_days(month, year)
        return Date(day, month, year)

    def __radd__(self, n: int):
        return self + n

    def __eq__(self, other: Date):
        return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)

    def __ne__(self, other: Date):
        return not self == other

    def __gt__(self, other: Date):
        return self.to_iso_format() > other.to_iso_format()

    def __ge__(self, other: Date):
        return self > other or self == other

    def __lt__(self, other: Date):
        return not self >= other

    def __le__(self, other):
        return not self > other

    def __str__(self):
        return f"{self.__day} de {self.month_name} de {self.__year}"

    @staticmethod
    def __is_ok(day: int, month: int, year: int):
        if year < 1:  # año correcto
            return False
        if month < 1 or month > 12:  # mes correcto
            return False
        return 0 < day <= Date.__month_days(month, year)  # día correcto

    @staticmethod
    def __month_days(month: int, year: int):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.__is_leap(year):
            month_days[1] = 29
        return month_days[month - 1]

    @staticmethod
    def __is_leap(year: int):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
