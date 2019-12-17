import copy
import math
import functools


class Moon:
    def __init__(self, x, y, z):
        self.position = {'x': x, 'y': y, 'z': z}
        self.velocity = {'x': 0, 'y': 0, 'z': 0}
        self.axis = ['x','y','z']

    def change(self, x, y, z):
        self.velocity['x'] += x
        self.velocity['y'] += y
        self.velocity['z'] += z

    def change_pos(self):
        for axis in self.axis:
            self.position[axis] += self.velocity[axis]
        

    def get_energy(self):
        potential_energy = functools.reduce(
            lambda a, b: a + abs(b), self.position.values(), 0)
        kinetic_energy = functools.reduce(
            lambda a, b: a + abs(b), self.velocity.values(), 0)
        return potential_energy * kinetic_energy

    def __str__(self):
        return f"Pos:{self.position}, Vel:{self.velocity}"


first = Moon(4, 12, 13)
second = Moon(-9, 14, -3)
third = Moon(-7, -1, 2)
forth = Moon(-11, 17, -1)

moons = [first, second, third, forth]
original_moons = copy.deepcopy(moons)


def check_axis(original_moons, moons, axis):
    is_equal = True
    for i, moon in enumerate(original_moons):
        is_equal = is_equal and moon.position[axis] == moons[i].position[axis]
    return is_equal


def get_value(first, second):
    value = 0
    if first < second:
        value = 1
    elif first > second:
        value = -1
    return value


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def calculate_lcm(numbers):
    return functools.reduce(lcm, numbers, 1)


def check(first, second):
    [x, y, z] = [get_value(first.position[axis], second.position[axis])
                 for axis in ['x', 'y', 'z']]
    first.change(x, y, z)
    second.change(-x, -y, -z)
    return first, second


def part1(moons):
    c_moons = copy.deepcopy(moons)
    first, second, third, forth = c_moons
    total = 0
    for _ in range(1000):
        first, second = check(first, second)
        first, third = check(first, third)
        first, forth = check(first, forth)
        second, third = check(second, third)
        second, forth = check(second, forth)
        third, forth = check(third, forth)
        for moon in moons:
            moon.change_pos()
    for moon in moons:
        total += moon.get_energy()
    return total


def part2(moons):
    first, second, third, forth = moons
    x = y = z = None
    i = 1
    while 1:
        i += 1
        first, second = check(first, second)
        first, third = check(first, third)
        first, forth = check(first, forth)
        second, third = check(second, third)
        second, forth = check(second, forth)
        third, forth = check(third, forth)
        for moon in moons:
            moon.change_pos()
        if check_axis(original_moons, moons, 'x') and not x:
            x = i
        if check_axis(original_moons, moons, 'y') and not y:
            y = i
        if check_axis(original_moons, moons, 'z') and not z:
            z = i
        if x and y and z:
            break
    return calculate_lcm([x, y, z])


total = part1(moons)
lcm = part2(moons)


print(lcm, total)
