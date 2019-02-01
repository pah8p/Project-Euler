


import collections

N = collections.defaultdict(list)

MAX = 5000

CEIL = 100

##for i in range(1, MAX):
##    print(i)
##    for j in range(i+1, MAX):
##        n = (i+j)*(i-j)
##        N[n].append((n, i, j))
##
##print(sum([1 for k, v in N.items() if len(v) == 1 and k < CEIL]))
##
##for k, v in N.items():
##    if k < CEIL and len(v) == 1:
##        print(k, v)

def sieve(n):
    _sieve = []
    for i in range(2, n):
        _sieve.append([])
    for i in range(2, n):
        j = 1
        while True:

            if i*j < n:
                _sieve[i*j-2].append(i)
                j += 1

            else:
                break
            
    return _sieve

def num_ways(n, sieve):

    factors = sieve[n-2]
    factors = factors[:-1]
    #print(factors)

    _n = 0
    for i in range(int(len(factors)/2)):
        a = factors[i]
        b = factors[-(i+1)]
        #print(a, b)
        bb = (a+b)/2
        aa = a-bb

        bbb=bb/2
        aaa=aa-3*bb

        if n == 20: print(n, _n, a, b, aa, bb, aaa, bbb)
        
        if aa > 0 and (aa+bb) > 0 and (aa+2*bb) > 0:
        
            if a % 2 == 0 and b % 2 == 0:
                _n+=1
                print(n, _n, a, b, aa, bb)
            elif a % 2 == 1 and b % 2 == 1:
                print(n, _n, a, b, aa, bb)
                _n+=1
    return _n



import euler_tools
with euler_tools.Watch():
    s = sieve(101)
    singles = [1 for i in range(1, 100) if num_ways(i, s)==1]
    print(sum(singles))

    
    #print(sum([1 for i in range(2, 5000000) if num_ways(i) == 1]))

