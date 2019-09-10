"""
We have discussed Backtracking and Knight’s tour problem in Set 1. Let us discuss Rat in a Maze as another
 example problem that can be solved using Backtracking.

A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0, 0][0, 0]
 and destination block is lower rightmost block i.e., maze[N-0, 0][N-0, 0]. A rat starts from source and has to reach
 the destination. The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to
 destination. Note that this is a simple version of the typical Maze problem. For example, a more complex version
  can be that the rat can move in 4 directions and a more complex version can be with a limited number of moves.

    Maze:

    1, 0, 0, 0              1, 0, 0, 0
    1, 1, 0, 1      --->    2, 3, 0, 0
    0, 1, 0, 0              0, 4, 0, 0
    1, 1, 1, 1              0, 5, 6, 7

"""
from collections import namedtuple
import pandas
from copy import deepcopy

# Setup
Point = namedtuple('Point', ['x', 'y'])
RAT_MOVES = {
    'n': Point(-1, 0),
    'e': Point(0, 1),
    's': Point(1, 0),
    'w': Point(0, -1),
}
class Maze(object):
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1],
    ]

    WIDTH = 5
    HEIGHT = 5

    START = Point(0, 0)
    END = Point(WIDTH - 1, HEIGHT - 1)


def output_matrix(sol):
    for row in sol:
        print(row)
    print()


def can_move_to(position, trace):
    return Maze.WIDTH > position.x >= 0 <= position.y < Maze.HEIGHT and \
           Maze.matrix[position.x][position.y] == 1 and \
           trace[position.x][position.y] == 0


def solve_rat_in_maze(current_pos, trace, step_count=1):

    trace[current_pos.x][current_pos.y] = step_count

    if current_pos == Maze.END:
        yield deepcopy(trace)

    for move in RAT_MOVES.values():
        next_pos = Point(current_pos.x + move.x, current_pos.y + move.y)
        if can_move_to(next_pos, trace):
            yield from solve_rat_in_maze(next_pos, trace, step_count + 1)
    trace[current_pos.x][current_pos.y] = 0


if __name__ == '__main__':

    sols = []

    sols = list(solve_rat_in_maze(
        current_pos=Maze.START,
        step_count=1,
        trace=[[0] * Maze.WIDTH for _ in range(Maze.HEIGHT)],
    ))

    for sol in sols:
        output_matrix(sol)
    print(f'Found {len(sols)} solutions.')
