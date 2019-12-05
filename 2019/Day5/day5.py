import copy
import time

input_array = list(map(int, open("input.txt", "r").readline().split(",")))


def get_value(parameter_mode, array, position):
    return array[array[position]] if int(parameter_mode) == 0 else array[position]


def calculate(array):
    position = 0
    input = 5
    while (array[position] != 99):
        instruction = str(array[position]).zfill(5)
        third_parameter_mode, second_parameter_mode, first_parameter_mode, _, op = instruction
        first_arg = get_value(first_parameter_mode, array, position + 1)
        second_arg = get_value(second_parameter_mode, array, position + 2)
        save_pos = array[position+3]
        op = int(op)
        if op in [1, 2]:
            array[save_pos] = first_arg + \
                second_arg if op == 1 else first_arg * second_arg
            position += 4
        elif op == 3:
            array[array[1]] = input
            position += 2
        elif op == 4:
            print(f"OP 4: Output Value:{array[array[position+1]]}")
            position += 2
        elif op in [5, 6]:
            position = second_arg if (first_arg != 0 and op == 5) or (
                first_arg == 0 and op == 6) else position + 3
        elif op in [7, 8]:
            array[save_pos] = first_arg < second_arg if op == 7 else first_arg == second_arg
            position += 4

calculate(input_array)
