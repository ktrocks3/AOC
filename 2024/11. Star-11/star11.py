from collections import defaultdict


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename, blinks):
    stones = [int(x) for x in common(filename)[0].split(' ')]
    for blink in range(blinks):
        ns = []
        for i in range(len(stones)):
            if stones[i] == 0:
                ns.append(1)
            elif len(str(stones[i])) % 2 == 0:
                stones[i] = str(stones[i])
                l, r = stones[i][:(len(stones[i]) // 2)], stones[i][(len(stones[i]) // 2):]
                ns.append(int(l))
                ns.append(int(r))
            else:
                ns.append(stones[i] * 2024)
        stones = ns
    return len(stones)


def part2(filename, blinks):
    stones = defaultdict(int)
    for x in common(filename)[0].split(' '):
        stones[int(x)] += 1
    for blink in range(blinks):
        ns = defaultdict(int)
        for x in stones:
            if x == 0:
                ns[1] += stones[0]
            elif len(str(x)) % 2 == 0:
                x = str(x)
                l, r = x[:len(x) // 2], x[len(x) // 2:]
                x = int(x)
                ns[int(l)] += stones[x]
                ns[int(r)] += stones[x]
            else:
                ns[x * 2024] = stones[x]
        stones = ns
    return sum(stones.values())


if __name__ == '__main__':
    assert part1('example.txt', 1) == 7, f"Received {part1('example.txt', 1)} for example on part1"
    assert part1('example2.txt', 6) == 22, f"Received {part1('example2.txt', 6)} for example2 on part1"
    assert part1('example2.txt', 25) == 55312, f"Received {part1('example2.txt', 25)} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt', 25)}')
    assert part2('example.txt', 1) == 7, f"Received {part2('example.txt', 1)} for example on part1"
    assert part2('example2.txt', 6) == 22, f"Received {part2('example2.txt', 6)} for example2 on part1"
    assert part2('example2.txt', 25) == 55312, f"Received {part2('example2.txt', 25)} for example2 on part1"
    print(f'Part 2 answer: {part2('input.txt', 75)}')
