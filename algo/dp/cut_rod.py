prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30,]


def cut_rod_recursive(p, n):
    """
    Recursive method - calculates inefficiently best profit.
    :param p: list of the prices per rod size (the index list)
    :param n: initial rod size
    :return: Best profit
    """
    if n == 0:
        return 0
    q = 0
    for j in range(1, n + 1):
        q = max(q, p[j] + cut_rod_recursive(p, n - j))
    return q


def cut_rod_top_down(p, n, r):
    """
    Recursive method - calculates from top \ bottom with optimal nr of calcs.
    :param r: list of memoized values
    """
    if r[n] > 0:
        return r[n]
    q = 0
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod_top_down(p, n - i, r))
    r[n] = q
    return r[n]


def cut_rod_bottom_up(p, n, r):
    """
    Iterative method - it memoizes the value for the previous calculations.
    :param r: list of memoized values
    """
    for j in range(1, n + 1):
        q = 0
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up(p, n):
    """
    Iterative method - same as cut_rod_bottom_up but it keeps the choices made
    to get the optimal value.
    """
    r, s = [0] * (n + 1), [0] * (n + 1)
    for j in range(1, n + 1):
        q = r[j - 1]
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r[n], s[1:]


if __name__ == '__main__':

    n = 5
    results = {
        'recursive': cut_rod_recursive(prices, n),
        'top-down': cut_rod_top_down(prices, n, r=[0] * (n + 1)),
        'bottom-up': cut_rod_bottom_up(prices, n, r=[0] * (n + 1)),
        'extend-bu': extended_bottom_up(prices, n),
    }

    for method, value in results.items():
        print(f'Use method {method}: {value}')
