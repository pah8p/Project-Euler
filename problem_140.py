
import problem_137
from decimal import Decimal

def g(a, b):
    x = Decimal(a/b)-1
    return (Decimal(x)+3*Decimal(x)**2)/(1-Decimal(x)-Decimal(x)**2)

def iterate(a, b):
    return (Decimal(2*a+b), Decimal(a+b))

x1 = (3, 2)
x2 = (7, 5)

gs = []
for i in range(15):
    gs.append(g(*x2))
    x2 = iterate(*x2)
    gs.append(g(*x1))
    x1 = iterate(*x1)


print(len(gs))
for _g in gs: print(_g)

print(sum(gs))