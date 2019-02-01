import math

def quadratic(a, b, c):
    det = math.sqrt(b**2-4*a*c)
    if (-b+det)/(2*a) > 0:
        return (-b+det)/(2*a)
    else:
        return (-b-det)/(2*a)

def triangle(n):
    return n*(n+1)/2

def pentagon(n):
    return n*(3*n-1)/2

def hexagon(n):
    return n*(2*n-1)

def is_int(n):
    return n==int(n)

for z in range(143, 100000):
    y = quadratic(-3, 1, 4*z**2-2*z)
    x = quadratic(1, 1, y-3*y**2)

    if is_int(x) and is_int(y):

        print('%s %s %s %s' % (x, y, z, triangle(x)))
