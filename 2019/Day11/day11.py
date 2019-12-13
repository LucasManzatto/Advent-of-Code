from day9 import program
from collections import namedtuple
from enum import Enum
Coordinates = namedtuple('Coordinates', 'x y')
Robot = namedtuple('Robot', 'position direction')


class Direction(Enum):
    UP = 1
    RIGHT = 2
    LEFT = 3
    DOWN = 4


turn_left = {
    Direction.UP: Direction.LEFT,
    Direction.RIGHT: Direction.UP,
    Direction.DOWN: Direction.RIGHT,
    Direction.LEFT: Direction.DOWN
}

turn_right = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP
}

move = {
    Direction.UP: (1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (-1, 0),
    Direction.LEFT: (0, -1)
}


# def print_space(painted, robot_position, robot_direction):
#     for y in range(3, -3, -1):
#         line = ""
#         for x in range(-3, 3):
#             if (x, y) == robot_position:
#                 line += directions[robot_direction]
#             elif (x, y) in painted:
#                 line += colors[painted[(x, y)]]
#             else:
#                 line += "."
#         print(line)
# colors = {"White": "#", "Black": "."}

def move_robot(direction,x,y):
    moves = move[direction]
    x += moves[0]
    y += moves[1]
    return x,y

directions = {Direction.UP: "^", Direction.RIGHT: ">",
              Direction.LEFT: "<", Direction.DOWN: "V"}


memory = list(map(int, open('input.txt').readline().split(',')))

painted = {(0, 0): 0}
x = 0
y = 0
robot_direction = Direction.UP
current_color = 1
run = program(memory, current_color)
stop = False
pause = False
output = []

while 1:
    (output, pause, stop) = run(current_color, output, pause)
    if stop:
        break
    if pause:
        color, turn_direction = output
        pause = False
        output = []
        painted[(x, y)] = color
        robot_direction = turn_left[robot_direction] if turn_direction == 0 else turn_right[robot_direction]
        x,y = move_robot(robot_direction,x,y)
        print(x,y)
        current_color = painted.get((x, y), 0)

print(len(painted))
pause