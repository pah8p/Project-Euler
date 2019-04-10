
import euler_tools

def x_min(a, b, c):
    return (a*b*c-a**2*c)/(b**2-a**2)

def distance(a, b, c):

    x = x_min(a, b, c)
    return (a**2+x**2)**0.5 + ((c-x)**2+b**2)**0.5


def is_int(x):
    if x.is_integer():
        return True

    if x-int(x) > 0.9999:
        return True

    if x-int(x) < 0.0001:
        return True

    return False

def min_distance(a, b, c):

    def d(a, b, c):
        try:
            return distance(a, b, c)
        except ZeroDivisionError:
            return 1e6 + 0.1

    return min(
        d(a, b, c), 
        d(c, b, a),
        #d(b, a, c),
        d(c, a, b),
        #d(a, c, b),
        #d(b, c, a),
    )

def count(m):

    n = []
    for c in range(1, m+1):
        for b in range(1, c+1):
            for a in range(1, b+1):

                d = min_distance(a, b, c)
                if is_int(d):
                    n.append((a, b, c))

    return len(n)

with euler_tools.Watch():
    print(count(200))


#print(distance(2, 49, 68))

a = 100
b = 95
c = 10

'''
print(distance(a, b, c))
print(distance(c, b, a))
print(distance(b, a, c))
print(distance(c, a, b))
print(distance(a, c, b))
print(distance(b, c, a))
'''










