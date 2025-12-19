def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    grid = []
    head = []
    for i, row in enumerate(common(filename)):
        grid.append([])
        for j, col in enumerate(row):
            grid[-1].append(int(col))
            if col == '0':
                head.append((i, j))

    def traverse(start, height):
        movements = [(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0], start[1] - 1),
                     (start[0], start[1] + 1)]
        movements = [(dx, dy) for dx, dy in movements if
                     0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == height + 1]
        movements = set(movements)
        if len(movements) == 0:
            return set()
        if height == 8:
            return movements
        total = set()
        for move in movements:
            total = total.union(traverse(move, height + 1))
        return total

    result = 0
    for trail in head:
        result += len(traverse(trail, 0))

    return result


def part2(filename):
    grid = []
    head = []
    for i, row in enumerate(common(filename)):
        grid.append([])
        for j, col in enumerate(row):
            if col == '.':
                col = '-1'
            grid[-1].append(int(col))
            if col == '0':
                head.append((i, j))

    def traverse(start, height):
        movements = [(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0], start[1] - 1),
                     (start[0], start[1] + 1)]
        movements = [(dx, dy) for dx, dy in movements if
                     0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == height + 1]
        if len(movements) == 0:
            return []
        if height == 8:
            return movements
        total = []
        for move in movements:
            total += traverse(move, height + 1)
        return total

    result = 0
    for trail in head:
        result += len(traverse(trail, 0))

    return result


if __name__ == '__main__':
    assert part1('example.txt') == 1, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 36, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example3.txt') == 3, f"Received {part2('example3.txt')} for example3 on part2"
    assert part2('example4.txt') == 13, f"Received {part2('example4.txt')} for example4 on part2"
    assert part2('example5.txt') == 227, f"Received {part2('example5.txt')} for example5 on part2"
    assert part2('example2.txt') == 81, f"Received {part1('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
