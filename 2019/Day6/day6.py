import re
input = open('input.txt').read().splitlines()

orbits = {}
for line in input:
    first_object, second_object = line.split(')')
    orbits[second_object] = first_object


def get_path(path_end,orbits,path_beginning='COM'):
    path = []
    while orbits.get(path_end) != path_beginning:
            path_end = orbits.get(path_end)
            path.append(path_end)
    return path

san_path_to_com = get_path('SAN',orbits)
my_path_to_com = get_path('YOU',orbits)

first_intersection = [value for value in my_path_to_com if value in san_path_to_com][0] 
num_of_moves = san_path_to_com.index(first_intersection) + my_path_to_com.index(first_intersection)

total = 0
for obj in orbits.keys():
    path_end = obj
    while path_end != "COM":
        path_end = orbits.get(path_end)
        total += 1

print(total,num_of_moves)
