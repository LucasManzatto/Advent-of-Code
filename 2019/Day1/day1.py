
inputs = open("input.txt", "r")


def calculate(input):
    required_fuel = ((input/3)//1) - 2
    if required_fuel <= 0:
        return 0
    return calculate(required_fuel) + required_fuel

total = 0
for input in inputs.readlines():
    total += calculate(int(input))

print(int(total))
