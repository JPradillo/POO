"""
Subclase Car que deriva de Vehicle.

- Tendremos una variable de instancia con los litros de combustible que quedan en el depósito, inicialmente cero.
- Tendremos un method para quemar rueda y otro para llenar el depósito.
- Cuando el coche viaje disminuirá el número de litros en el depósito en relación con los kilómetros viajados.
  Si no hay combustible suficiente, el coche recorrerá únicamente los kilómetros que pueda.
- Para simplificar, cada kilómetro recorrido consumirá 0,1 litros de combustible.
- En un depósito caben 50 litros y quemar rueda consume 1 litro de combustible.

Author: Jorge Pradillo Hinterberger
Date: 29/02/2024
"""
from vehicle import Vehicle
from typeguard import typechecked


@typechecked
class Car(Vehicle):
    __FULL_TANK_CAPACITY = 50.0
    __LITERS_PER_KM = 0.1

    def __init__(self):
        super().__init__()
        self.__liters_of_fuel = 0.0

        # Arte ASCII sacado de la subclase Car del github de Rafael del Castillo.
        self.__burn_wheel = "  _    _             /'_'_/.-''/                             _______\n" \
                          + "  \`../ |o_..__     / /__   / /  -= WORLD CHAMPIONSHIP =-   _\=.o.=/_\n" \
                          + "`.,(_)______(_).>  / ___/  / /                             |_|_____|_|\n" \
                          + "~~~~~~~~~~~~~~~~~~/_/~~~~~/_/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~1º~DAW~A~~\n"

    def burn_wheel(self):
        if self.__liters_of_fuel >= 1:
            print(self.__burn_wheel)
            self.__liters_of_fuel -= 1
        else:
            raise ValueError("El coche no puede quemar rueda porque no tiene combustible suficiente.")

    @property
    def liters_of_fuel(self):
        return self.__liters_of_fuel

    def fill_up(self):
        self.__liters_of_fuel = self.__FULL_TANK_CAPACITY

    def travel_combustion(self, distance: float):
        if self.__liters_of_fuel <= 0.0:
            raise ValueError("El coche no puede andar. Antes llena el deposito.")

        fuel_consumed = self.__LITERS_PER_KM * distance

        if fuel_consumed > self.__liters_of_fuel:
            distance = self.__liters_of_fuel / self.__LITERS_PER_KM
            self.__liters_of_fuel = 0.0
            print(f"Has recorrido {distance:.2f} kilómetros hasta que te quedaste sin gasolina.")
        else:
            self.__liters_of_fuel -= fuel_consumed

        super().travel(distance)
        return f"{distance:.2f} km"
