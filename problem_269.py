#from sympy.solvers import solve
#from sympy import Symbol

def quad(a, b, c):

    if a == 0:
        try:
            return -c/b, -c/b
        except ZeroDivisionError:
            return 0.1, 0.1
        
    d = (b**2 - 4*a*c)**0.5
    return (-b+d)/(2*a), (-b-d)/(2*a)

def brute2():
    ints = []
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                n = a*100 + b*10 + c
                y1, y2 = quad(a, b, c)

                try:
                    if y1.is_integer():
                        ints.append((n, int(a), int(y1), int(a*y2), y2))
                    elif y2.is_integer():
                        ints.append((n, int(a), int(y2), int(a*y1), y1))
                except AttributeError:
                    pass
                
    return ints


def brute3():
    ints = []
    x = Symbol('x')
    for a in range(0, 10):
        print(a)
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):

                    eq = a*x**3 + b*x**2 + c*x + d
                    n = a*10**3 + b*10**2 + c*10 + d

                    ys = solve(eq, x)
                    for y in ys:
                        try:
                            if y == int(y):
                                ints.append(n)
                        except:
                            pass
    return ints

N_WAYS = {}

def n_ways(n, m):
    try:
        return N_WAYS[(n, m)]

    except KeyError:
        if n == 1:
            ans = int(m)
        else:



            
            ans = int(m) + sum([n_ways(n-1, m/a) for a in range(1, int(m)+1)])

    N_WAYS[(n, m)] = ans
    print(n, m, ans)
    return ans

b = brute2()
print(len(b))
s = 0
for _b in sorted(b, key=lambda x: '%s%s%s' % (x[1], x[2], x[3])):
    if _b[4].is_integer() and _b[0] < 1000:
        s += 1
        print(_b[0], _b[1], _b[2], int(_b[4]), int(_b[2]*_b[4]), int(_b[2]+_b[4]))

print(s)

##grouped = {}
##for bb in b:
##    try:
##        grouped[(bb[1], bb[2])] += 1
##    except KeyError:
##        grouped[(bb[1], bb[2])] = 1
##
##for k, v in grouped.items():
##    print(k, v)

print(n_ways(2, 9))
#print(n_ways(16, 9))
print(n_ways(3, 9))

##import euler_tools
##with euler_tools.Watch():
##    print(n_ways(16, 9))
