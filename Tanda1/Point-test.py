"""
Test objeto Point

Author: Jorge Pradillo Hinterberger
Date: 18/01/2024
"""

from Point import Point

print("Este programa es un test que usa la clase Point para crear un punto e imprimir las coordenadas.")

x = float(input("Ingrese el valor del eje x: "))
y = float(input("Ingrese el valor del eje y: "))

p = Point(x, y)
print(f"El valor del punto creado es: {p.__str__()}")
print(f"El valor de la coordenada x = {p.x}")

while True:
    change = input("¿Desea invertir el valor de las coordenadas (s/n)? ")
    if change == "s":
        print(f"La coordenada invertida es {p.invert_coordinates()}")
    elif change == "n":
        break
    else:
        print("ERROR. Introduzca un valor válido.")

p.x = 0
print(f"El valor tras cambiar la coordenada x es = {p}")
