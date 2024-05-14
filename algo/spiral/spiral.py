import itertools
from examples import n4matrix, n7matrix


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, advance):
        return Point(self.x + advance.x, self.y + advance.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


def generate_directional_advances():
    for advance in {
        'E': Point(0, 1),
        'S': Point(1, 0),
        'W': Point(0, -1),
        'N': Point(-1, 0),
    }.values():
        yield advance


def generate_turning_points(n):
    half_size = n // 2
    for i in range(half_size):
        yield Point(i, n - i - 1)
        yield Point(n - i - 1, n - i -1)
        yield Point(n - i - 1, i)
        yield Point(i + 1, i)
    if n % 2 == 1:
        yield Point(half_size, half_size)


def generate_spiral_points(n):
    turning_points = generate_turning_points(n)
    advances = generate_directional_advances()
    current_position = Point(0, 0)
    yield current_position

    # Everytime we reach a turning point, we need a new one and another direction
    # We'll cycle through advances as they are only 4, because we need them over and over
    for turning_point, advance in zip(turning_points, itertools.cycle(advances)):
        while current_position != turning_point:
            current_position += advance
            yield current_position


def get_spiral_values(matrix):
    return [matrix[p.x][p.y] for p in generate_spiral_points(len(matrix))]


if __name__ == '__main__':
    print(get_spiral_values(n4matrix))
    print(get_spiral_values(n7matrix))
