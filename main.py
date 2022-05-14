import numpy as np
from colorama import Fore, Style

import graphic
from solver import lagrangepolynomial, newtonpolynomial
import dataworker

if __name__ == '__main__':
    print(Fore.GREEN + "Лабораторная работа №5" + Style.RESET_ALL)
    print("Интерполяция функции")
    data = {"method": dataworker.get_method(), "data": dataworker.get_data(), "x": dataworker.get_x()}
    x = np.array([dot[0] for dot in data["data"]], dtype=object)
    y = np.array([dot[1] for dot in data["data"]], dtype=object)

    plot_x = np.linspace(np.min(x), np.max(x), 100)
    plot_y = None

    answer1 = answer2 = 0
    if data["method"] == "1":
        answer1 = lagrangepolynomial.solve(data["data"], data["x"][0])
        answer2 = lagrangepolynomial.solve(data["data"], data["x"][1])
        plot_y = [lagrangepolynomial.solve(data["data"], x) for x in plot_x]
    elif data["method"] == "2":
        answer1 = newtonpolynomial.solve(data["data"], data["x"][0])
        answer2 = newtonpolynomial.solve(data["data"], data["x"][1])
        plot_y = [lagrangepolynomial.solve(data["data"], x) for x in plot_x]
    else:
        answer1 = None
        answer2 = None

    if answer1 and answer2 is not None:
        graphic.plot(x, y, plot_x, plot_y)
    print(answer1)
    print(answer2)
