import re
def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    line = ''.join(common(filename))
    match = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    match = [m[4:-1].split(',') for m in match]
    match = [int(m[0]) * int(m[1]) for m in match]

    return sum(match)


def part2(filename):
    line = ''.join(common(filename))
    match = re.findall(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', line)
    enabled = True
    total = 0
    for m in match:
        if enabled:
            if m == "don't()":
                enabled = False
                continue
            if m == 'do()':
                continue
            m = m[4:-1].split(',')
            total += int(m[0]) * int(m[1])
        else:
            if m == 'do()':
                enabled = True

    return total


if __name__ == '__main__':
    assert part1('example.txt') == 161, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example2.txt') == 48, f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
