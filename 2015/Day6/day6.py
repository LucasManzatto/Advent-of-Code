import re
import functools
inputs = open('input.txt').read().splitlines()


def part1():
    lights = {}
    for elem in inputs:
        x0, y0, x1, y1 = list(map(int, re.findall(r'\d+', elem)))
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if re.search(r'turn on', elem):
                    value = 1
                elif re.search(r'turn off', elem):
                    value = 0
                else:
                    value = not lights.get((x, y), 0)
                lights[x, y] = value

    lit_lights = list(lights.values()).count(1)
    print(lit_lights)


def part2():
    lights = {}
    for elem in inputs:
        x0, y0, x1, y1 = list(map(int, re.findall(r'\d+', elem)))
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if re.search(r'turn on', elem):
                    value = 1
                elif re.search(r'turn off', elem):
                    value = -1
                else:
                    value = 2
                total = lights.get((x, y), 0) + value
                lights[x, y] = total if total >= 0 else 0

    total_brightness = functools.reduce(lambda a, b: a + b, lights.values())
    print(total_brightness)


part2()
