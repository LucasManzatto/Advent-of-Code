import copy
import time
import itertools

input_array = list(map(int, open("input.txt", "r").readline().split(",")))
input_array += [0]*10000

SUM = 1
MULTIPLY = 2
SET = 3
OUTPUT = 4
JUMP_IF_NOT_NULL = 5
JUMP_IF_NULL = 6
RELATIVE_BASE_OFFSET = 9

POSITION_MODE = 0
VALUE_MODE = 1
RELATIVE_MODE = 2


def get_value(parameter_mode, array, position, relative_base=0):
    parameter_mode = int(parameter_mode)
    if parameter_mode == POSITION_MODE:
        return array[array[position]]
    elif parameter_mode == VALUE_MODE:
        return array[position]
    elif parameter_mode == RELATIVE_MODE:
        return array[array[position] + relative_base]
    return -1


def program(array, input=0, phase_input=0, debug=False, phase=False):
    position = 0
    output = 0
    relative_base = 0
    while (array[position] != 99):
        instruction = str(array[position]).zfill(5)
        third_parameter_mode, second_parameter_mode, first_parameter_mode, _, op = instruction
        first_arg = get_value(first_parameter_mode, array,
                              position + 1, relative_base)
        first_parameter_mode = int(first_parameter_mode)
        second_parameter_mode = int(second_parameter_mode)
        third_parameter_mode = int(third_parameter_mode)
        op = int(op)
        if op not in [3, 4, 9]:
            second_arg = get_value(second_parameter_mode,
                                   array, position + 2, relative_base)
        if op in [1, 2]:
            save_pos = array[position+3]
            array[save_pos] = first_arg + \
                second_arg if op == 1 else first_arg * second_arg
            position += 4
        elif op == 3:
            save_pos = 0
            if first_parameter_mode == POSITION_MODE:
                save_pos = array[position + 1]
            elif first_parameter_mode == VALUE_MODE:
                save_pos = position + 1
            elif first_parameter_mode == RELATIVE_MODE:
                save_pos = array[position + 1] + relative_base
            array[save_pos] = phase_input if phase else input
            phase = False
            position += 2
        elif op == 4:
            output = first_arg
            print(output)
            position += 2
        elif op in [5, 6]:
            position = second_arg if (first_arg != 0 and op == 5) or (
                first_arg == 0 and op == 6) else position + 3
        elif op in [7, 8]:
            save_pos = array[position+3]
            array[save_pos] = int(first_arg < second_arg) if op == 7 else int(
                first_arg == second_arg)
            position += 4
        elif op == RELATIVE_BASE_OFFSET:
            relative_base += array[position + 1]
            position += 2
    return output


print(program(input_array, input=1))
