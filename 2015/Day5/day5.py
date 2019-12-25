import re
import functools
inputs = open('input.txt').read().splitlines()


def part1():
    count = 0
    vowels = 'aeiou'
    for elem in inputs:
        total_vowels = functools.reduce(lambda a, b: a + elem.count(b), vowels, 0)
        if re.search(r'(\w)\1', elem) and total_vowels >= 3 and not re.search(r'(ab)|(cd)|(pq)|(xy)', elem):
            count += 1
    print(count)
