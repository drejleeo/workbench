from utils import print_matrix
import numpy as np
import random
n = 3
dim = 2 ** n

tile_placing = {
    
}


def can_be_placed(board, tile):
    pass


def get_marked_quarter(quarters):
    for key in quarters.keys():
        if sum(sum(row) for row in quarters[key]) == 1:
            return key


def place_tile(already_marked, tile_number, board, half):
    spots = {
        'wn': board[half-1][half-1],
        'ne': board[half-1][ half ],
        'es': board[ half ][half-1],
        'sw': board[ half ][ half ],
    }
    for key in spots.keys() - already_marked:
        spots[key] = tile_number


def solve_tiling(board, size, tile_number=1):

    if size == 2:
        return board

    half = size // 2
    quarters = {
        'wn': [row[0:half] for row in board[0:half]],
        'ne': [row[half:size] for row in board[0:half]],
        'es': [row[0:half] for row in board[half:size]],
        'sw': [row[half:size] for row in board[half:size]],
    }

    mark = get_marked_quarter(quarters)
    place_tile(
        already_marked=mark,
        tile_number=tile_number,
        board=board,
        half=half,
    )

    for quart in quarters:
        solve_tiling(quart, half, tile_number + 1)




if __name__ == '__main__':
    board = [[0] * dim for _ in range(dim)]
    board[random.randint(0, dim - 1)][random.randint(0, dim - 1)] = 1
    result = solve_tiling(
        board=board,
        size=dim,
    )

    print_matrix(board)
