import re
import math
import itertools
inputs = open('input_test.txt').read().splitlines()

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

def get_values(reaction):
    return re.match(r"([0-9]+)([a-z]+)", reaction, re.I).groups()

def get_ore_reactions(inputs):
    reactions = [x.replace(' ', '').split('=>') for x in inputs]
    reactions_dict = {}
    for x in reactions:
        reaction_value, reaction_name = x
        reaction_value = reaction_value.split(',')
        value, key = get_values(reaction_name)
        reaction_value.insert(0,int(value))
        reactions_dict[key] = reaction_value
    return reactions_dict

reactions = get_ore_reactions(inputs)

print(reactions)

fuel_reactions = list(filter(lambda x: 'FUEL' in x, inputs))[0]
fuel_reactions = fuel_reactions.replace(' ', '').split('=>')[0].split(',')

for _ in range(3):
    for index,fuel_reaction in enumerate(fuel_reactions):
        value, key = get_values(fuel_reaction)
        react = reactions.get(key)
        if "ORE" not in react[1]:
            fuel_reactions[index] = react[1:]
            fuel_reactions = flatten(fuel_reactions)
        print(fuel_reactions)
    # for reaction in inputs:
    #     if "ORE" in reaction or "FUEL" in reaction:
    #         continue

print(fuel_reactions[0][-1])

