from copy import deepcopy


class Queen(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_safe(self, board):
        for i in range(self.x):
            if board[i][self.y] == 1:
                return False
        for i, j in zip(range(self.x, -1, -1), range(self.y, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(self.x, -1, -1), range(self.y, DIMENSION, 1)):
            if board[i][j] == 1:
                return False
        return True


DIMENSION = 5


def output_matrix(sol, *args):
    print(*args)
    for row in sol:
        print(row)
    print()


def solve_nqueen(board, queens_count=0):

    if queens_count == DIMENSION:
        yield deepcopy(board)
        queens_count -= 1

    for col in range(DIMENSION):
        new_queen = Queen(queens_count, col)
        if new_queen.is_safe(board):
            board[new_queen.x][new_queen.y] = 1
            yield from solve_nqueen(board, queens_count + 1)
        board[new_queen.x][new_queen.y] = 0


if __name__ == '__main__':
    sols = list(solve_nqueen(board=[[0] * DIMENSION for row in range(DIMENSION)]))

    for sol in sols:
        output_matrix(sol)
    print(f'Found {len(sols)} solutions')
