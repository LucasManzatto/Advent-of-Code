import copy

input = open("input.txt", "r")


def calculate(array):
    operations = array[::4]
    position = 0
    while (array[position] != 99):
        op = array[position]
        first_arg = array[array[position+1]]
        second_arg = array[array[position+2]]
        save_pos = array[position+3]
        value = first_arg + second_arg if op == 1 else first_arg * second_arg
        array[save_pos] = value
        position += 4
    return array[0]


input_array = list(map(int, input.readline().split(",")))
answer = 19690720


def binary_search(array, low, high, result):
    if(low >= high):
        return 0
    mid = (low + (high - 1))//2
    input_array_copy = copy.copy(array)
    input_array_copy[1] = mid
    input_array_copy[2] = 0
    result = calculate(input_array_copy)
    verb = answer - result
    if 0 < verb < 99:
        return (mid, verb)
    if(result > answer):
        return binary_search(array, low, mid - 1, result)
    else:
        return binary_search(array, mid + 1, high, result)


print(binary_search(input_array, 0, 99, answer))
