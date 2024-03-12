"""
Prueba las clases creadas mediante un programa con un menú como el que se muestra a continuación:

+---------------------------------------------------------------+
|    VEHÍCULOS                                                  |
|    =========                                                  |
|    1. Anda con la bicicleta.                                  |
|    2. Haz el caballito con la bicicleta.                      |
|    3. Anda con el coche.                                      |
|    4. Quema rueda con el coche.                               |
|    5. Llena el depósito del coche.                            |
|    6. Ver kilometraje de la bicicleta.                        |
|    7. Ver kilometraje del coche.                              |
|    8. Ver el combustible que queda en el depósito del coche.  |
|    9. Ver kilometraje total.                                  |
|    10. Salir.                                                 |
|                                                               |
|    Elige una opción (1-8):                                    |
+---------------------------------------------------------------+

Author: Jorge Pradillo Hinterberger
Date: 01/03/2024
"""
from Tanda2 import menu
from Tanda3.vehicle.vehicle import Vehicle
from Tanda3.vehicle.car import Car
from Tanda3.vehicle.bike import Bike
import random


MIN_KILOMETERS_WITH_BIKE = 1
MAX_KILOMETERS_WITH_BIKE = 100
MIN_KILOMETERS_WITH_CAR = 1
MAX_KILOMETERS_WITH_CAR = 500


def main():
    options = menu.Menu("Anda con la bicicleta", "Haz el caballito con la bicicleta",
                        "Ver kilometraje de la bici", "Anda con el coche",
                        "Quemar rueda con el coche (Llena el depósito antes)",
                        "Llena el deposito del coche", "Ver kilometraje del coche",
                        "Ver combustible que queda en el depósito del coche", "Ver kilometraje total", "Salir",
                        title="VEHÍCULOS")

    while True:
        choice = options.show()
        match choice:
            case 1:
                bicycle_travel()
            case 2:
                bicycle.do_wheelie()
            case 3:
                print(bicycle.kilometers_traveled)
            case 4:
                car_travel()
            case 5:
                car.burn_wheel()
            case 6:
                car.fill_up()
            case 7:
                print(car.kilometers_traveled)
            case 8:
                print(f"Quedan {car.liters_of_fuel:.2f} litros de gasolina")
            case 9:
                print(f"{car.total_kilometers():.2f} km")
            case 10:
                break


def bicycle_travel():
    # random.uniform → Genera un número float aleatorio entre dos valores
    distance = round(random.uniform(MIN_KILOMETERS_WITH_BIKE, MAX_KILOMETERS_WITH_BIKE), 2)
    print(bicycle.travel_kilometers(distance))


def car_travel():
    max_km_car = MAX_KILOMETERS_WITH_CAR
    kilometers = round(random.uniform(MIN_KILOMETERS_WITH_CAR, max_km_car), 2)
    print(car.travel_combustion(kilometers))


if __name__ == "__main__":
    bicycle = Bike()
    car = Car()
    main()
