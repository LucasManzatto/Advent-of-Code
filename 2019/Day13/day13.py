import functools
import itertools
import random
import os
import sys
sys.path.insert(0,'..')
import intcode


tiles = {
    0: ' ',
    1: '|',
    2: '⬜',
    3: '➖',
    4: '⚪'
}

run = intcode.program('input.txt')

def print_game(board):
    width = max([k[0] for k in board]) + 1
    height = max([k[1] for k in board]) + 1
    print_board = {(elem[0],elem[1]):elem[2] for elem in board}
    for col in range(height):
        line = ""
        for row in range(width):
            line += tiles[print_board.get((row,col),0)]
        print(line)
    os.system('cls')

stop = False
pause = False
output = []
full_output = []
direction = 0
score = 0
ball = None
paddle = None

while not stop:
    while not pause:
        output, stop, pause = run(output, direction)
    if stop:
        break
    # x,y == (-1,0) is the score
    if output[0:2] == [-1, 0]:
        score = output[2]
    elif output[2] == 4:
        ball = output[0:2]
    if output[2] == 3:
        paddle = output[0:2]

    full_output.append(output)
    pause = False
    output = []
    if ball and paddle:
        direction = 0
        if paddle[0] < ball[0]:
            direction = 1
        elif paddle[0] > ball[0]:
            direction = -1

print(score)
def part1():
    blocks = functools.reduce(lambda a, b: a + int(b[2] == 2), full_output, 0)
    print(blocks)
