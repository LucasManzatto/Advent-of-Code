import functools

inputs = list(map(int, open("input.txt", "r").readlines()))


def calculate(input):
    required_fuel = ((input/3)//1) - 2
    if required_fuel <= 0:
        return 0
    return calculate(required_fuel) + required_fuel


total = functools.reduce(lambda a, b: a+b, list(map(calculate, inputs)))

print(total)
