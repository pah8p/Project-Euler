
import math

def max_key_by_val(dct):
    max_v = 0
    max_k = None
    for k, v in dct.items():
        if v > max_v:
            max_v, max_k = v, k
    return max_k
            
res = {}

for p in range(1, 1001):
    res[p] = 0
    
    for a in range(1, int(p/2)):
        for b in range(1, p-a):

            c = p - a - b

            if (c**2 == a**2+b**2):
                res[p] += 1

                #print('%s %s %s' % (a, b, c))

print(res)

print(max_key_by_val(res))
