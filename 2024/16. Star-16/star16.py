import heapq
from heapq import heappop


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: list(x.strip()), f.readlines()))
    return lines


def part1(filename):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    grid = common(filename)

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


global best_cost
global best_path


def part2(filename):
    import heapq

    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Direction vectors
    grid = common(filename)  # Read and parse the grid

    def dijkstra_all_paths(start, end):
        heap = [(0, start, (0, 1), [start])]  # cost, position, direction, path
        visited = {}
        min_cost = float('inf')
        result_paths = []

        while heap:
            cost, (i, j), d, path = heapq.heappop(heap)

            # If we find a path to the end
            if (i, j) == end:
                if cost < min_cost:
                    min_cost = cost
                    result_paths = [path]
                elif cost == min_cost:
                    result_paths.append(path)
                continue

            # Skip visited states with a better cost
            if (i, j, d) in visited and visited[(i, j, d)] < cost:
                continue
            visited[(i, j, d)] = cost

            # Explore neighbors
            for dy, dx in dirs:
                ni, nj = i + dy, j + dx
                if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])) or grid[ni][nj] == '#':
                    continue
                turn_cost = 1001 if (dy, dx) != d else 1
                new_cost = cost + turn_cost
                new_path = path + [(ni, nj)]
                heapq.heappush(heap, (new_cost, (ni, nj), (dy, dx), new_path))

        return result_paths
    # Find start (S) and end (E) positions
    s, e = None, None
    for ri, row in enumerate(grid):
        for ci, cell in enumerate(row):
            if cell == 'S':
                s = (ri, ci)
            elif cell == 'E':
                e = (ri, ci)

    # Run Dijkstra to find all best paths
    paths = dijkstra_all_paths(s, e)
    tiles = set()
    for p in paths:
        tiles = tiles.union(set(p))

    return len(tiles)  # Number of unique tiles in best paths


if __name__ == '__main__':
    assert part1('example.txt') == 7036, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 11048, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 45, f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == 64, f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
