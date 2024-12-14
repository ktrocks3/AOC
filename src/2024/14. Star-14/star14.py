from collections import defaultdict
import re

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    file = common(filename)

    width, length = map(int, file.pop(0).split(' '))

    def movement(x, y, vx, vy, duration):
        return (x + vx * duration) % width, (y + vy * duration) % length

    def quadrant(x, y):
        middle_horizontal = width // 2
        middle_vertical = length // 2

        # Check if the point is on the middle lines
        if x == middle_horizontal or y == middle_vertical:
            return -1

        # Determine if the point is in the right half and/or bottom half
        right = x > middle_horizontal
        bottom = y > middle_vertical

        # Return quadrant based on the position
        return right + 2 * bottom

    quads = defaultdict(int)
    S = [[0 for _ in range(width)] for _ in range(length)]
    for line in file:
        values = re.match(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)', line)
        values = tuple(map(int, values.groups())) if values else None
        res_x, res_y = movement(*values, 100)
        q = quadrant(res_x, res_y)
        S[res_y][res_x] += 1
        quads[q] += 1
    for r in S:
        s = ""
        for c in r:
            s += str(c) if c > 0 else '.'
    safety = 1
    for v in [quads[x] for x in range(4)]:
        safety *= v
    return safety


def part2(filename):
    file = common(filename)

    width, length = map(int, file.pop(0).split(' '))

    def movement(x, y, vx, vy, duration):
        return (x + vx * duration) % width, (y + vy * duration) % length

    def create_bitmap(fn):
        Image.fromarray(np.array(S, dtype=np.uint8) * 255).save(fn)

    def create_image(fn):
        cell_size = 5  # pixels
        image_width, image_height = width * cell_size, length * cell_size
        font = ImageFont.load_default()
        # Create a blank image with white background
        image = Image.new("RGB", (image_width, image_height), "white")
        draw = ImageDraw.Draw(image)
        # Draw the text without grid lines
        for r, row in enumerate(S):
            for c, value in enumerate(row):
                x, y = c * cell_size, r * cell_size
                # Draw number or dot
                text = str(value) if value > 0 else " "
                bbox = font.getbbox(text)  # Use getbbox to get text dimensions
                text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
                text_x = x + (cell_size - text_width) // 2
                text_y = y + (cell_size - text_height) // 2
                draw.text((text_x, text_y), text, fill="black", font=font)
        image.save(fn)

    def print_grid():
        for r in S:
            s = ""
            for c in r:
                s += '.' if c else ' '
            print(s)

    for i in range(10000):
        print(i)
        S = [[False for _ in range(width)] for _ in range(length)]
        for line in file:
            values = re.match(r'p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)', line)
            values = tuple(map(int, values.groups())) if values else None
            res_x, res_y = movement(*values, i)
            S[res_y][res_x] = True
        # create_image(f"grid_output{i}.png")
        create_bitmap(f"images/grid_output{i}.bmp")


if __name__ == '__main__':
    assert part1('example.txt') == 12, f"Received {part1('example.txt')} for example on part1"
    # assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    # assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    # assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
