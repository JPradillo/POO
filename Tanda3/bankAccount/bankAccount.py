"""
Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos.
El número de cuenta se genera de forma aleatoria cuando se crea una cuenta nueva
No puede haber dos objetos con el mismo número de cuenta.

La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente.
En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra.
No se permite el saldo negativo.

Author: Jorge Pradillo Hinterberger
Date: 04/04/2023
"""
from __future__ import annotations
from typeguard import typechecked
import random

MIN_NUMBER_OF_ACCOUNT = 1
MAX_NUMBER_OF_ACCOUNT = 9999999999


@typechecked
class BankAccount:
    __account_number = []

    def __init__(self, money: float = 0.0):
        if money < 0:
            raise ValueError("No puedes crear una cuenta con el dinero en negativo.")
        self.__money = money
        self.__number_account = BankAccount.__new_account

    def __new_account(self):
        while True:
            number = random.randint(MIN_NUMBER_OF_ACCOUNT, MAX_NUMBER_OF_ACCOUNT)
            if number not in self.__account_number:
                self.__account_number.append(number)
                break
        # Si no devolvemos el número, imprime None y a la hora de crear el str no muestra el núm. de cuenta
        return number

    @property
    def money(self):
        return self.__money

    @property
    def number_account(self):
        return self.__number_account

    def add_money(self, number: float):
        if number < 0:
            raise ValueError("No puedes ingresar un valor negativo.")
        self.__money += number

    def remove_money(self, number: float):
        self.__check_remove_money(number)
        self.__money -= number

    def __check_remove_money(self, number):
        if number < 0:
            raise ValueError("No puedes retirar un valor negativo.")
        if number > self.__money:
            raise ValueError("No puedes retirar tanto dinero. No eres Cristiano Ronaldo.")

    def transfer_money(self, other: BankAccount, number):
        self.__check_transfer(number, other)
        self.__money -= number
        other.add_money(number)

    def __check_transfer(self, number, other):
        if self.__number_account == other.__number_account:
            raise ValueError("El número de cuenta a transferir no es válido.")
        if number < 0 or number > self.__money:
            raise ValueError("El valor introducido no es válido. Consulte con su entidad.")

    def __str__(self):
        # Número de cta: 6942541557 Saldo: 0,00 €
        return f"Número de cta: {self.__number_account} Saldo: {self.__money:.2f} €"
