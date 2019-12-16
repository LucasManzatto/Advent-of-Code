import copy
import math
import functools


class Moon:
    def __init__(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def change(self, x, y, z):
        self.vel_x += x
        self.vel_y += y
        self.vel_z += z

    def change_pos(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.pos_z += self.vel_z

    def get_energy(self):
        potential_energy = abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)
        kinetic_energy = abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)
        return potential_energy * kinetic_energy

    def __str__(self):
        return f"Pos:{self.pos_x,self.pos_y,self.pos_z}, Vel:{self.vel_x,self.vel_y,self.vel_z}"


first = Moon(4, 12, 13)
second = Moon(-9, 14, -3)
third = Moon(-7, -1, 2)
forth = Moon(-11, 17, -1)

moons = [first, second, third, forth]
original_moons = copy.deepcopy(moons)


def is_equal(first, second):
    return first.pos_x == second.pos_x and first.pos_y == second.pos_y and first.pos_z == second.pos_z \
        and first.vel_x == second.vel_x and first.vel_y == second.vel_y and first.vel_z == second.vel_z


def check_x_axis(original_moons, moons):
    return original_moons[0].pos_x == moons[0].pos_x and original_moons[1].pos_x == moons[1].pos_x and original_moons[2].pos_x == moons[2].pos_x and original_moons[3].pos_x == moons[3].pos_x


def check_y_axis(original_moons, moons):
    return original_moons[0].pos_y == moons[0].pos_y and original_moons[1].pos_y == moons[1].pos_y and original_moons[2].pos_y == moons[2].pos_y and original_moons[3].pos_y == moons[3].pos_y


def check_z_axis(original_moons, moons):
    return original_moons[0].pos_z == moons[0].pos_z and original_moons[1].pos_z == moons[1].pos_z and original_moons[2].pos_z == moons[2].pos_z and original_moons[3].pos_z == moons[3].pos_z


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
    return functools.reduce(lcm,numbers,1)


def check(first, second):
    x = get_value(first.pos_x, second.pos_x)
    y = get_value(first.pos_y, second.pos_y)
    z = get_value(first.pos_z, second.pos_z)

    first.change(x, y, z)
    second.change(-x, -y, -z)
    return first, second

def part1(moons):
    c_moons = copy.deepcopy(moons)
    first,second,third,forth = c_moons
    total =0
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
    first,second,third,forth = moons
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
        if check_x_axis(original_moons, moons) and not x:
            x = i
        if check_y_axis(original_moons, moons) and not y:
            y = i
        if check_z_axis(original_moons, moons) and not z:
            z = i
        if x and y and z:
            break
    return calculate_lcm([x,y,z])

total = part1(moons)
lcm = part2(moons)


print(lcm,total)
