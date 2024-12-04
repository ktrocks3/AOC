def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    left, right = [], []
    for row in common(filename):
        l, r = row.split()
        left.append(l)
        right.append(r)
    left, right = sorted(left), sorted(right)
    total = 0
    for l, r in zip(left, right):
        total += abs(int(l) - int(r))
    return total

def part2(filename):
    left, right = [], []
    for row in common(filename):
        l, r = row.split()
        left.append(l)
        right.append(r)
    counter = {}
    for r in right:
        counter[r] = counter.get(r, 0) + 1
    total = 0
    for l in left:
        total += int(l) * counter.get(l, 0)
    return total


if __name__ == '__main__':
    assert part1('example.txt') == 11, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 31, f"Received {part2('example.txt')} for example on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
