from collections import namedtuple
from math import *
Coordinates = namedtuple('Coordinates', 'x y')

space = open('input.txt').read().splitlines()
asteroids = []
for y, line in enumerate(space):
    for x, obj in enumerate(line):
        if obj == '#':
            asteroids.append(Coordinates(x, y))


def distance(a, b):
    return abs(a.x - b.x)+abs(a.y - b.y)


def get_angle(a, b):
    return degrees(atan2((a.x - b.x), (a.y - b.y)))


def compute_lines(base):
    lines = {}
    for ast in asteroids:
        angle = get_angle(ast, base)
        lines[angle] = [ast]
    return base, lines


lines_of_sight = map(compute_lines, asteroids)
(best_ast,line_of_sight) = max(lines_of_sight, key=lambda x: len(x[1]))
last_erased = [line_of_sight[angle][0] for angle in sorted(compute_lines(best_ast)[1].keys(),reverse=True)][199]
print(len(line_of_sight), best_ast, last_erased)
