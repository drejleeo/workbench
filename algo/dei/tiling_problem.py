from utils import print_matrix
import numpy as np
import random
n = 3
dim = 2 ** n

tile_placing = {
    
}


def can_be_placed(board, tile):
    pass


def get_markerd_quarter(quarters):
    for key in quarters.keys():
        if sum(sum(row) for row in quarters[key]) == 1:
            return key


def solve_tiling(board):
    lng = dim
    mid = lng // 2

    quarters = {
        'wn': [row[0:mid] for row in board[0:mid]],
        'ne': [row[mid:lng] for row in board[0:mid]],
        'es': [row[0:mid] for row in board[mid:lng]],
        'sw': [row[mid:lng] for row in board[mid:lng]],
    }

    mark = get_markerd_quarter(quarters)


    for quart in quarters:
        solve_tiling(quart)


if __name__ == '__main__':
    board = [[0] * dim for _ in range(dim)]
    board[random.randint(0, dim - 1)][random.randint(0, dim - 1)] = 1
    result = solve_tiling(board)
    print()
    print_matrix(board)
