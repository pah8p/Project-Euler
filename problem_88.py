import euler_tools
import itertools
import functools

##@functools.lru_cache(maxsize=256)
##def ways(target, value):
##
##    if value == 1:
##        r = [[1]*target]
##
##    else:
##
##        s = []
##        top = int(target/value) + 1
##        for n in range(0, top):
##            remainder = target - value*n
##            subways = ways(remainder, value -1)
##            for subway in subways:
##                s.append(n*[value] + subway)
##                 
##        r = s
##
##    return r

WAYS = {}

def ways(target, value):

    try:
        return WAYS[(target, value)]

    except KeyError:

        if value == 1:
            r = [[1]*target]

        else:

            s = []
            top = int(target/value) + 1
            for n in range(0, top):
                remainder = target - value*n
                subways = ways(remainder, value - 1)
                for subway in subways:
                    s.append(n*[value] + subway)
                     
            r = s

        #if target < 20:
        WAYS[(target, value)] = r

        return r

SPS = {}

def sums_products(target, value):

    try:
        return SPS[(target, value)]

    except KeyError:

        '''(sum, product, size)'''

        if value == 1:
            r = [(target, 1, target)]

        else:

            s = []
            top = int(target/value) + 1
            for n in range(0, top):
                remainder = target - value*n
                subways = sums_products(remainder, value - 1)
                for subway in subways:
                    s.append((
                        subway[0] + n*value,
                        subway[1] * value**n,
                        subway[2] + n,
                    ))

            r = s

        #if target < 20:
        SPS[(target, value)] = r

        return r

def product(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

def min_psm(n, k):
    psm = {}
    for i in range(2, n):
        with euler_tools.Watch(i):
            ways_to_sum = ways(i, i)
        for way_to_sum in ways_to_sum:

            if sum(way_to_sum) == product(way_to_sum):

                try:
                    curr_min = psm[len(way_to_sum)]['min']
                    if i < curr_min:
                        psm[len(way_to_sum)] = {
                            'min': i,
                            'way': way_to_sum,
                        }
                except KeyError:
                    psm[len(way_to_sum)] = {
                        'min': i,
                        'way': way_to_sum,
                    }

    mins = list()
    for key, val in psm.items():
        print(key, val)
        if 2 <= key <= k:
            mins.append(val['min'])

    return sum(set(mins)), max(psm.keys())


with euler_tools.Watch():
    #print(ways(5, 5))
    print(ways(5, 5))
    print(sums_products(12, 12))
##   psms = min_psm(50, 20)
##    print(psms)
##    for k, v in psms.items():
##        print(k, v['min'])
    
#for k in sorted(WAYS.keys()):
#    print(k)
    
