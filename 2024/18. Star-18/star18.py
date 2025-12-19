import heapq
from heapq import heappop


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dijkstra(start, end, grid):
    heap = [(0, start, (0, 1))]  # cost, position, direction
    visited = set()

    while heap:
        cost, (i, j), d = heappop(heap)
        if (i, j) == end:
            return cost
        if (i, j, d) in visited:
            continue
        visited.add((i, j, d))

        for dy, dx in dirs:
            ni, nj = i + dy, j + dx
            if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])) or grid[ni][nj]:
                continue
            heapq.heappush(heap, (cost + 1, (ni, nj), (dy, dx)))

    return float('inf')  # If no path is found


def print_grid(grid):
    for r in grid:
        S = ""
        for c in r:
            if c:
                S += '#'
            else:
                S += '.'
        print(S)


def part1(filename):
    stop = 12 if 'input' not in filename else 1024
    size = 7 if 'input' not in filename else 71
    file = common(filename)[:stop]
    grid = [[False for _ in range(size)] for _ in range(size)]
    for line in file:
        x, y = line.split(',')
        x, y = int(x), int(y)
        grid[y][x] = True
    return dijkstra((0, 0), (size - 1, size - 1), grid)


def part2(filename):
    size = 7 if 'input' not in filename else 71
    stop = 12 if 'input' not in filename else 3040
    curr = 0
    file = common(filename)
    grid = [[False for _ in range(size)] for _ in range(size)]
    for line in file[:stop]:
        x, y = line.split(',')
        x, y = int(x), int(y)
        grid[y][x] = True
        curr += 1

    while dijkstra((0, 0), (size - 1, size - 1), grid) < 100000:
        x, y = file[curr].split(',')
        x, y = int(x), int(y)
        grid[y][x] = True
        curr += 1

    return f'{x},{y}'


if __name__ == '__main__':
    assert part1('example.txt') == 22, f"Received {part1('example.txt')} for example on part1"
    # assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "6,1", f"Received {part2('example.txt')} for example on part2"
    # assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
