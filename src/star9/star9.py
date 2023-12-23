def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    return


def extrapolate(history):
    rows = [[]]
    rows[0] = list(map(int, history.split(' ')))
    while any(x != 0 for x in rows[-1]):
        rows.append([])
        for i in range(len(rows[-2]) - 1):
            rows[-1].append(rows[-2][i + 1] - rows[-2][i])
    rows[-1].append(0)
    for i in range(len(rows) - 1, 0, -1):
        rows[i - 1].append(rows[i][-1] + rows[i - 1][-1])
    return rows[0][-1]


def reverse_extrapolate(history):
    rows = [[]]
    rows[0] = list(map(int, history.split(' ')))
    while any(x != 0 for x in rows[-1]):
        rows.append([])
        for i in range(len(rows[-2]) - 1):
            rows[-1].append(rows[-2][i + 1] - rows[-2][i])
    rows[-1].insert(0, 0)
    for i in range(len(rows) - 1, 0, -1):
        rows[i - 1].insert(0, rows[i - 1][0] - rows[i][0])
    return rows[0][0]


def part1(filename):
    lines = common(filename)
    return sum(extrapolate(line) for line in lines)


def part2(filename):
    lines = common(filename)
    return sum(reverse_extrapolate(line) for line in lines)


if __name__ == '__main__':
    example_lines = common('example.txt')
    assert extrapolate(example_lines[0]) == 18
    assert extrapolate(example_lines[1]) == 28
    assert extrapolate(example_lines[2]) == 68
    assert part1('example.txt') == 114
    print(part1('input.txt'))
    assert reverse_extrapolate(example_lines[2]) == 5
    assert reverse_extrapolate(example_lines[0]) == -3
    assert reverse_extrapolate(example_lines[1]) == 0
    assert part2('example.txt') == 2
    print(part2('input.txt'))
