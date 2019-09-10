import random
DIMENSION = 4


def solve_tiling():
    return


if '__name__' == '__main__':
    import ipdb; ipdb.set_trace()
    board = [[0] * 2 ** DIMENSION for _ in range(2 ** DIMENSION)]
    board[random.randint(0, 2 ** DIMENSION - 1)][random.randint(0, 2 ** DIMENSION - 1)] = 1
    result = solve_tiling()
    print(board)
