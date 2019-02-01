from decimal import Decimal

##def ways1(target, index):
##    PRIMES = list(range(1, index+1))
##    ways = [1] + [0]*(target)
##    for i in range(index):
##        for j in range(PRIMES[i], target+1):
##            #print(i, PRIMES[i])
##            ways[j] += ways[j-PRIMES[i]]
##    return ways[target]

def pentagon(n):
    return int((3*n**2-n)/2)

P = [1, 1]

def partition(n):
    try:
        return P[n]
    except IndexError:
        i = 1
        k = 0
        p = 0
        while n-k >= 0:

            k = pentagon(i)

            if n-k >= 0:                
                sign = (-1)**(abs(i)-1)
                p = p + sign*partition(n-k)

            if i > 0:
                i = -i
            elif i < 0:
                i = -i + 1
            else:
                i += 1
    
        P.append(p)
        return p

def ways(target, index):
    w = [1] + [0]*(target)
    for i in range(1, index+1):
        for j in range(i, target+1):
            #print(i, j, j-i)
            w[j] += w[j-i]
    return w[target]


def divisible_by(n):
    i = 1
    while True:

        m = partition(i)

        if str(m)[-6:] == '000000':
        #if m % 1e6 == 0:
            print(i, m)
            return None
        
        i += 1

        #if i % 10000 == 0:
        #    print(i, m)

import euler_tools

with euler_tools.Watch('abc'):

    partition(10)
    print(P)
    #print(ways(23000, 23000))
    print(divisible_by(1e6))
