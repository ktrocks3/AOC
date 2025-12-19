import scipy


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
        result = scipy.optimize.linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=[1, 1])

        # Check the result
        if result.success:
            fun_rounded = round(result.fun)
            if abs(result.fun - fun_rounded) < 1e-6:  # Close enough to an integer
                return fun_rounded
            else:
                return 0
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
    c = [3, 1]

    from sympy import symbols, Eq, solve, Integer

    def calculate_machine(A_eq, b_eq):
        a, b = symbols('a b')
        equations = [
            Eq(A_eq[i][0] * a + A_eq[i][1] * b, b_eq[i])
            for i in range(len(A_eq[0]))
        ]
        solutions = solve(equations, (a, b))

        if solutions:
            a_sol, b_sol = solutions[a], solutions[b]
            if isinstance(a_sol, Integer) and isinstance(b_sol, Integer):
                return 3 * a_sol + b_sol
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
            Prize.append(10000000000000 + int(line[1].strip("'").split(',')[0]))
            Prize.append(10000000000000 + int(line[2].strip("'")))
            total += calculate_machine(A, Prize)
            A = [[], []]
    return total


if __name__ == '__main__':
    assert part1('example.txt') == 480, f"Received {part1('example.txt')} for example on part1"
    # assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part1('input.txt') == 26299, f"Received {part1('input.txt')} for input on part1"
    assert part2('example.txt') == 875318608908, f"Received {part2('example.txt')} for example on part2"
    # assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
