from scipy.optimize import linprog


def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    c = [3, 1]

    def calculate_machine(A_eq, b_eq):

        # Bounds for x and y
        bounds = [(0, 100), (0, 100)]

        # Solve the linear program
        result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

        # Check the result
        if result.success:
            return round(result.fun)
        else:
            return 0

    file = common(filename)
    A = [[], []]
    total = 0
    for line in file:
        Prize = []
        if 'Button' in line:
            line = [int(x.strip().split('+')[1]) for x in line.split(':')[1].strip().split(',')]
            A[0].append(line[0])
            A[1].append(line[1])
        if 'Prize' in line:
            line = line[7:].split('=')
            Prize.append(int(line[1].strip("'").split(',')[0]))
            Prize.append(int(line[2].strip("'")))
            total += calculate_machine(A, Prize)
            A = [[], []]
    return total


def part2(filename):
    return


if __name__ == '__main__':
    assert part1('example.txt') == 480, f"Received {part1('example.txt')} for example on part1"
    # assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    # assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
