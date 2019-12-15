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
    Direction.UP: (0, 1),
    Direction.RIGHT: (1,0),
    Direction.DOWN: (0, -1),
    Direction.LEFT: (-1, 0)
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


set_memory = {k:v for k,v in enumerate(list(map(int, open('input.txt').readline().split(','))))}
painted = {(0, 0): 0}
x = 0
y = 0
robot_direction = Direction.UP
current_color = 0
run = program(set_memory)
stop = False
pause = False

while 1:
    color,_,op = run(current_color,pause)
    turn_direction,stop,_ = run(current_color,pause)
    str_turn = "Left" if turn_direction == 0 else "Right"
    curr_str_color = "White" if current_color == 1 else "Black"
    new_str_color = "White" if color == 1 else "Black"
    # print(f"Turn:{str_turn}")
    # print(f"Paint color:{new_str_color}")
    # print(f"Old Position:{x,y}, Robot Direction:{robot_direction},Color:{curr_str_color}")
    if stop:
        break

    painted[(x, y)] = color
    robot_direction = turn_left[robot_direction] if turn_direction == 0 else turn_right[robot_direction]
    x,y = move_robot(robot_direction,x,y)
    current_color = painted.get((x, y), 0)
    # str_color = "White" if current_color == 1 else "Black"
    # print(f"Old Position:{x,y}, Robot Direction:{robot_direction},Color:{str_color}\n")

print(painted)
print(len(painted))