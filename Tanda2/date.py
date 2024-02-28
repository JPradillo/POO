"""
Muestra un menú con las siguientes opciones:

- Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa.
    * Si no se introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
- Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
    * Si el número es negativo restará los días.
    * Esta opción solo podrá realizarse si hay una fecha introducida (se ha ejecutado la opción anterior)
    * Si no la hay mostrará un mensaje de error.
- Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
- Añadir años a la fecha. El mismo procedimiento que la opción 2.
- Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
    * La comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior
    a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
- Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
- Terminar.

- Consideraciones a tener en cuenta:
    * Clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger alguna opción.
    * Las fechas las manejaremos con la clase datetime.date.

Author: Jorge Pradillo Hinterberger
Date: 12/02/2024
"""
import locale
from menu import Menu
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

date_1 = 0


def main():
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')   # Pone los nombres de los días, meses y años en español.
    menu = Menu("Introducir una fecha en formato dd/mm/aaaa", "Añadir días a la fecha", "Añadir meses a la fecha",
                "Añadir años a la fecha", "Comparar con otra fecha",
                "Mostrar en formato largo (Por ej: lunes, 1 de febrero de 2021)", "Terminar", title="Menú de fechas")

    while True:
        choice = menu.show()
        if choice != 1 and date_1 is None and choice != menu.len:
            print("Debes introducir la fecha primero.")
        else:
            match choice:
                case 1: input_date()
                case 2: add_days()
                case 3: add_months()
                case 4: add_years()
                case 5: compare_dates()
                case 6: long_mode()
                case 7: break


def input_date():
    global date_1
    date_1_str = input("Introduce la fecha en formato dd/mm/aaaa: \n")
    date_1 = datetime.strptime(date_1_str, "%d/%m/%Y").date()


def add_days():
    global date_1
    days = int(input("Introduce la cantidad de días que quieras añadir.\n"))
    date_1 += timedelta(days=days)    # Fechas hasta semanas


def add_months():
    global date_1
    months = int(input("Introduce la cantidad de meses que quieras añadir.\n"))
    date_1 += relativedelta(months=months)


def add_years():
    global date_1
    years = int(input("Introduce la cantidad de años que quieras añadir.\n"))
    date_1 += relativedelta(years=years)


def compare_dates():
    global date_1
    date_2_str = input("Introduce la fecha con la que la quieras comparar.")
    date_2 = datetime.strptime(date_2_str, "%d/%m/%Y").date()

    if date_2 > date_1:
        print("Esta fecha es mayor que la que había introducida.")
    elif date_2 == date_1:
        print("Esta fecha y la que había introducida son iguales.")
    else:
        print("Esta fecha es menor que la que había introducida.")


def long_mode():
    global date_1
    print(date_1.strftime("%A, %d de %B de %Y"))


if __name__ == "__main__":
    main()
