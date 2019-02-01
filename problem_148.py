import math
import pandas
import multiprocessing

##PASCAL = {1: [1], 2: [1, 1]}
##
##def pascal(n):
##
##    try:
##        return PASCAL[n]
##
##    except KeyError:
##        
##        prev = pascal(n-1)
##        _pascal = [1]
##
##        for m in range(1, n-1):
##            _pascal.append(prev[m-1] + prev[m])
##
##        _pascal.append(1)
##
##        PASCAL[n] = _pascal
##
##        return _pascal
##
##def pascal_sevens(row):
##    _pascal = pascal(row)
##    return row, sum([1 for p in _pascal if p % 7 == 0])

F = {}

def formula(n):

    try:
        return F[n]

    except KeyError:

        if n % 1e5 == 0: print(int(n/1e5))

        if n < 7:
            F[n] = 0
            return 0

        p = int(math.log(n)/math.log(7)) 

        p7 = 7**p
        m = int(n/p7)
        mod = n % p7

        val = (p7- mod - 1)*m + formula(mod)*(1+m)

        if n < 3e7:
            F[n] = val

        return val

N = int(1e9)

import euler_tools

with euler_tools.Watch('formula'):
    print(sum(i-formula(i-1) for i in range(1, int(N)+1)))


