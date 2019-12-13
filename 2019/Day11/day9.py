import copy
import time
import itertools

input_memory = list(map(int, open("input.txt", "r").readline().split(",")))

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
    return position >= 0 and position <= len(memory) - 1


def get_by_position(memory, position):
    try:
        if is_pos_in_memory(memory, position):
            position = memory[position]
            if is_pos_in_memory(memory, position):
                return memory[position]
            else:
                return 0
        else:
            return 0
    except:
        print(f'Error at position {position}')
        return 0


def get_by_value(memory, position):
    return memory[position] if is_pos_in_memory(memory, position) else 0


def get_by_relative_pos(memory, position, relative_base):
    if is_pos_in_memory(memory, position):
        position = memory[position] + relative_base
        try:
            return memory[position]
        except:
            print(f"Position:{position} exceeded memory size({len(memory)})")
    else:
        return 0


def get_by_relative_address(memory, position, relative_base):
    if is_pos_in_memory(memory, position):
        return memory[position] + relative_base
    else:
        return 0


def get_first_argument(parameter_mode, memory, position, relative_base=0):
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


def get_save_address(parameter_mode, memory, position, relative_base=0):
    parameter_mode = int(parameter_mode)
    assert position <= len(memory), "Position exceeded memory"
    assert parameter_mode in [
        VALUE_MODE, RELATIVE_MODE], f"Invalid parameter mode {parameter_mode}"
    if parameter_mode == VALUE_MODE:
        return get_by_value(memory, position)
    elif parameter_mode == RELATIVE_MODE:
        return get_by_relative_address(memory, position, relative_base)


def decode_instruction(instruction):
    instruction = str(instruction).zfill(5)
    op = int(instruction[-2:])
    first_parameter_mode = int(instruction[-3:-2])
    second_parameter_mode = int(instruction[-4:-3])
    third_parameter_mode = int(instruction[-5:-4])
    if third_parameter_mode == 0:
        third_parameter_mode = 1
    return (op, first_parameter_mode, second_parameter_mode, third_parameter_mode)


def program(memory, program_input=0, debug=False):
    memory += [0]*10000
    relative_base = 0
    position = 0
    pause = False
    stop = False

    def run(program_input, output,pause):
        nonlocal position
        nonlocal relative_base
        nonlocal memory
        nonlocal stop
        op, first_parameter_mode, second_parameter_mode, third_parameter_mode = decode_instruction(
            memory[position])
        first_arg = get_first_argument(first_parameter_mode, memory,
                                       position + 1, relative_base)
        second_arg = get_second_argument(second_parameter_mode,
                                         memory, position + 2, relative_base)
        address = get_save_address(
            third_parameter_mode, memory, position + 3, relative_base)
        if op in [1, 2]:
            value = first_arg + second_arg if op == 1 else first_arg * second_arg
            try:
                memory[address] = value
            except:
                print(f'Address:{address} exceeded memory size({len(memory)})')
            position += 4
        elif op == 3:
            memory[address] = program_input
            position += 2
        elif op == 4:
            output.append(first_arg)
            if len(output) == 2:
                pause = True
                stop = False
            position += 2
        elif op in [5, 6]:
            position = second_arg if (first_arg != 0 and op == 5) or (
                first_arg == 0 and op == 6) else position + 3
        elif op in [7, 8]:
            memory[address] = int(first_arg < second_arg) if op == 7 else int(
                first_arg == second_arg)
            position += 4
        elif op == 9:
            relative_base += first_arg
            position += 2
        elif op == 99:
            stop = True
        return output, pause, stop
    return run


# program(input_memory, input=1)
