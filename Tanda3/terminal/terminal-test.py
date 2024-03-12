"""
Test clase Terminal.

Author: Jorge Pradillo Hinterberger
Date: 03/03/2024
"""
from terminal import Terminal


def main():
    # Programa principal:
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)

    """
    SALIDAS ESPERADAS:
    -------------------------------------
    No 678 11 22 33 - 0s de conversación
    No 644 74 44 69 - 0s de conversación
    No 678 11 22 33 - 520s de conversación
    No 644 74 44 69 - 320s de conversación
    No 622 32 89 09 - 200s de conversación
    No 664 73 98 18 - 0s de conversación
    """


if __name__ == "__main__":
    main()
