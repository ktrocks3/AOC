def get_sum(input_games):
    input_games = dict(sorted(input_games.items(), key=lambda x: (x[0][0], -int(x[0][1]))))
    return sum((i + 1) * value for i, value in enumerate(input_games.values()))


def part1(path):
    with open(path, 'r') as f:
        games = {}
        orders = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        ordering = {value: index for index, value in enumerate(orders)}

        for line in f.read().split('\n'):
            hand, bid = line.split()
            cards_dict = {char: hand.count(char) for char in set(hand)}
            cards_dict = dict(sorted(cards_dict.items(), key=lambda x: -x[1]))
            keys = ''.join(str(ordering[key]).zfill(2) for key in hand)
            values = ''.join(str(value) for value in cards_dict.values())
            games[(values, keys)] = int(bid)

        return get_sum(games)


def part2(path):
    with open(path, 'r') as f:
        games = {}
        orders = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        ordering = {value: index for index, value in enumerate(orders)}

        for line in f.read().split('\n'):
            hand, bid = line.split()
            cards_dict = {char: hand.count(char) for char in set(hand)}
            cards_dict = dict(sorted(cards_dict.items(), key=lambda x: -x[1]))

            if 'J' in cards_dict.keys():
                normal_values = [v for k, v in cards_dict.items() if k != 'J']
                if len(normal_values) != 0:
                    max_count = max(normal_values)
                    max_values = [key for key, value in cards_dict.items() if value != 'J' and value == max_count]
                    max_value = max(max_values, key=lambda x: -ordering[x])
                else:
                    max_value = 'A'
                cards_dict[max_value] = cards_dict.get('J') + cards_dict.get(max_value, 0)
                cards_dict = dict(sorted(cards_dict.items(), key=lambda x: -x[1]))
                del cards_dict['J']

            keys = ''.join(str(ordering[key]).zfill(2) for key in hand)
            values = ''.join(str(value) for value in cards_dict.values())
            games[(values, keys)] = int(bid)

        return get_sum(games)


if __name__ == '__main__':
    assert part1('example.txt') == 6440
    print(part1('input.txt'))
    assert part2('example.txt') == 5905
    print(part2('input.txt'))