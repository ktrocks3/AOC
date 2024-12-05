def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    lines = common(filename)
    rules = {}
    pages = []
    rulesDone = False
    for l in lines:
        if l == '':
            rulesDone = True
            continue
        if rulesDone:
            pages.append(l.split(','))
        else:
            l, r = l.split('|')
            s = rules.get(r, set())
            s.add(l)
            rules[r] = s

    mid = 0
    for p, page in enumerate(pages):
        flag = True
        for i in range(len(page)):
            for j in range(i,len(page)):
                if page[i] in rules and page[j] in rules[page[i]]:
                    flag = False
                    break
        if flag:
            mid += int(page[len(page)//2])
    return mid



def part2(filename):
    pass


if __name__ == '__main__':
    assert part1('example.txt') == 143, f"Received {part1('example.txt')} for example on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == "", f"Received {part2('example.txt')} for example on part2"
    assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
