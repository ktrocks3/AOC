def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    def can_form(pattern, available, memo):
        # If the pattern is empty, it's possible.
        if pattern == "":
            return True

        # If we have already computed this pattern, return the result.
        if pattern in memo:
            return memo[pattern]

        # Check if the pattern can be formed using available towels.
        for towel in available:
            if pattern.startswith(towel):  # Match only the prefix
                if can_form(pattern[len(towel):], available, memo):  # Recurse with the remaining string
                    memo[pattern] = True
                    return True

        # If no combination works, store and return False
        memo[pattern] = False
        return False

    # Read file and extract available towels and patterns.
    file = common(filename)
    available = [x.strip() for x in file[0].split(',')]
    patterns = file[2:]  # Skip the blank line and towel definitions

    # Count the number of designs that can be formed
    count = 0
    memo = {}  # Memoization dictionary
    for pattern in patterns:
        if can_form(pattern, available, memo):
            print(f"Possible: {pattern}")
            count += 1
        else:
            print(f"Impossible: {pattern}")

    return count


def part2(filename):
    def count_ways(pattern, available, memo):
        if pattern == "":
            return 1  # Base case: one way to form an empty pattern

        if pattern in memo:
            return memo[pattern]

        total_ways = 0
        for towel in available:
            if pattern.startswith(towel):
                # Recursively calculate ways for the remaining string
                total_ways += count_ways(pattern[len(towel):], available, memo)

        memo[pattern] = total_ways
        return total_ways

    file = common(filename)
    available = [x.strip() for x in file[0].split(',')]
    patterns = file[2:]

    total_arrangements = 0
    memo = {}
    for pattern in patterns:
        arrangements = count_ways(pattern, available, memo)
        total_arrangements += arrangements

    return total_arrangements


if __name__ == '__main__':
    assert part1('example.txt') == 6, f"Received {part1('example.txt')} for example on part1"
    # assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 16, f"Received {part2('example.txt')} for example on part2"
    # assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
