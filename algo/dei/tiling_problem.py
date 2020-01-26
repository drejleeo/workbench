import random

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'P({self.x}, {self.y})'

n = 3
dim = 2 ** n


def generate_subsquare_designed_by_2_points(board, A, B):
    for i in range(A.x, B.x):
        for j in range(A.y, B.y):
            yield board[i][j]


def get_marked_quarter(board, quarters):
    for k, v in quarters:
        for element in generate_subsquare_designed_by_2_points(
            board, v.get('point1'), v.get('point2')
        ):
            if element != 0:
                return k


def place_tile(board, already_marked, tile_number, half, size):
    spots = {
        'wn': (half - 1, half - 1),
        'ne': (half - 1, size - half),
        'es': (size - half, half - 1),
        'sw': (half, half),
    }
    not_marked_quarts = list(spots.keys() - {already_marked})
    for key in not_marked_quarts:
        x, y = spots[key]
        board[x][y] = tile_number


def solve_tiling(board, size, tile_number=1):
    """
    Calculate quarters by starting and ending points:

    matrix = [
        A, -, -, -, C, -, -, -,
        -, -, -, -, -, -, -, -,
        -, -, -, -, -, -, -, -,
        -, -, -, B, -, -, -, D,
        E, -, -, -, G, -, -, -,
        -, -, -, -, -, -, -, -,
        -, -, -, -, -, -, -, -,
        -, -, -, F, -, -, -, H,
    ]

    Quarters are being iterated by iteration over the
    subsquares designed by the pairs of points
    (A, B), (C, D), (E, F), (G, H)

    :param board: The board to place tiles on.
    :param size: n size of the n*n board.
    :param tile_number: The starting number for tile count.
    :return:
    """
    print('\niteration')
    pmatrix(board)
    print('end\n')

    if size > 2:
        half = size // 2

        # Quarters defined by 2 points: top-left, bottom-right
        quarters = {
            'wn': {
                'point1': Point(0, 0),
                'point2': Point(half - 1, half - 1),
            },
            'ne': {
                'point1': Point(0, half),
                'point2': Point(half - 1, size - 1)
            },
            'es': {
                'point1': Point(half, 0),
                'point2': Point(size - 1, half - 1)
            },
            'sw': {
                'point1': Point(half, half),
                'point2': Point(size - 1, size - 1),
            }
        }
        mark = get_marked_quarter(board, )
        place_tile(board, mark, tile_number, half, size)

        for q in quarters.items():
            solve_tiling(board, half, tile_number + 1)


def pmatrix(mat):
    for row in mat:
        print(row)


if __name__ == '__main__':
    board = [[0] * dim for _ in range(dim)]
    board[random.randint(0, dim - 1)][random.randint(0, dim - 1)] = 1

    solve_tiling(
        board=board,
        size=dim,
    )

    print('Result is as follows: ')
    pmatrix(board)
