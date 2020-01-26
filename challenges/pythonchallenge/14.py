from PIL import Image

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coordinates_tuple(self):
        return (self.x, self.y)

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __str__(self):
        return f'Point({self.x}, {self.y})'

directions = {
    0: Point(0, 1),
    1: Point(1, 0),
    2: Point(0, -1),
    3: Point(-1, 0),
}

def get_direction(index):
    return directions.get(index % 4)

if __name__ == '__main__':

    canvas = Image.new('RGB', (100, 100))
    img = Image.open('inputs/wire.png', 'r')
    d = 200

    subject = Point(0, 0)
    subject -= get_direction(d)

    image_cursor = 0

    while d // 2 > 0:
        nr_of_steps = d // 2
        for i in range(nr_of_steps):
            subject = subject + get_direction(d)
            pixel = img.getpixel((image_cursor, 0))
            image_cursor += 1
            canvas.putpixel(subject.coordinates_tuple, pixel)
        d -= 1

    canvas.show()
