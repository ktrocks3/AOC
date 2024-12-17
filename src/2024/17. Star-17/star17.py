from collections import deque


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    def combo(combo_code):
        if combo_code <= 3:
            return combo_code
        if combo_code == 4:
            return a
        if combo_code == 5:
            return b
        if combo_code == 6:
            return c
        raise ValueError(f'{combo_code} should not appear')

    file = common(filename)
    a, b, c, prog, out = 0, 0, 0, [], []
    for line in file:
        if 'Register A' in line:
            a = int(line[11:])
        if 'Register B' in line:
            b = int(line[11:])
        if 'Register C' in line:
            c = int(line[11:])
        if 'Program' in line:
            prog = [int(x) for x in line[8:].strip().split(',')]

    i = 0
    while i < len(prog) - 1:
        instr, code = prog[i], prog[i + 1]
        match instr:
            case 0:
                a = a // (2 ** combo(code))
            case 1:
                b = b ^ code
            case 2:
                b = combo(code) % 8
            case 3:
                if a == 0:
                    i += 2
                else:
                    i = code
                continue
            case 4:
                b = b ^ c
            case 5:
                out.append(combo(code) % 8)
            case 6:
                b = a // (2 ** combo(code))
            case 7:
                c = a // (2 ** combo(code))
        i += 2

    return (str(out)[1:-1]).replace(' ', ''), a, b, c


def part2(filename):
    return



if __name__ == '__main__':
    assert part1('example.txt')[2] == 1, f"Received {part1('example.txt')} for example on part1"
    assert part1('example2.txt')[0] == "0,1,2", f"Received {part1('example2.txt')} for example2 on part1"
    assert part1('example3.txt')[0] == "4,2,5,6,7,7,7,7,3,1,0", \
        f"Received {part1('example3.txt')} for example2 on part1"
    assert part1('example3.txt')[1] == 0, f"Received {part1('example3.txt')} for example2 on part1"
    assert part1('example4.txt')[2] == 26, f"Received {part1('example4.txt')} for example2 on part1"
    assert part1('example5.txt')[2] == 44354, f"Received {part1('example5.txt')} for example2 on part1"
    assert part1('example6.txt')[0] == "4,6,3,5,6,3,5,2,1,0", f"Received {part1('example6.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')[0]}')
    assert part1('example7.txt')[0] == "0,3,5,4,3,0", f"Received {part1('example7.txt')} for example on part2"
    assert part2('input.txt') > 16300095239778
    print(f'Part 2 answer: {part2('input.txt')}')
