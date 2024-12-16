import heapq
from heapq import heappop


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: list(x.strip()), f.readlines()))
    return lines


def part1(filename):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    grid = common(filename)
    seen = set()
    memo = {}

    def dijkstra(start, end):
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
                if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])) or grid[ni][nj] == '#':
                    continue
                turn_cost = 1001 if (dy, dx) != d else 1
                heapq.heappush(heap, (cost + turn_cost, (ni, nj), (dy, dx)))

        return float('inf')  # If no path is found

    s = (0, 0)
    e = (0, 0)
    for ri, r in enumerate(grid):
        for ci, c in enumerate(r):
            if c == 'S':
                s = (ri, ci)
            if c == 'E':
                e = (ri, ci)
    return dijkstra(s, e)


def part2(filename):
    return


if __name__ == '__main__':
    assert part1('example.txt') == 7036, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 11048, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
