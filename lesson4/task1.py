from sys import argv


def salary():
    try:
        time, stavka, prem = map(int, argv[1:])
        print(f"Зарплата - {time * stavka + prem}")
    except ValueError:
        print("Введи все 3 значения.")


salary()
