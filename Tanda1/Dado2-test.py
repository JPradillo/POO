"""
Test de la clase dado 2

Author: Jorge Pradillo Hinterberger
Date: 28/01/2024
"""
from Dado2 import Dice

print("Este programa lanza 4 dados las veces que quieras")
d1 = Dice(4)
d2 = Dice(5, 8)
d3 = Dice(8, 9)
d4 = Dice(10, 10)

throw_times = int(input("¿Cuántas veces desear lanzar los dados? "))
for i in range(throw_times):
    d1.roll_dice()
    d2.roll_dice()
    d3.roll_dice()
    d4.roll_dice()
    print(f"{d1}\n"
          f"{d2}\n"
          f"{d3}\n"
          f"{d4}\n")
