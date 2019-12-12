from collections import namedtuple
import itertools
import math
space = open('input_test2.txt').read().splitlines()
Coordinates = namedtuple('Coordinates', 'x y')
asteroids = []
for y, line in enumerate(space):
    for x, obj in enumerate(line):
        if obj == '#':
            asteroids.append(Coordinates(x, y))

def get_angles(asteroids, ast_to_test, radians=True):
    angles = {}
    for ast in asteroids:
        angle = math.atan2(ast.x - ast_to_test.x,ast.y -  ast_to_test.y)
        angle = angle if radians else math.degrees(angle)
        angles[angle]= ast
    if len(angles) == 326:
        print(ast)
    return angles


best_asteroid = max([len(get_angles(asteroids, asteroid))
                     for asteroid in asteroids])
print(best_asteroid)

def calculate_distance(ast1, ast2):
    return (math.sqrt(math.pow(ast1.x - ast2.x, 2) + math.pow(ast1.y - ast2.y, 2)), ast2)



test = Coordinates(11,13)
asteroids = list(filter(lambda x: x != test,asteroids))
angles = get_angles(asteroids, test, radians=False)
print(len(angles))
vaporized_asteroids = [angles[i] for i in sorted(angles.keys(),reverse=True)]
print(vaporized_asteroids[199])
# first_nine = list(itertools.islice(sorted_angles.values(), 9))
asteroids = [x for x in asteroids if x not in vaporized_asteroids]

# angles = get_angles(asteroids, test, radians=False)
# sorted_angles = {i: angles[i] for i in sorted(angles.keys(),reverse=True)}
# last = list(itertools.islice(sorted_angles.values(), 2))

# print(last)