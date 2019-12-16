import copy
import time
import itertools

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

def get_memory(file):
    set_memory = {k:v for k,v in enumerate(list(map(int, open(file).readline().split(','))))}
    return set_memory

def get_by_position(memory, position):
    position = memory.get(position,0)
    value = memory.get(position,0)
    return value

def get_by_value(memory, position):
    return memory.get(position,0)


def get_by_relative_pos(memory, position, relative_base):
    return memory.get(memory.get(position,0) + relative_base,0)

def get_by_relative_address(memory, position, relative_base):
        return memory.get(position,0) + relative_base


def get_argument(parameter_mode, memory, position, relative_base=0,get_by_address=False):
    assert parameter_mode in [POSITION_MODE, VALUE_MODE,
                              RELATIVE_MODE], f"Invalid parameter mode {parameter_mode}"
    argument = -1
    if parameter_mode == POSITION_MODE:
        argument = get_by_position(memory, position)
    elif parameter_mode == VALUE_MODE:
        argument = get_by_value(memory, position)
    elif parameter_mode == RELATIVE_MODE:
        argument = get_by_relative_address(memory, position, relative_base) if get_by_address else get_by_relative_pos(memory, position, relative_base)
    return argument

def get_parameters(instruction):
    op = int(instruction[-2:])
    first_mode = int(instruction[-3:-2])
    second_mode = int(instruction[-4:-3])
    third_mode = int(instruction[-5:-4])
    if third_mode == 0:
        third_mode = 1
    return op, first_mode, second_mode, third_mode


def decode_instruction(memory, position, relative_base):
    instruction = str(memory[position]).zfill(5)
    op,first_parameter_mode,second_parameter_mode,third_parameter_mode = get_parameters(instruction)
    first_arg = get_argument(first_parameter_mode, memory,
                                   position + 1, relative_base)
    second_arg = get_argument(second_parameter_mode,
                                     memory, position + 2, relative_base)
    address = get_argument(
        third_parameter_mode, memory, position + 3, relative_base,get_by_address=True)
    return op, first_arg, second_arg, address


def program(memory, program_input=0, debug=False):
    relative_base = 0
    position = 0
    stop = False
    def run(program_input,output):
        nonlocal position
        nonlocal relative_base
        nonlocal memory
        nonlocal stop
        pause = False
        op, first_arg, second_arg, address = decode_instruction(
            memory, position, relative_base)
        if op == 1:
            memory[address] = first_arg + second_arg
            position += 4
        if op == 2:
            memory[address] = first_arg * second_arg
            position += 4   
        elif op == 3:
            memory[address] = program_input
            position += 2
        elif op == 4:
            output.append(first_arg)
            if len(output) == 2:
                pause = True
            position += 2
        elif op == 5:
            position = second_arg if first_arg != 0 else position + 3
        elif op == 6:
            position = second_arg if first_arg == 0 else position + 3
        elif op == 7:
            memory[address] = int(first_arg < second_arg)
            position += 4
        elif op == 8:
            memory[address] = int(first_arg == second_arg)
            position += 4
        elif op == 9:
            relative_base += first_arg
            position += 2
        elif op == 99:
            pause = True
            stop = True
        return output, stop, pause
    return run


# memory = get_memory('input_day9.txt')
# run = program(memory, program_input=1)
# stop = False
# while not stop:
#     output,stop = run(1,False)
# print(output)
