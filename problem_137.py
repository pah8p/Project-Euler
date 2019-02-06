
import pell_equation
from decimal import Decimal

#print(pell_equation.continued_fraction(5**0.5))

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

def phi(n):
    cf = [1]*(n+1)
    return Decimal(h(n, cf))/Decimal(k(n, cf))

def a(x):
    return Decimal(x)/(1-Decimal(x)-Decimal(x)**2)

# for i in range(16):
#     j = 2*i
#     x = (phi(j)-1)
#     y = a(x)
#     print(i, j, x, y)
