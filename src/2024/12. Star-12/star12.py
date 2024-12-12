from collections import defaultdict


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


from collections import defaultdict


def part1(filename):
    def flood_fill(grid, i, j, plant_type, visited):
        """ Perform DFS to find all connected plots of the same plant type (a region) """
        stack = [(i, j)]
        area = 0
        perimeter = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        while stack:
            x, y = stack.pop()

            # Skip if already visited
            if visited[x][y]:
                continue

            visited[x][y] = True
            area += 1

            # Check the 4 directions for perimeter
            local_perimeter = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If the neighbor is out of bounds or not the same plant type, count as exposed (part of the perimeter)
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != plant_type:
                    local_perimeter += 1
                # Otherwise, if it's the same plant, add it to the stack for further exploration
                elif not visited[nx][ny]:
                    stack.append((nx, ny))

            perimeter += local_perimeter

        return area, perimeter

    # Load the grid (we assume common(filename) reads the file and returns a 2D grid of characters)
    file = common(filename)
    visited = [[False] * len(file[0]) for _ in range(len(file))]  # Keep track of visited plots
    total_cost = 0

    # Loop through each plot in the grid
    for i in range(len(file)):
        for j in range(len(file[0])):
            # If the plot hasn't been visited, it's a new region
            if not visited[i][j]:
                plant_type = file[i][j]
                area, perimeter = flood_fill(file, i, j, plant_type, visited)
                # Calculate cost for this region: area * perimeter
                total_cost += area * perimeter

    return total_cost


def part2(filename):
    def get_num_sides(region):
        # We nominate the right and belowest part of a perimeter
        # as the segment "owning" the side. There can only be one such.
        # We count the number of owners.
        up_sides = 0
        down_sides = 0
        left_sides = 0
        right_sides = 0
        for (x, y) in region:
            left = x - 1
            right = x + 1
            above = y - 1
            below = y + 1
            right_not_in_region = (right, y) not in region
            below_not_region = (x, below) not in region

            if (x, above) not in region:
                if right_not_in_region or (right, above) in region:
                    up_sides += 1

            if (x, below) not in region:
                if right_not_in_region or (right, below) in region:
                    down_sides += 1

            if (left, y) not in region:
                if below_not_region or (left, below) in region:
                    left_sides += 1

            if (right, y) not in region:
                if below_not_region or (right, below) in region:
                    right_sides += 1

        return up_sides + down_sides + left_sides + right_sides


    def flood_fill(grid, i, j, plant_type, visited):
        """ Perform DFS to find all connected plots of the same plant type (a region) """
        stack = [(i, j)]
        region = set()  # Keep track of all cells in the current region
        area = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        while stack:
            x, y = stack.pop()

            # Skip if already visited
            if visited[x][y]:
                continue

            visited[x][y] = True
            region.add((x, y))  # Add the current cell to the region
            area += 1

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # If the neighbor is part of the same region, add to stack
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == plant_type and not visited[nx][ny]:
                    stack.append((nx, ny))

        sides = get_num_sides(region)  # Use the get_num_sides logic to count sides
        return area, sides

    # Load the grid
    file = common(filename)
    visited = [[False] * len(file[0]) for _ in range(len(file))]  # Keep track of visited plots
    total_cost = 0

    # Loop through each plot in the grid
    for i in range(len(file)):
        for j in range(len(file[0])):
            # If the plot hasn't been visited, it's a new region
            if not visited[i][j]:
                plant_type = file[i][j]
                area, sides = flood_fill(file, i, j, plant_type, visited)
                # Calculate cost for this region: area * sides
                total_cost += area * sides

    return total_cost


if __name__ == '__main__':
    assert part1('example.txt') == 140, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 772, f"Received {part1('example2.txt')} for example2 on part1"
    assert part1('example3.txt') == 1930, f"Received {part1('example3.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 80, f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == 436, f"Received {part2('example2.txt')} for example2 on part2"
    assert part2('example3.txt') == 1206, f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
