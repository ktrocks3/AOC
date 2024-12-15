def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    def print_grid():
        for r in grid:
            S = ""
            for c in r:
                if c == '@':
                    S += "\033[31m@\033[0m"  # Red color for '@'
                else:
                    S += c
            print(S)

    def GPS(GPSx, GPSy):
        return GPSx + (GPSy * 100)

    file = common(filename)
    b = True
    grid = []
    movement = []
    x, y = 0, 0
    for i, line in enumerate(file):
        if line == '':
            b = False
        elif b:
            grid.append(list(line))
            if '@' in line:
                x, y = line.index('@'), i
        else:
            movement.extend(list(line))
    for m in movement:
        if m == '<':
            dy, dx = y, x - 1
        elif m == '>':
            dy, dx = y, x + 1
        elif m == '^':
            dy, dx = y - 1, x
        elif m == 'v':
            dy, dx = y + 1, x
        else:
            print(m, "BAD")
            continue

        if grid[dy][dx] == '#':
            continue
        elif grid[dy][dx] == '.':
            grid[dy][dx], grid[y][x] = grid[y][x], grid[dy][dx]
            y, x = dy, dx
        elif grid[dy][dx] == 'O':
            np = (dy + (dy - y), dx + (dx - x))
            while grid[np[0]][np[1]] == 'O':
                np = (np[0] + (dy - y), np[1] + (dx - x))
            if grid[np[0]][np[1]] == '.':
                grid[np[0]][np[1]], grid[dy][dx] = grid[dy][dx], grid[np[0]][np[1]]
                grid[dy][dx], grid[y][x] = grid[y][x], grid[dy][dx]
                y, x = dy, dx
            elif grid[np[0]][np[1]] == '#':
                continue
    return sum(GPS(i,j) for i in range(len(grid[0])) for j in range(len(grid)) if grid[j][i] == 'O')


def part2(filename):
    return


if __name__ == '__main__':
    assert part1('example.txt') == 2028, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 10092, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
