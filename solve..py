def solve(n, repeats):
    res = 0
    for i in range(1, repeats + 1):
        res += int(str(n) * i)

    return res
