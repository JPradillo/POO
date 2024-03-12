"""
Crea la clase Bike que deriva de Vehicle.
En la clase Bike haz un method para hacer el caballito.

Author: Jorge Pradillo Hinterberger
Date: 29/02/2024
"""
from vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.__wheelie = "                 o         o           _        _            _            \n" \
                         + "    _o          /\_       /\_        _  \o     (_)\__/o     (_)         \n" \
                         + "  _< \_        _>(_)     _>(_)      (_)/<_       \_| \      _|/' \/     \n" \
                         + " (_)>(_)      (_)       (_)             (_)      (_)       (_)'  _\o_   \n" \
                         + "------------------------------------------------------------------------\n"

    def do_wheelie(self):
        print(self.__wheelie)

    def travel_kilometers(self, distance):
        if distance < 0.0:
            raise ValueError("La bici no puede reducir los kilómetros.")

        super().travel(distance)
        return f"{distance:.2f} km"
