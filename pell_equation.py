import math
import decimal
from decimal import Decimal

decimal.getcontext().prec = 50

def continued_fraction(n):
    i = 0
    a = []
    while i < 30:
        a.append(math.floor(Decimal(n)))
        diff = Decimal(n) - math.floor(Decimal(n))
        if diff == 0:
            break
        n = Decimal(1.0)/Decimal(diff)
        i += 1
    return a

def h(n, a):
    if n == 0:
        return a[0]
    elif n == 1:
        return a[1]*a[0] + 1
    else:
        return a[n]*h(n-1, a) + h(n-2, a)

def k(n, a):
    if n == 0:
        return 1
    elif n == 1:
        return a[1]
    else:
        return a[n]*k(n-1, a) + k(n-2, a)
        
def first_solution(d):
    n = 0
    a = continued_fraction(Decimal(d).sqrt())
    if math.sqrt(d).is_integer():
        return (0, 0, d, 0)
    #print(a)
    while n < 100:
        x = h(n, a)
        y = k(n, a)
        if x == Decimal(-1+d*y**2).sqrt():
            return (x, y, d, n)
        n += 1
        if n == 100:
            raise Exception
        #print(n)
    return None

def solve(d, num_solutions=10):
    solutions = []
    x_1, y_1, d, n = first_solution(d)
    for n in range(num_solutions):
        if n == 0:
            s = (x_1, y_1)
        else:
            s = (
                x_1*solutions[n-1][0] + d*y_1*solutions[n-1][1],
                x_1*solutions[n-1][1] + y_1*solutions[n-1][0]
            )
        solutions.append(s)
    return solutions
            
    

#print(solve(3))

#res = [solve(d) for d in ds]
#print(max(res, key=lambda x: x[0]))

#print(continued_fraction(math.sqrt(661)))

#print(solve(778))

