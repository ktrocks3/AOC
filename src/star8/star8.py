import re


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def ghostly_traverse(start, info_map, directions, steps=0):
    state = start

    while state[-1] != "Z":
        if steps > 1000000:
            raise Exception('Too many steps: {}'.format(steps))
        steps += 1
        direction = directions[0]
        directions = directions[1:] + directions[0]

        left, right = info_map[state]
        if direction == 'L':
            state = left
        elif direction == 'R':
            state = right
        else:
            raise Exception('Invalid direction: {}'.format(direction))
    return steps


def traverse(start, end, info_map, directions, steps=0):
    state = start

    while state != end:
        if steps > 1000000:
            raise Exception('Too many steps: {}'.format(steps))
        steps += 1
        direction = directions[0]
        directions = directions[1:] + directions[0]

        left, right = info_map[state]
        if direction == 'L':
            state = left
        elif direction == 'R':
            state = right
        else:
            raise Exception('Invalid direction: {}'.format(direction))
    return steps


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    directions = lines.pop(0)

    info_map = {}
    lines.pop(0)
    for line in lines:
        k, l, r = re.findall(r'[A-Z0-9]+', line)
        if k in info_map:
            raise Exception('Duplicate key: {}'.format(k))
        info_map[k] = (l, r)

    return directions, info_map


def part1(filename):
    directions, info_map = common(filename)
    return traverse("AAA", "ZZZ", info_map, directions)


def part2(filename):
    directions, info_map = common(filename)
    As = [k for k in info_map.keys() if k[-1] == 'A']
    res = []
    for A in As:
        steps = ghostly_traverse(A, info_map, directions)
        res.append(steps)
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            res[i] = lcm(res[i], res[j])
    return res[0]


if __name__ == '__main__':
    assert part1('example.txt') == 2
    assert part1('example2.txt') == 6
    print(part1('input.txt'))
    assert part2('example3.txt') == 6
    print(part2('input.txt'))
