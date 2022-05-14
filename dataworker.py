import math

from colorama import Fore, Style


def get_method():
    print("Выберите метод инторполяции")
    print("1 - Метод Лагранжа")
    print("2 - Метод Ньютона с конечными  разностями")
    while True:
        try:
            method_choise = input(Fore.GREEN + "    >>>" + Style.RESET_ALL)
            if method_choise != "1" and method_choise != "2":
                raise AttributeError
        except AttributeError:
            print(Fore.RED + "Выберите либо 1, либо 2" + Style.RESET_ALL)
        break
    return method_choise


def get_data():
    print("Задать исходные данные в виде 1 - набора данных, 2 - функции")
    choise = None
    while True:
        try:
            choise = input(Fore.GREEN + "    >>>" + Style.RESET_ALL)
            if choise != "1" and choise != "2":
                raise AttributeError
        except AttributeError:
            print(Fore.RED + "Выберите либо 1, либо 2" + Style.RESET_ALL)
        break
    if choise == "1":
        data = get_data_from_data_set()
        return data
    elif choise == "2":
        data = get_data_from_function()
    return data


def get_data_from_data_set():
    print("Введите X и Y")
    print(Fore.YELLOW + "Для выхода напечатайте" + Fore.RED + " stop" + Style.RESET_ALL)
    arr = []
    while True:
        try:
            dot = input(Fore.GREEN + "   >>>" + Style.RESET_ALL).strip()
            if dot == "stop":
                if len(arr) < 2:
                    raise AttributeError
                break
            parse_dot = tuple(map(float, dot.split()))
            if len(parse_dot) != 2:
                raise ValueError
            arr.append(parse_dot)
        except AttributeError:
            print(Fore.RED + "Введите >=2 координат!" + Style.RESET_ALL)
            return None
        except ValueError:
            print(Fore.RED + "Введите два числа через пробел!" + Style.RESET_ALL)
    return arr


def get_data_from_function():
    print("Выберите функцию:")
    print("1 - sin(x)")
    print("2 - x^2 + 2x + 3")
    print("3 - √x - 4")
    while True:
        try:
            func_id = input(Fore.GREEN + "  >>>" + Style.RESET_ALL)
            func = get_func(func_id)
            if func is None:
                raise AttributeError
            break
        except AttributeError:
            print(Fore.RED + "Выберите функцию из заданного списка!" + Style.RESET_ALL)
            get_data_from_data_set()
    a, b, n = get_scope()
    return get_values_from_the_function(a, b, func, n)


def get_scope():
    print("Введите границы функции:")
    while True:
        try:
            print("Начало: ")
            a = float(input(Fore.GREEN + "  >>>" + Style.RESET_ALL))
            print("Конец: ")
            b = float(input(Fore.GREEN + "  >>>" + Style.RESET_ALL))
            print("Количество узлов: ")
            n = int(input(Fore.GREEN + "  >>>" + Style.RESET_ALL))
            if a > b:
                a, b = b, a
            elif a == b:
                raise ArithmeticError
            break
        except ArithmeticError:
            print(Fore.RED + "Границы интервала должны отличаться!" + Style.RESET_ALL)
    return a, b, n


def get_values_from_the_function(a, b, func, n):
    step = (b - a) / (n - 1)
    dots = []
    for i in range(n):
        dots.append((a, func(a)))
        a += step
    return dots


def get_func(func_id):
    if func_id == "1":
        return lambda x: math.sin(x)
    elif func_id == "2":
        return lambda x: x ** 2 + 2 * x + 3
    elif func_id == "3":
        return lambda x: math.sqrt(x) - 4
    else:
        return None


def get_x():
    print("Введите X:")
    while True:
        try:
            x1 = float(input(Fore.GREEN + "  >>>" + Style.RESET_ALL))
            x2 = float(input(Fore.GREEN + "  >>>" + Style.RESET_ALL))
            break
        except AttributeError:
            print(Fore.RED + "Что-то пошло не так:(" + Style.RESET_ALL)
    return x1, x2
