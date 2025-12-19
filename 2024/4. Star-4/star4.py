def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    lines = common(filename)
    # Gotta start with the X's
    search = 'XMAS!'
    X = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'X':
                X.append((i, j))
    total = 0
    for x in X:
        nextLetter = 'M'
        dirs = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
        valid = [True for _ in range(len(dirs))]
        while nextLetter != '!':
            for i in range(len(dirs)):
                dx, dy = x[0] + dirs[i][0] * search.index(nextLetter), x[1] + dirs[i][1] * search.index(nextLetter)
                if not (0 <= dx < len(lines) and 0 <= dy < len(lines[0])):
                    valid[i] = False
                    continue
                if valid[i]:
                    if lines[dx][dy] != nextLetter:
                        valid[i] = False
            nextLetter = search[1 + search.index(nextLetter)]
        total += sum(valid)
    return total


def part2(filename):
    lines = common(filename)
    # Gotta start with the A's
    A = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'A':
                A.append((i, j))
    total = 0
    for ax, ay in A:
        if 0 == ax or ax == len(lines) - 1 or 0 == ay or ay == len(lines[0]) - 1:
            continue
        tl, tr, bl, br = (ax - 1, ay - 1), (ax - 1, ay + 1), (ax + 1, ay - 1), (ax + 1, ay + 1)
        if (lines[tl[0]][tl[1]] == 'M' and lines[br[0]][br[1]] == 'S' and
                lines[tr[0]][tr[1]] == 'M' and lines[bl[0]][bl[1]] == 'S'):
            total += 1
        if (lines[tl[0]][tl[1]] == 'S' and lines[br[0]][br[1]] == 'M' and
                lines[tr[0]][tr[1]] == 'S' and lines[bl[0]][bl[1]] == 'M'):
            total += 1
        if (lines[tl[0]][tl[1]] == 'S' and lines[br[0]][br[1]] == 'M' and
                lines[tr[0]][tr[1]] == 'M' and lines[bl[0]][bl[1]] == 'S'):
            total += 1
        if (lines[tl[0]][tl[1]] == 'M' and lines[br[0]][br[1]] == 'S' and
                lines[tr[0]][tr[1]] == 'S' and lines[bl[0]][bl[1]] == 'M'):
            total += 1
    return total


if __name__ == '__main__':
    assert part1('example.txt') == 4, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt') == 18, f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example3.txt') == 1, f"Received {part2('example3.txt')} for example on part2"
    assert part2('example2.txt') == 9, f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
