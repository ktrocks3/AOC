from collections import defaultdict


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    positions = defaultdict(list)
    file = common(filename)
    for i, row in enumerate(file):
        for j, col in enumerate(row):
            if col != '.':
                positions[col].append((i, j))
    s = set()
    # Check pairs of antennas with the same frequency
    for frequency, locations in positions.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                xDiff, yDiff = x2 - x1, y2 - y1

                antinode1 = (x1 - xDiff, y1 - yDiff)
                antinode2 = (x2 + xDiff, y2 + yDiff)

                # Validate bounds and add to set
                if 0 <= antinode1[0] < len(file) and 0 <= antinode1[1] < len(file[0]):
                    s.add(antinode1)
                if 0 <= antinode2[0] < len(file) and 0 <= antinode2[1] < len(file[0]):
                    s.add(antinode2)

    return len(s)


def part2(filename):
    positions = defaultdict(list)
    file = common(filename)
    for i, row in enumerate(file):
        for j, col in enumerate(row):
            if col != '.':
                positions[col].append((i, j))
    s = set()
    # Check pairs of antennas with the same frequency
    for frequency, locations in positions.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                s.add(locations[i])
                s.add(locations[j])
                x1, y1 = locations[i]
                x2, y2 = locations[j]
                xDiff, yDiff = x2 - x1, y2 - y1

                antinode1 = (x1 - xDiff, y1 - yDiff)
                antinode2 = (x2 + xDiff, y2 + yDiff)

                # Validate bounds and add to set
                while 0 <= antinode1[0] < len(file) and 0 <= antinode1[1] < len(file[0]):
                    s.add(antinode1)
                    antinode1 = (antinode1[0] - xDiff, antinode1[1] - yDiff)
                while 0 <= antinode2[0] < len(file) and 0 <= antinode2[1] < len(file[0]):
                    s.add(antinode2)
                    antinode2 = (antinode2[0] + xDiff, antinode2[1] + yDiff)

    
    return len(s)


if __name__ == '__main__':
    assert part1('example.txt') == 14, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 2, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example3.txt') == 9, f"Received {part2('example2.txt')} for example3 on part2"
    assert part2('example.txt') == 34, f"Received {part2('example.txt')} for example on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
