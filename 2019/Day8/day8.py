import re
import sys
input = open('input.txt').read()
width = 25
height = 6
image_size = width * height


def chunks(array, size):
    return [array[i:i+size] for i in range(0, len(array), size)]


layers = chunks(input, image_size)

min_zeros = sys.maxsize
ans_part1 = 0
decoding = [2] * image_size

best_layer = min(layers, key=lambda layer: layer.count('0'))
ans_part1 = best_layer.count('2') * best_layer.count('1')

for layer in layers:
    for index, pixel in enumerate(layer):
        if int(pixel) != 2 and int(decoding[index]) == 2:
            decoding[index] = pixel

layers = chunks(decoding, width)
for layer in layers:
    print("".join(layer).replace('0', ' '))
