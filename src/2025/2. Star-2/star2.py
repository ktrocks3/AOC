def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    ids = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in common(filename)[0].split(',')]
    m = max([y for _, y in ids])
    max_length = len(str(m))
    invalid = set()
    for l in range(2, max_length + 1, 2):
        start, end = 10 ** (l // 2 - 1), 10 ** (l // 2)
        for half in range(start, end):
            s = str(half)
            r = int(s+s)
            if r > m:
                break
            invalid.add(r)

    total = 0
    for r in invalid:
        for start, end in ids:
            if start <= r <= end:
                total += r
    return total

import math

def divisors(n):
    result = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)


def part2(filename):
    ids = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in common(filename)[0].split(',')]
    total = 0
    for start, end in ids:
        for x in range(start, end+1):
            for d in divisors(len(str(x))):
                if len(str(x))//d > 1 and str(x) == (str(x)[:d] * (len(str(x))//d)):
                    total += x
                    break
    return total


if __name__ == '__main__':
    assert part1('example.txt') == 1227775554, f"Received {part1('example.txt')} for example on part1"
    # assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 4174379265, f"Received {part2('example.txt')} for example on part2"
    # assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
