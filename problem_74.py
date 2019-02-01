

FACT = {}

def fact(n):
    try:
        return FACT[n]
    except KeyError:
        if n == 1 or n == 0:
            r = 1
        else:
            r = n*fact(n-1)
        FACT[n] = r
        return r

def fact_sum(n):
    return sum([fact(int(m)) for m in str(n)])

CHAINS = {}

def chain(n):
    orig_n = n
    seen = []
    i = 1
    while i < 61:
    
        n = fact_sum(n)
        
        if n in seen:
            r = len(seen)
            break

        seen.append(n)
        i += 1
        
##        try:
##            r = i + 1 + CHAINS[n]
##            print(orig_n, i+1, n, CHAINS[n])
##            break
##
##        except KeyError:
##            i += 1

    CHAINS[orig_n] = r
    return r

testers = [
    145, 169, 871, 872, 69, 78, 540
    #540
    #145
]
import euler_tools
with euler_tools.Watch():
    for i in range(1, int(1e6)): chain(i)

import collections
counts = collections.defaultdict(int)
for k, v in CHAINS.items():
    if v > 55:
        counts[v] += 1

print(counts)
