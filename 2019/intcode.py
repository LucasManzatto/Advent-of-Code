import copy
import time
import itertools
from enum import Enum,IntEnum


class Op(IntEnum):
    SUM = 1
    MULTIPLY = 2
    SET = 3
    OUTPUT = 4
    JUMP_IF_NOT_NULL = 5
    JUMP_IF_NULL = 6
    SET_IF_LESS = 7
    SET_IF_EQUALS = 8
    SET_RELATIVE_BASE_OFFSET = 9
    STOP = 99


class Mode(IntEnum):
    POSITION = 0
    VALUE = 1
    RELATIVE = 2


def get_memory(file):
    set_memory = {k: v for k, v in enumerate(
        list(map(int, open(file).readline().split(','))))}
    return set_memory


def get_by_position(memory, position, relative_base=0):
    position = memory.get(position, 0) + relative_base
    value = memory.get(position, 0)
    return value


def get_by_value(memory, position):
    return memory.get(position, 0)


def get_by_relative_pos(memory, position, relative_base):
    position = memory.get(position, 0) + relative_base
    return memory.get(position, 0)


def get_by_relative_address(memory, position, relative_base):
    return memory.get(position, 0) + relative_base


def get_argument(parameter_mode, memory, position, relative_base=0, get_by_address=False):
    argument = -1
    if parameter_mode == Mode.POSITION:
        argument = get_by_position(memory, position)
    elif parameter_mode == Mode.VALUE:
        argument = get_by_value(memory, position)
    elif parameter_mode == Mode.RELATIVE:
        argument = get_by_relative_address(
            memory, position, relative_base) if get_by_address else get_by_relative_pos(memory, position, relative_base)
    return argument


def get_parameters(instruction):
    op = Op(int(instruction[-2:]))
    first_mode = Mode(int(instruction[-3:-2]))
    second_mode = Mode(int(instruction[-4:-3]))
    third_mode = Mode(int(instruction[-5:-4]))
    if third_mode == Mode.POSITION:
        third_mode = Mode.VALUE
    return op, first_mode, second_mode, third_mode


def decode_instruction(memory, position, relative_base):
    instruction = str(memory[position]).zfill(5)
    op, first, second, third = get_parameters(instruction)
    first_arg = get_argument(first, memory, position + 1, relative_base)
    second_arg = get_argument(second, memory, position + 2, relative_base)
    if op == Op.SET:
        address = get_argument(first, memory, position + 1,
                               relative_base, get_by_address=True)
    else:
        address = get_argument(third, memory, position + 3,
                               relative_base, get_by_address=True)
    return op, first_arg, second_arg, address


def program(file, program_input=0, debug=False):
    memory = get_memory(file)
    relative_base = 0
    position = 0

    def run(output=[], program_input=0):
        nonlocal position
        nonlocal relative_base
        nonlocal memory
        stop = False
        pause = False
        op, first_arg, second_arg, address = decode_instruction(
            memory, position, relative_base)
        if op == Op.SUM:
            memory[address] = first_arg + second_arg
            position += 4
        if op == Op.MULTIPLY:
            memory[address] = first_arg * second_arg
            position += 4
        elif op == Op.SET:
            memory[address] = program_input
            position += 2
        elif op == Op.OUTPUT:
            output.append(first_arg)
            if len(output) == 3:
                pause = True
            position += 2
        elif op == Op.JUMP_IF_NOT_NULL:
            position = second_arg if first_arg != 0 else position + 3
        elif op == Op.JUMP_IF_NULL:
            position = second_arg if first_arg == 0 else position + 3
        elif op == Op.SET_IF_LESS:
            memory[address] = int(first_arg < second_arg)
            position += 4
        elif op == Op.SET_IF_EQUALS:
            memory[address] = int(first_arg == second_arg)
            position += 4
        elif op == Op.SET_RELATIVE_BASE_OFFSET:
            relative_base += first_arg
            position += 2
        elif op == Op.STOP:
            pause = True
            stop = True
        return output, stop, pause
    return run


def test():
    run = program('test_intcode.txt', program_input=1)
    stop = False
    while not stop:
        output, stop, _ = run(program_input=1)
    print(output)