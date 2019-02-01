import math
import decimal
import pell_equation

def quadratic(a, b, c):
    d = b**2-4*a*c
    return (-b + decimal.Decimal(d).sqrt())/(2*a)

def b_from_n(n):
    return quadratic(1, -1, -(1/2)*(n**2-n))

#print(b_from_n(21))
#print(b_from_n(120))

def test(b, n):    
    x = (2*n-1)**2-2*(2*b-1)**2
    return x

def pell_solutions(n):
    solutions = []
    pells = pell_equation.solve(2, n)
    for pell in pells:

        n = (pell[0] + 1)/2
        b = (pell[1] + 1)/2



        #if n > 10e12:
        if n.is_integer() and b.is_integer():
#                print(pell[0]**2-2*pell[1]**2)
            print(n, b, n > 1000000000000)

        solutions.append(((pell[1]+1)/2, (pell[0]+1)/2))
    return solutions

##def search():
##    n = int(1e12)
##    while True:
##        b = b_from_n(n)
##        #if abs(b-int(b)) < 0.001:
##        #    print('%s -- %s -- %s' % (n, int(b), b-int(b)))
##        if b == int(b):
##            print('%s -- %s' % (n, b))
##            return int(b)
##        n += 1
##        #if n % 1000 == 0:
##            #print(n)
##        if n > 1e12 + 1e6:
##            return None


#search()

print(pell_solutions(50))
