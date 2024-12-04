def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    safe = 0
    for report in common(filename):
        report = report.split()
        flag = True
        inc = True
        dec = True
        for i in range(len(report)-1):
            if 1 > abs(int(report[i])-int(report[i+1])) or abs(int(report[i])-int(report[i+1])) > 3:
                flag = False
            if int(report[i]) < int(report[i+1]):
                dec = False
            if int(report[i]) > int(report[i+1]):
                inc = False
            if not inc and not dec:
                flag = False
                break
        if flag:
            safe += 1
    return safe

def part2(filename):
    def is_safe(report):
        inc = True
        dec = True
        for num in range(len(report)-1):
            if 1 > abs(int(report[num])-int(report[num+1])) or abs(int(report[num])-int(report[num+1])) > 3:
                return False
            if int(report[num]) < int(report[num+1]):
                dec = False
            if int(report[num]) > int(report[num+1]):
                inc = False
            if not inc and not dec:
                return False
        return True

    safe = 0
    for row in common(filename):
        row = [int(x) for x in row.split()]
        for i in range(len(row)):
            if is_safe(row[:i] + row[i+1:]):
                safe += 1
                break

    return safe


if __name__ == '__main__':
    assert part1('example.txt') == 2, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 4, f"Received {part2('example.txt')} for example on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
