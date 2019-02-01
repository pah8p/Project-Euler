
import itertools

WAYS = {}

def ways(target, value):

    try:
        return WAYS[(target, value)]

    except KeyError:

        if value == 1:
            #print(1, target)
            r = 1

        else:
            s = 0
            top = int(target/value) + 1
            for n in range(0, top):
                remainder = target - value*n
                w = ways(remainder, value -1)
                s += w
                #print(top, remainder, w)
                    
            r = s

        WAYS[(target, value)] = r

        return r

def ways2(target, value):
    ways = [1]
    for i in range(1, value):
        for j in range(value, target):
            ways[j] += ways[j-i]
    return ways[target]

import euler_tools

with euler_tools.Watch():
    print(ways(100, 100))

with euler_tools.Watch():
    print(ways2(100, 100))

#for i in range(1,10):
#        print('ways', i, ways(i, i))
