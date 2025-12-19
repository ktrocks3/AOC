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
    return sum(GPS(i, j) for i in range(len(grid[0])) for j in range(len(grid)) if grid[j][i] == 'O')


def part2(filename, skiprp=False):
    def print_grid():
        for r in grid:
            S = ""
            for c in r:
                if c == '@':
                    S += "\033[31m@\033[0m"  # Red color for '@'
                else:
                    S += c
            print(S, len(S))

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
            if not skiprp:
                line = line.replace('.', '..')
                line = line.replace('O', '[]')
                line = line.replace('@', '@.')
                line = line.replace('#', '##')
            grid.append(list(line))
            if '@' in line:
                x, y = line.index('@'), i
        else:
            movement.extend(list(line))

    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    moves = "<>^v"
    for m in movement:
        dy, dx = dirs[moves.index(m)]

        if grid[y + dy][x + dx] == '#':
            continue
        elif grid[y + dy][x + dx] == '.':
            grid[y + dy][x + dx], grid[y][x] = grid[y][x], grid[y + dy][x + dx]
            y += dy
            x += dx
        elif grid[y + dy][x + dx] in ['[', ']']:
            left_br = (y + dy, x + dx) if grid[y + dy][x + dx] == '[' else (y + dy, x + dx - 1)
            right_br = (left_br[0], left_br[1] + 1)
            # Are we moving horizontally or vertically
            if dy == 0:  # Horizontally, easy
                # Just keep moving in this direction until we find a . or a #:
                i = 2
                while grid[y][x + dx * i] in ['[', ']']:
                    i += 1

                if grid[y][x + dx * i] == '#':
                    continue
                for j in range(x + dx * i, x, -dx):
                    grid[y][j] = grid[y][j - dx]
                grid[y][x] = '.'
                y, x = y, x + dx
            else:
                to_move = [left_br, right_br]
                all_moves = set()
                detected_wall = False
                while to_move:
                    if detected_wall:
                        break
                    all_moves = all_moves.union(to_move)
                    to_move = [(my+dy, mx) for my, mx in to_move if grid[my+dy][mx] != '.']
                    if any(grid[my][mx] == "#" for my, mx in to_move):
                        detected_wall = True
                        continue
                    n_move = set(to_move[::])
                    for l, r in to_move:
                        if grid[l][r] == '[':
                            n_move.add((l, r + 1))
                        elif grid[l][r] == ']':
                            n_move.add((l, r - 1))
                    to_move = list(n_move)
                if detected_wall:
                    continue
                all_moves = sorted(all_moves, reverse=dy > 0)
                for ay, ax in all_moves:
                    grid[ay+dy][ax] = grid[ay][ax]
                    grid[ay][ax] = '.'
                grid[y][x], grid[y+dy][x] = grid[y+dy][x], grid[y][x]
                x, y = x, y+dy

    return sum(GPS(i, j) for i in range(len(grid[0])) for j in range(len(grid)) if grid[j][i] == '[')


if __name__ == '__main__':
    assert part1('example.txt') == 2028, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 10092, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example3.txt') == 618, f"Received {part2('example3.txt')} for example on part2"
    assert part2('example2.txt') == 9021, f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
