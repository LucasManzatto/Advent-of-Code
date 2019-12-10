import copy
import time
import itertools

input_memory = list(map(int, open("input.txt", "r").readline().split(",")))
input_memory += [0]*10000

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


def is_pos_in_memory(memory, position):
    return position >= 0 and position <= len(memory)


def get_by_position(memory, position):
    if is_pos_in_memory(memory, position):
        position = memory[position]
        if is_pos_in_memory(memory, position):
            return memory[position]
        else:
            return 0
    else:
        return 0


def get_by_value(memory, position):
    return memory[position] if is_pos_in_memory(memory, position) else 0


def get_by_relative_pos(memory, position, relative_base):
    if is_pos_in_memory(memory, position):
        position = memory[position] + relative_base
        return memory[position]
    else:
        return 0


def get_by_relative_address(memory, position, relative_base):
    if is_pos_in_memory(memory, position):
        return memory[position] + relative_base
    else:
        return 0


def get_first_argument(parameter_mode, memory, position, relative_base=0):
    parameter_mode = int(parameter_mode)
    assert parameter_mode in [POSITION_MODE, VALUE_MODE,
                              RELATIVE_MODE], f"Invalid parameter mode {parameter_mode}"
    argument = -1
    if parameter_mode == POSITION_MODE:
        argument = get_by_position(memory, position)
    elif parameter_mode == VALUE_MODE:
        argument = get_by_value(memory, position)
    elif parameter_mode == RELATIVE_MODE:
        argument = get_by_relative_pos(memory, position, relative_base)
    return argument


def get_second_argument(parameter_mode, memory, position, relative_base=0):
    parameter_mode = int(parameter_mode)
    argument = -1
    assert parameter_mode in [POSITION_MODE, VALUE_MODE,
                              RELATIVE_MODE], f"Invalid parameter mode {parameter_mode}"
    if parameter_mode == POSITION_MODE:
        argument = get_by_position(memory, position)
    elif parameter_mode == VALUE_MODE:
        argument = get_by_value(memory, position)
    elif parameter_mode == RELATIVE_MODE:
        argument = get_by_relative_pos(memory, position, relative_base)
    return argument


def get_save_pos(parameter_mode, memory, position, relative_base=0):
    parameter_mode = int(parameter_mode)
    assert position <= len(memory), ""
    assert parameter_mode in [
        VALUE_MODE, RELATIVE_MODE], f"Invalid parameter mode {parameter_mode}"
    if parameter_mode == VALUE_MODE:
        return get_by_value(memory, position)
    elif parameter_mode == RELATIVE_MODE:
        return get_by_relative_address(memory, position, relative_base)


def get_value(parameter_mode, memory, position, relative_base=0):
    parameter_mode = int(parameter_mode)
    if parameter_mode == POSITION_MODE:
        return memory[memory[position]]
    elif parameter_mode == VALUE_MODE:
        return memory[position]
    elif parameter_mode == RELATIVE_MODE:
        return memory[memory[position] + relative_base]
    return -1


def decode_instruction(instruction):
    instruction = str(instruction).zfill(5)
    op = int(instruction[-2:])
    first_parameter_mode = int(instruction[-3:-2])
    second_parameter_mode = int(instruction[-4:-3])
    third_parameter_mode =  int(instruction[-5:-4])
    if third_parameter_mode == 0:
        third_parameter_mode = 1
    return (op, first_parameter_mode, second_parameter_mode, third_parameter_mode)


def program(memory, input=0, phase_input=0, debug=False, phase=False):
    position = 0
    output = 0
    relative_base = 0
    while 1:
        op, first_parameter_mode, second_parameter_mode, third_parameter_mode = decode_instruction(
            memory[position])
        first_arg = get_first_argument(first_parameter_mode, memory,
                                       position + 1, relative_base)
        second_arg = get_second_argument(second_parameter_mode,
                                         memory, position + 2, relative_base)
        save_pos = get_save_pos(
            third_parameter_mode, memory, position + 3, relative_base)
        if op in [1, 2]:
            value = first_arg + second_arg if op == 1 else first_arg * second_arg
            memory[save_pos] = value
            position += 4
        elif op == 3:
            memory[save_pos] = phase_input if phase else input
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
            memory[save_pos] = int(first_arg < second_arg) if op == 7 else int(
                first_arg == second_arg)
            position += 4
        elif op == 9:
            relative_base += first_arg
            position += 2
        elif op == 99:
            return output


program(input_memory, input=1)
