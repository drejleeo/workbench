from PIL import Image, ImageChops

sequence = [
    (
        int(p[0:2], 16),
        int(p[2:4], 16),
        int(p[4:6], 16)
    ) for p in ['f9f9f9'] + 5 * ['b87cf3'] + ['f9f9f9']
]
img = Image.open('inputs/mozart.gif', 'r')
w, h = img.size

canvas = Image.new('RGB', (1000, 1000))
x, y = 0, 0

in_every_row = [x for x in img.histogram() if x % h == 0 and x != 0]
occurrences = in_every_row[0]
tone = img.histogram().index(occurrences)

for y in range(img.size[1]):
    box = 0, y, img.size[0], y + 1
    row = img.crop(box)
    bytes = row.tobytes()
    i = bytes.index(195)
    row = ImageChops.offset(row, -i)
    img.paste(row, box)

img.save("level16-result.gif")
