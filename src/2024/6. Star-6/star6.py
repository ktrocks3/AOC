import time


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    grid = []
    start = (0, 0)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction = directions[0]
    x, y = -1, -1
    # Up, Right, Down, Left is the order

    for line in common(filename):
        row = []
        for j, item in enumerate(line):
            if item == '^':
                row.append(1)
                y, x = (len(grid), j)
            elif item == '.':
                row.append(0)
            elif item == '#':
                row.append(-1)
            else:
                print("Bad found at", len(grid), j, item)
        grid.append(row)
    count = 1
    while True:
        dx, dy = x + direction[0], y + direction[1]
        if dx < 0 or dx >= len(grid[0]) or dy < 0 or dy >= len(grid):
            break
        if grid[dy][dx] == -1:
            direction = directions[(directions.index(direction) + 1) % len(directions)]
            continue
        x, y = dx, dy
        if grid[y][x] == 0:
            grid[y][x] = 1
            count += 1
    return count


def part2(filename):
    pass


if __name__ == '__main__':
    assert part1('example.txt') == 41, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
