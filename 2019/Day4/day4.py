import re
import time
min = 372304
max = 847060
real_min = 377778
real_max = 800000

range_array = list(map(str, range(real_min, real_max)))

init_time = time.time()
regex_sequence = re.compile(r'^3*4*5*6*7*8*9*$')

sequence = list(filter(regex_sequence.search, range_array))

def check(item):
    first, second, third, forth, fifth, sixth = item
    if (first == second != third or 
        first != second == third != forth or
        second != third == forth != fifth or
        third != forth == fifth != sixth or
        forth != fifth == sixth):
        return item

matches = list(filter(check,sequence))

print(len(matches))