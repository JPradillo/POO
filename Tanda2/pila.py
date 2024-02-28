"""
Clase pila con distintas operaciones
- Crear la pila con o sin valores iniciales o a partir de otra pila.
- Obtener el número de elementos almacenados (tamaño).
- Saber si está vacía.
- Vaciar completamente la pila.
- Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
- Des apilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
- Leer el elemento superior de la pila sin retirarlo (top).

Author: Jorge Pradillo Hinterberger
Date: 28/01/24
"""
from __future__ import annotations
from typeguard import typechecked


@typechecked
class Stack:
    def __init__(self, *params: int):
        self.__params = list(params)

    @classmethod
    def from_stack(cls, other: Stack):
        new_stack = cls()
        new_stack.__params = other.__params.copy()
        return new_stack

    @property
    def size(self):
        return len(self.__params)

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.__params = []

    def push(self, param):
        return self.__params.insert(0, param)

    def pop(self):
        return self.__params.pop(0)

    def top(self):
        return self.__params[0]

    def __str__(self):
        return f"Los elementos que tiene la pila son {str(self.__params)}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__params})"


if __name__ == "__main__":
    p1 = Stack(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    p2 = Stack()
    p3 = Stack.from_stack(p1)
    print(f"Las pilas creadas son:\n"
          f"Stack1 = {p1}\nStack2 = {p2}\nStack3 = {p3}\n")

    print(f"{p1.top()} es el primer elemento de Stack1.\n")

    print("Si añadimos -1 y 0 a Stack2: ")
    p2.push(0)
    p2.push(-1)
    print(f"{p2}\n")

    print(f"Si quitamos dos parámetros del Stack3 ({p3.pop()}, {p3.pop()}):")
    print(p3)
