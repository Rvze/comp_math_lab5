def solve(dots, x):
    n = len(dots)
    answer = 0
    for i in range(n):
        numerator = denominator = 1
        for j in range(n):
            if j != i:
                numerator *= x - dots[j][0]
                denominator *= dots[i][0] - dots[j][0]
        answer += dots[i][1] * numerator / denominator
    return answer
