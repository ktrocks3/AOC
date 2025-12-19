def common(filename):
    with open(filename, 'r') as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines


def part1(filename):
    file = common(filename)
    s = []
    i = 0
    even = True
    for c in file[0]:
        if even:
            s += [i] * int(c)
            i += 1
        else:
            s += ['.'] * int(c)
        even = not even

    left, right = 0, len(s) - 1
    while left <= right:
        if s[right] == '.':
            right -= 1
        if s[left] == '.':
            s[left], s[right] = s[right], s[left]
        else:
            left += 1



    total = 0
    for i in range(len(s)):
        if s[i] == '.':
            break
        total += i * s[i]
    return total


def part2(filename):
    file = common(filename)
    s = []
    even = True
    blocks = {}
    index = 0

    # Parse input and build the sequence
    for c in file[0]:
        if even:
            count = int(c)
            s.extend([str(index)] * count)
            blocks[index] = count
            index += 1
        else:
            s.extend(['.'] * int(c))
        even = not even

    # Rearrange blocks
    for block, count in sorted(blocks.items(), key=lambda x: -x[0]):  # Process blocks by size descending
        print(block)
        block_str = str(block)
        first_position = s.index(block_str)
        for i in range(len(s)):
            # Check if there is enough space to place the block
            if i <= first_position and all(c == '.' for c in s[i:i+count]) and i+count <= len(s):
                # Move the block
                current_positions = [first_position + j for j in range(count)]
                for j in range(count):
                    s[current_positions[j]] = '.'
                    s[i + j] = block_str
                break

    # Calculate total score
    total = sum(i * int(val) for i, val in enumerate(s) if val != '.')
    return total



if __name__ == '__main__':
    assert part1('example.txt') == 1928, f"Received {part1('example.txt')} for example on part1"
#    assert part1('example2.txt') == "", f"Received {part1('example2.txt')} for example2 on part1"
    print(f'Part 1 answer: {part1('input.txt')}')
    assert part2('example.txt') == 2858, f"Received {part2('example.txt')} for example on part2"
#    assert part2('example2.txt') == "", f"Received {part2('example2.txt')} for example2 on part2"
    print(f'Part 2 answer: {part2('input.txt')}')
