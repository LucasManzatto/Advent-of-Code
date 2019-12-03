input = open("input.txt", "r").readlines()

results = []

direction_x = dict(zip('LRUD', [-1, 1, 0, 0]))
direction_y = dict(zip('LRUD', [0, 0, 1, -1]))


def get_path(commands):
    (x, y) = (0, 0)
    dict = {}
    position = 0
    for command in commands.split(','):
        direction, move = command[:1], int(command[1:])
        for _ in range(move):
            position += 1
            x += direction_x[direction]
            y += direction_y[direction]
            dict[(x, y)] = position
    return dict


first_path, second_path = map(get_path, input)

intersections = set(first_path).intersection(second_path)

sum_of_distances = [sum((first_path[x], second_path[x]))
                    for x in intersections]

mininum_manhattam = min(abs(x)+abs(y) for (x, y) in intersections)

minimum_path = min(sum_of_distances)

print(mininum_manhattam, minimum_path)
