import re
input=open('input.txt').read().splitlines()

def find_orbit(obj,input):
    for objects in input:
        if(objects.count(f"{obj})")) == 1:
            second = objects.split(')')[1]
            return f"---{second}" + find_orbit(second,input[1:])
    return ""

letters = []
paths = []
for objects in input:
    first_object, second_object = objects.split(')')
    letters.append(second_object)
    orbit = f"{first_object}---{second_object}"
    orbit += find_orbit(second_object,input)
    if len([string for string in paths if orbit in string]) == 0:
        paths.append(orbit)

print(paths)

main_path = paths[0].split('---')
all_paths = [main_path]
for path in paths[1:]:
    path_array = path.split('---')
    for index,item in enumerate(main_path):
        if path_array[0] == item:
            all_paths.append([str(index+1)] + path_array[1:])

checksum = 0

for path in all_paths:
    try:
        base = int(path[0])
        path = path[1:]
        # print(f"{base},{checksum},{path}")
    except:
        base = 0
    for index,item in enumerate(path):
        # print(f"{item}:{base+ index}")
        checksum += (base + index)

# print(all_paths)
print(checksum)






