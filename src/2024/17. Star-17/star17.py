def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    return


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
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
