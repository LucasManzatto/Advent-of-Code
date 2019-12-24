inputs = list(map(lambda x: x.split('x'), open(
    'input.txt').read().splitlines()))
inputs = [list(map(int, elem)) for elem in inputs]


def part1():
    total_paper = 0
    for elem in inputs:
        length, height, width = elem
        area1 = length * width
        area2 = width * height
        area3 = height * length
        smallest = min([area1, area2, area3])
        total_paper += 2*area1 + 2*area2 + 2*area3 + smallest

    print(total_paper)


def part2():
    total_ribbon = 0
    for elem in inputs:
        length, height, width = elem
        total_ribbon += 2 * min(width+length, width+height, length+height) + length * width * height
    print(total_ribbon)


part1()
part2()
