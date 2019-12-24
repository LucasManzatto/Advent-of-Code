inputs = open('input.txt').readline()


def part1():
    up = inputs.count('(')
    down = inputs.count(')')
    floor = up - down
    print(floor)


def part2():
    floor = 0
    for pos, elem in enumerate(inputs):
        floor = floor + 1 if elem == '(' else floor - 1
        if floor == -1:
            print(pos + 1)
            break

part1()
part2()
