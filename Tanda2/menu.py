"""
Clase menu por defecto

Author: Jorge Pradillo Hinterberger
Date: 12/02/2024
"""
from typeguard import typechecked


@typechecked
class Menu:
    def __init__(self, *options: str, title: str = "Opciones"):
        self.__title = title
        self.__options = list(options)

    @property
    def len(self):
        return len(self.__options)

    def show(self):
        self.__print_menu()
        return self.__select_option()

    def add_option(self, option):
        self.__options.append(option)

    def __print_menu(self):
        print()
        print(self.__title)
        print("=" * len(self.__title))
        for n in range(len(self.__options)):
            print(f"{n + 1}.- {self.__options[n]}")

    def __select_option(self):
        while True:
            try:
                option = int(input("\nIntroduce una opción: \n"))
                if 1 <= option <= len(self.__options):
                    return option
                print(f"Debes introducir un valor entre 1 y {len(self.__options)}.")
            except TypeError:
                print("El valor introducido no es válido.")
