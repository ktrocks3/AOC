def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    l = common(filename)
    current = 50
    total = 0
    for line in l:
        x = int(line[1:]) if line[0] == 'R' else -int(line[1:])
        current = (current + x) % 100
        if current == 0:
            total += 1
    return total


def part2(filename):
    l = common(filename)
    current = 50
    total = 0
    for line in l:
        x = int(line[1:]) if line[0] == 'R' else -int(line[1:])
        d, current = divmod(current+x, 100)
        total += abs(d)
    return total


if __name__ == '__main__':
    assert part1('example.txt') == 3, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 6, f"Received {part2('example.txt')} for example on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
