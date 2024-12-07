def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    total = 0
    for line in common(filename):
        res, vals = line.split(':')
        res, vals = int(res), [int(v) for v in vals.strip().split()]
        gotten = {vals[0]}
        for i in range(1, len(vals)):
            ng = set()
            for g in gotten:
                for op in [True, False]:
                    if op:
                        ng.add(g + vals[i])
                    else:
                        ng.add(g * vals[i])
            gotten = ng
        if res in gotten:
            total += res
    return total


def part2(filename):
    total = 0
    for line in common(filename):
        res, vals = line.split(':')
        res, vals = int(res), [int(v) for v in vals.strip().split()]
        gotten = {vals[0]}
        for i in range(1, len(vals)):
            ng = set()
            for g in gotten:
                for op in range(3):
                    if op == 0:
                        ng.add(g + vals[i])
                    elif op == 1:
                        ng.add(g * vals[i])
                    else:
                        ng.add(int(str(g) + str(vals[i])))
            gotten = ng
        if res in gotten:
            total += res
    return total


if __name__ == '__main__':
    assert part1('example.txt') == 3749, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 11387, f"Received {part2('example.txt')} for example on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
