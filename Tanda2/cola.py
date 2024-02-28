"""
Clase cola con distintas operaciones
- Crear la cola con o sin valores iniciales o a partir de otra cola.
- Obtener el número de elementos almacenados (tamaño).
- Saber si está vacía.
- Vaciar completamente la cola.
- Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
- Desencolar (dequeue): se saca (devolverlo) y se elimina el elemento frontal de la cola (primer elemento que entró)
- Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Author: Jorge Pradillo Hinterberger
Date: 30/01/24
"""
from typeguard import typechecked


@typechecked
class Queue:
    def __init__(self, *params):
        if len(params) == 1 or isinstance(params[0], Queue):
            self.__params = params[0].__params.copy()
        else:
            for i in params:
                if not isinstance(i, int):
                    raise TypeError("El valor introducido no es correcto ya que se espera un número entero.")
            self.__params = list(params)

    @property
    def size(self):
        return len(self.__params)

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.__params = []

    def enqueue(self, param):
        return self.__params.append(param)

    def dequeue(self):
        return self.__params.pop(0)

    def front(self):
        return self.__params[0]

    def __str__(self):
        return str(self.__params)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__params})\n"


if __name__ == "__main__":
    q1 = Queue(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    q2 = Queue(q1)
    print(f"cola 1: {q1}\ncola 2: {q2}")

    q1.enqueue('A')
    print(q1, "es el valor final tras añadir 'A' a la cola 1.\n")
    q2.front()
    q2.dequeue()
    print(q2, "es el valor final tras eliminar un elemento de la cola 2.\n")
