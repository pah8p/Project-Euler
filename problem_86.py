import pell_equation
from decimal import Decimal

def quadratic(a, b, c):
    return float((-b+Decimal(b**2-4*a*c).sqrt())/(2*a))

def distance_pell(h, w, d):
    a = h**2-d**2
    b = 2*w*d**2
    c = -d**2*w**2
    d = a/c

def distance(h, w, d):
    a = h**2-d**2
    b = 2*w*d**2
    c = -d**2*w**2
    if h == d:
        x = w/2
    else:
        x = quadratic(a, b, c)
    length = Decimal(h**2+(w-x)**2).sqrt() + Decimal(x**2+d**2).sqrt()


    A = x**2*(h**2-d**2)
    B = 2*w*d**2*x
    C = -d**2*w**2
    print(A+B+C)
    print(a*x**2+b*x+c)

    
    return float(length), x

print(distance(3, 6, 5))

##s = 0
##for w in range(1, 101):
##    for h in range(1, 101):
##        for d in range(1, 101):
##
##
##            length, x = distance(h, w, d)
##            
##            if length.is_integer():
##                print(length, x, h, w, d)
##                s += 1
##
##print(s)
