import re
import functools
inputs = open('input.txt').read().splitlines()

total_len = 0
total_memory_len = 0


def part1():
    total_len = sum(len(s) - len(eval(s)) for s in inputs)
    print(total_len)


def part2():
    total_len = sum(len(s) + 2 * s.count('"') + 2* s.count("\\") - len(s) for s in inputs)
    print(total_len)


a = '"nbydghkfvmq\\\xe0\"lfsrsvlsj\"i\x61liif"'
a= '\\'
print(len(a))
a = str(a.encode())
print(a.count("\\") + a.count('"'))
part1()
part2()
