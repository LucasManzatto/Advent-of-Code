import functools
import time
from collections import Counter
import itertools

input = open('input.txt', 'r').readlines()

total = 0
twice = 0
list = {0}
for number in itertools.cycle(map(int, input)):
    total += number
    if total in list:
        print(total)
        break
    list.add(total)

result = functools.reduce(lambda a, b: a + b, map(int, input))
print(result)
