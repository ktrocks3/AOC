import time


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    grid = []
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
    grid = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    start = ()
    # Up, Right, Down, Left is the order

    for line in common(filename):
        row = []
        for j, item in enumerate(line):
            if item == '^':
                start = (j, len(grid))
                row.append(1)
            elif item == '.':
                row.append(0)
            elif item == '#':
                row.append(-1)
            else:
                print("Bad found at", len(grid), j, item)
        grid.append(row)

    def simulate(s, o):
        x, y = s
        g = [r[:] for r in grid]  # Deep copy of a 2D grid
        g[o[1]][o[0]] = -1
        d = directions[0]
        while True:
            dx, dy = x + d[0], y + d[1]
            if dx < 0 or dx >= len(g[0]) or dy < 0 or dy >= len(g):
                return False
            if g[dy][dx] == -1:
                d = directions[(directions.index(d) + 1) % len(directions)]
                continue
            x, y = dx, dy
            if g[y][x] > 0 and g[y][x] & (1 << directions.index(d)):
                return True
            g[y][x] |= 1 << directions.index(d)
        return True

    count = 0
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if (j, i) == start:
                continue

            if simulate(start, (i, j)):
                count += 1

    return count


if __name__ == '__main__':
    assert part1('example.txt') == 41, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 6, f"Received {part2('example.txt')} for example on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
