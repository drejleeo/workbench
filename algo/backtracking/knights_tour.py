"""The knight is placed on the first block of an empty BoardSetup and, moving
according to the rules of chess, must visit each square exactly once. """
from collections import namedtuple
from copy import deepcopy

# Directions ordered clockwise - Edit: not anymo'
Point = namedtuple('Point', ['x', 'y'])
KNIGHT_MOVES = {
    'sse': Point(2, 1),
    'ese': Point(1, 2),
    'ene': Point(-1, 2),
    'nne': Point(-2, 1),
    'nnw': Point(-2, -1),
    'wnw': Point(-1, -2),
    'wsw': Point(1, -2),
    'ssw': Point(2, -1),
}
class BoardSetup(object):
    WIDTH = 4
    HEIGHT = 5
    START = Point(0, 0)


def is_valid(position, visited, BoardSetup):
    return BoardSetup.WIDTH > position.y >= 0 <= position.x < BoardSetup.HEIGHT


def output_matrix(matrix):
    for row in matrix:
        print(row)
    print()


def start_knights_tour(current_pos, step_count, visited):

    visited[current_pos.x][current_pos.y] = step_count

    if step_count == BoardSetup.WIDTH * BoardSetup.HEIGHT:
        yield deepcopy(visited)

    # output_matrix(visited)

    for move in KNIGHT_MOVES.values():
        next_step = Point(current_pos.x + move.x, current_pos.y + move.y)

        if is_valid(next_step, visited, BoardSetup) and not visited[next_step.x][next_step.y]:
            yield from start_knights_tour(next_step, step_count + 1, visited)
    visited[current_pos.x][current_pos.y] = 0


if __name__ == '__main__':
    sols = list(start_knights_tour(
        current_pos=BoardSetup.START,
        step_count=1,
        visited=[[0] * BoardSetup.WIDTH for _ in range(BoardSetup.HEIGHT)],
    ))

    for sol in sols:
        output_matrix(sol)
    print(f'Found {len(sols)} solutions.')