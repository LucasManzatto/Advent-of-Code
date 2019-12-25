inputs = open('input.txt').read()

directions = {
    '^': (0, 1),
    '>': (1, 0),
    'v': (0, -1),
    '<': (-1, 0)
}


def part2():
    pos = [0, 0]
    robot_pos = [0, 0]
    houses = {(0, 0): 0}
    robot_houses = {(0, 0): 0}
    for index, elem in enumerate(inputs):
        direction = directions[elem]
        if index % 2 == 0:
            robot_pos[0] += direction[0]
            robot_pos[1] += direction[1]
            robot_houses[(robot_pos[0], robot_pos[1])] = 0
        else:
            pos[0] += direction[0]
            pos[1] += direction[1]
            houses[(pos[0], pos[1])] = 0

    unique_houses = len(houses) + len(robot_houses) - \
        len(set(houses).intersection(robot_houses))
    print(unique_houses)


def part1():
    pos = [0, 0]
    houses = {(0, 0): 0}
    for elem in inputs:
        direction = directions[elem]
        pos[0] += direction[0]
        pos[1] += direction[1]
        houses[(pos[0], pos[1])] = 0

    print(len(houses))

part1()
part2()
