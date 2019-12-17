import intcode
import functools
import itertools
import random

tiles = {
    0: ' ',
    1: '|',
    2: '⬜',
    3: '➖',
    4: '⚪'
}

run = intcode.program('input.txt')


def chunks(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]


stop = pause = False
output = []
full_output = []
direction = 0
rand = [0,1,-1]
while not stop:
    while not pause:
        output, stop, pause = run(output,random.choice(rand))
    if stop:
        break
    full_output.append(output)
    pause = False
    output = []

# intcode.test()
# part 1
blocks = functools.reduce(lambda a, b: a + int(b[2] == 2), full_output, 0)
scores = list(filter(lambda x: x[0] == -1 and x[1] == 0, full_output))
balls = list(filter(lambda x: x[2] == 4, full_output))
paddles = list(filter(lambda x: x[2] == 3, full_output))


lines = list(chunks(full_output,38))
for line in lines:
    str_line=""
    for elem in line:
        str_line += tiles[elem[2]]
    print(str_line)
# print(lines[0])
print(full_output)
print(blocks)
# print(scores)
print(paddles)
