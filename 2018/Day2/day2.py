import string
import difflib
import re

alphabet = string.ascii_lowercase
input = open('input.txt', 'r').read().splitlines()


def find_word(array):
    result = None
    for value in array:
        for value2 in array:
            matches = 0
            position = 0
            for i in range(len(value)):
                if(value[i] != value2[i]):
                    position = i
                    matches += 1
            if matches == 1:
                result = value[:position] + value[position+1:]
    return result

def find_checksum(array):
    two_count = 0
    three_count = 0
    for value in array:
        found_three = False
        found_two = False
        for letter in alphabet:
            if(value.count(letter) == 3 and not found_three):
                three_count += 1
                found_three = True
            elif(value.count(letter) == 2 and not found_two):
                two_count += 1
                found_two = True
            if found_two and found_three: break
    return two_count * three_count

print(find_checksum(input))

print(find_word(input))