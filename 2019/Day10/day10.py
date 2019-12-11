space = open('input_test.txt').read().splitlines()
y = 0
asteroids = []
for y, line in enumerate(space):
    for x, obj in enumerate(line):
        if obj == '#':
            asteroids.append((x, y))

test = asteroids[6]
distances = {}
print(test)
for asteroid in asteroids:
    distance = abs(test[0] - asteroid[0]) + abs(test[1] - asteroid[1])
    if distance > 0:
        distances[asteroid] = distance

sorted_distances = {k: v for k, v in sorted(
    distances.items(), key=lambda item: item[1])}
# {k: v for k, v in sorted_distances.items() if v == distance}
print(asteroids)
can_not_see = []
for ast, distance in sorted_distances.items():
    if ast not in can_not_see:
        if test[0] == ast[0]:
            after_ast = {k: v for k, v in sorted_distances.items(
            ) if k[0] == ast[0] and k[1] > ast[1]}
            if len(after_ast) > 0:
                can_not_see.append(after_ast)
        elif test[1] == ast[1]:
            after_ast = {k: v for k, v in sorted_distances.items(
            ) if k[1] == ast[1] and k[0] > ast[0]}
            if len(after_ast) > 0:
                can_not_see.append(after_ast)
        elif abs(test[0] - ast[0]) == abs(test[1] - ast[1]):
            x, y = ast
            count = 0
            while count < 10:
                count += 1
                x += 1 if test[0] < ast[0] else -1
                y += 1
                adjacent = sorted_distances.get((x, y), False)
                if adjacent:
                    can_not_see.append((x, y))
        else:
            x, y = ast
            dist_to_x = abs(test[0] - ast[0])
            dist_to_y = abs(test[1] - ast[1])
            print(f'Found rectangle:{ast} , dist to x:{dist_to_x},dist to y:{dist_to_y}')
            count = 0
            while count < 10:
                count+=1
                x += dist_to_x if test[0] < ast[0] else -dist_to_x
                y += dist_to_y if test[1] < ast[1] else -dist_to_y
                adjacent = sorted_distances.get((x, y), False)
                if adjacent:
                    can_not_see.append((x, y))

print(can_not_see)
print(len(sorted_distances) - len(can_not_see))
