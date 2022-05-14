import math


def solve(dots, x):
    n = len(dots)
    h = dots[1][0] - dots[0][0]
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][0] = dots[i][1]

    for i in range(1, n):
        for j in range(n - i):
            a[j][i] = a[j + 1][i - 1] - a[j][i - 1]

    if x <= dots[n // 2][0]:
        # Первая интерполяционная формула Ньютона
        x0 = n - 1
        for i in range(n):
            if x <= dots[i][0]:
                x0 = i - 1
                break
        if x0 < 0:
            x0 = 0
        t = (x - dots[x0][0]) / h

        result = a[x0][0]
        for i in range(1, n):
            result += (t_calc(t, i) * a[x0][i]) / math.factorial(i)
    else:
        # Вторая интерполяционная формула Ньютона
        t = (x - dots[n - 1][0]) / h

        result = a[n - 1][0]
        for i in range(1, n):
            result += (t_calc(t, i, False) * a[n - i - 1][i]) / math.factorial(i)

    return result


def t_calc(t, n, forward=True):
    result = t

    for i in range(1, n):
        if forward:
            result *= t - i
        else:
            result *= t + i

    return result
