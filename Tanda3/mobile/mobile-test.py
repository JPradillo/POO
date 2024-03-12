"""
Test subclase Mobile
Author: Jorge Pradillo Hinterberger
Date: 03/03/2024
"""
from mobile import Mobile


def main():
    # PROGRAMA PRINCIPAL:

    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")
    print(m1)
    print(m2)
    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)
    print(m1)
    print(m2)
    print(m3)

    """
    SALIDA ESPERADA:
    
    Nº 678 11 22 33 - 0s de conversación - tarificados 0,00 euros
    Nº 644 74 44 69 - 0s de conversación - tarificados 0,00 euros
    Nº 678 11 22 33 - 520s de conversación - tarificados 0,52 euros
    Nº 644 74 44 69 - 870s de conversación - tarificados 1,10 euros
    Nº 622 32 89 09 - 750s de conversación - tarificados 0,00 euros
    """


if __name__ == "__main__":
    main()
