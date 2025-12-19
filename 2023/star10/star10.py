def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    return lines


def findNeighbors(x, y, grid, forbidden=[]):
    match (grid[x][y]):
        case '|':
            return [z for z in [(x - 1, y), (x + 1, y)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case '-':
            return [z for z in [(x, y - 1), (x, y + 1)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case 'L':
            return [z for z in [(x - 1, y), (x, y + 1)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case 'J':
            return [z for z in [(x - 1, y), (x, y - 1)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case '7':
            return [z for z in [(x, y - 1), (x + 1, y)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case 'F':
            return [z for z in [(x + 1, y), (x, y + 1)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case 'S':
            return [z for z in
                    [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1),
                     (x + 1, y - 1)]
                    if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]]) and z not in forbidden]
        case _:
            return []


def find_path(x, y, grid, visited):
    stack = [(x, y)]  # Initialize stack with the starting node

    while stack:
        current_x, current_y = stack.pop()
        for n in findNeighbors(current_x, current_y, grid):
            if n not in visited:
                visited.append(n)
                stack.append(n)
    return visited


def part1(filename, return_path=False):
    grid = common(filename)
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
                break
        if start:
            break
    path = []
    for n in findNeighbors(start[0], start[1], grid):
        if start not in (findNeighbors(n[0], n[1], grid)):
            continue
        p = find_path(n[0], n[1], grid, [start, n])
        if start in findNeighbors(p[-1][0], p[-1][1], grid):
            path = p
            break
    if return_path:
        return path
    return len(path) // 2


def get_nearby(x, y, grid):
    return [z for z in
            [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if 0 <= z[0] < len(grid) and 0 <= z[1] < len(grid[z[0]])]


def pad(grid, path):
    ngrid = [[x for x in y] for y in grid]
    n_i = 0
    for i in range(len(grid) - 1):
        check_left_right = []
        check_up_down = []
        for j in range(len(grid[i]) - 1):
            if (i, j + 1) in findNeighbors(i, j, grid) and (i, j + 1) in path:
                check_left_right.append('-')
            else:
                check_left_right.append('#')
            if (i + 1, j) in findNeighbors(i, j, grid) and (i + 1, j) in path:
                check_up_down.append('|')
            else:
                check_up_down.append('#')
        ngrid[n_i] = [val for pair in zip(grid[i], check_left_right) for val in pair]
        ngrid.insert(n_i + 1, check_up_down)
        n_i += 2
    for i in range(len(ngrid)):
        for j in range(len(ngrid[i])):
            print(ngrid[i][j], end='')
        print()


def flood(grid):
    grid[0][0] = 2
    stack = [(0, 0)]
    while stack:
        current_x, current_y = stack.pop()
        for n in get_nearby(current_x, current_y, grid):
            nx, ny = n
            if grid[nx][ny] == 0 and not is_between_pipes(nx, ny, grid):
                grid[nx][ny] = 2
                stack.append(n)

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                total += 1
    print(total)


def part2(filename):
    path = part1(filename, return_path=True)
    grid = common(filename)
    pad(grid, path)


if __name__ == '__main__':
    # assert part1('example.txt') == 4
    # assert part1('example2.txt') == 8
    # print(part1('input.txt'))
    part2('example3.txt')
