import copy
import itertools

def load_sets():
    file = 'p105_sets.txt'
    with open(file, 'r') as f:
        sets = f.readlines()

    print(sets)
    return [[int(s) for s in _s.split(',')] for _s in sets]

def generate_subsets(s):
    subsets = []
    for i in range(len(s)):
        subset = itertools.combinations(s, i+1)
        for _subset in subset:
            subsets.append(_subset)
    return subsets

    
def check_set(s):
    subsets = generate_subsets(s)
    for i in range(len(subsets)):
        for j in range(i+1, len(subsets)):

            s_i = sum(subsets[i])
            s_j = sum(subsets[j])

            if s_i == s_j:
                #print(subsets[i], subsets[j], s_i, s_j)
                return 0

            l_i = len(subsets[i])
            l_j = len(subsets[j])

            if l_i > l_j and s_i < s_j:
                #print(subsets[i], l_i, s_i, subsets[j], l_j, s_j)
                return 0
            elif l_j > l_i and s_j < s_i:
                #print(subsets[i], l_i, s_i, subsets[j], l_j, s_j)
                return 0

    return sum(s)

sets = load_sets()
print(sets)

import euler_tools

with euler_tools.Watch():
    print(sum([check_set(s) for s in sets]))
