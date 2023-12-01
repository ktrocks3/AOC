def find_number(line):
    numwords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = []
    test = ""
    for x in line:
        if x.isdigit():
            nums.append(x)
            continue
        test += x
        inner = test
        while inner != "":
            if inner in numwords:
                nums.append(numwords.index(inner))
                break
            else:
                inner = inner[1:]
    return nums


with open('input.txt', 'r') as f:
    lines = f.readlines()
res = []
for line in lines:
    a = find_number(line)
    res.append(str(a[0]) + str(a[-1]))

print(sum([int(x) for x in res]))
