"""
Test BankAccount module

Author: Jorge Pradillo Hinterberger
Date: 04/03/2024
"""
from bankAccount import BankAccount


def main():
    # PROGRAMA PRINCIPAL:

    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.add_money(2000)
    cuenta2.remove_money(600)
    cuenta3.add_money(75)
    cuenta1.remove_money(55)
    cuenta2.transfer_money(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

    """
    SALIDA ESPERADA:

    Número de cta: 6942541557 Saldo: 0,00 €
    Número de cta: 9319536518 Saldo: 1500,00 €
    Número de cta: 7396941518 Saldo: 6000,00 €
    Número de cta: 6942541557 Saldo: 1945,00 €
    Número de cta: 9319536518 Saldo: 800,00 €
    Número de cta: 7396941518 Saldo: 6175,00 €
    """


if __name__ == "__main__":
    main()
