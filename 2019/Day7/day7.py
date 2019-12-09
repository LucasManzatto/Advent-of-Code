import copy
import time
import itertools

input_array = list(map(int, open("input.txt", "r").readline().split(",")))


def get_value(parameter_mode, array, position):
    return array[array[position]] if int(parameter_mode) == 0 else array[position]


def ampliflier(array, input=0, phase_input=0, debug=False):
    position = 0
    first = True
    output = 0
    while (array[position] != 99):
        instruction = str(array[position]).zfill(5)
        third_parameter_mode, second_parameter_mode, first_parameter_mode, _, op = instruction
        first_arg = get_value(first_parameter_mode, array, position + 1)
        op = int(op)
        if op not in [3, 4]:
            second_arg = get_value(second_parameter_mode, array, position + 2)
        if op in [1, 2]:
            save_pos = array[position+3]
            array[save_pos] = first_arg + \
                second_arg if op == 1 else first_arg * second_arg
            if debug:
                if op == 1:
                    print(
                        f'Saving {first_arg}({array[position+1]})+{second_arg} to position {save_pos}')
                if op == 2:
                    print(
                        f'Saving {first_arg}({array[position+1]})*{second_arg} to position {save_pos}')
            position += 4
        elif op == 3:
            array[array[position + 1]] = phase_input if first else input
            first = False
            position += 2
        elif op == 4:
            output = array[array[position+1]]
            if debug:
                print(
                    f"OP 4: Output Value:{output}, input:{input},phase:{phase_input}")
            position += 2
        elif op in [5, 6]:
            position = second_arg if (first_arg != 0 and op == 5) or (
                first_arg == 0 and op == 6) else position + 3
            if debug:
                if op == 5:
                    print(
                        f"OP 5: new position:{position},first arg:{first_arg},second arg:{second_arg}")
                else:
                    print(
                        f"OP 6: new position:{position},first arg:{first_arg}")
        elif op in [7, 8]:
            save_pos = array[position+3]
            array[save_pos] = first_arg < second_arg if op == 7 else first_arg == second_arg
            position += 4
    return output


def get_best_phase_sequence(phases, out=0):
    phases_permutations = list(itertools.permutations(phases))

    best = 0
    best_sequence =[]
    for phase_sequence in phases_permutations:
        output = out
        for phase in phase_sequence:
            output = ampliflier(input_array.copy(), output, phase)
            print(output)
        if output > best:
            best = output
            best_sequence = phase_sequence
    return (best,best_sequence)

def get_best_phase_sequence_feedback(phases, out=0):
    phases_permutations = list(itertools.permutations(phases))

    best = 0
    best_sequence =[]
    for phase_sequence in phases_permutations:
        output = out
        for phase in phase_sequence:
            output = ampliflier(input_array.copy(), output, phase)
            print(output)
        if output > best:
            best = output
            best_sequence = phase_sequence
    return (best,best_sequence)

best = get_best_phase_sequence([0,1,2,3,4])
print(best)
