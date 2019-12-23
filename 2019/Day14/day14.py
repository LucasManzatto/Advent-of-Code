import re
import math
import itertools
inputs = open('input_test.txt').read().splitlines()


def flatten(A):
    rt = []
    for i in A:
        if isinstance(i, list):
            rt.extend(flatten(i))
        else:
            rt.append(i)
    return rt


def get_values(reaction):
    ammount, key = re.match(r"([0-9]+)([a-z]+)", reaction, re.I).groups()
    return int(ammount), key


def get_reactions(inputs):
    reactions = [x.replace(' ', '').split('=>') for x in inputs]
    reactions_dict = {}
    ore_reactions = []
    for x in reactions:
        reaction_value, reaction_name = x
        reaction_value = reaction_value.split(',')
        value, key = get_values(reaction_name)
        if "ORE" in reaction_value[0]:
            ore_reactions.append(key)
        reaction_value.insert(0, int(value))
        reactions_dict[key] = reaction_value
    return reactions_dict, ore_reactions


reactions, ore_reactions = get_reactions(inputs)

# print(reactions, ore_reactions)

fuel_reactions = list(filter(lambda x: 'FUEL' in x, inputs))[0]
fuel_reactions = fuel_reactions.replace(' ', '').split('=>')[0].split(',')

print(fuel_reactions)
# while 1:
#     flattened_reactions = []
#     for index, fuel_reaction in enumerate(fuel_reactions):
#         fuel_reaction_ammount, key = get_values(fuel_reaction)
#         react = reactions.get(key)
#         ammount = react[0]
#         reacts = react[1:]

#         if "ORE" not in reacts[0]:
#             times_needed = math.ceil(fuel_reaction_ammount / ammount)
#             for i, reaction in enumerate(reacts):
#                 reaction_ammount, key = get_values(reaction)
#                 new_value = times_needed * reaction_ammount
#                 reacts[i] = str(new_value) + key
#             flattened_reactions.append(reacts)
#         else:
#             flattened_reactions.append(fuel_reaction)
#     print(flattened_reactions)
#     print('\n')

#     if flattened_reactions == fuel_reactions:
#         break
#     fuel_reactions = flattened_reactions
#     fuel_reactions = flatten(fuel_reactions)

# total_ore = 0
# for ore_react in ore_reactions:
#     total = 0
#     for reaction in fuel_reactions:
#         reaction_ammount, key = get_values(reaction)
#         if key == ore_react:
#             total += reaction_ammount
#     ore = reactions.get(ore_react)
#     times_needed = math.ceil(total / ore[0])
#     print(f'Total:{total},Times needed:{times_needed}, Ore:{ore},Reaction:{ore_react}')
#     ore_value, _ = get_values(ore[1])
#     result = times_needed * ore_value
#     total_ore += result

print(fuel_reactions)
# print(total_ore)
