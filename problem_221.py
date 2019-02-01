
##p = 3
##for q in range(p+1, 1000):
##    r = (1+p*q)/(p-q)
##    #print(p, -q, r, -p*q-q*r+p*r, -p*q*r)
##
##pqs = [
##    (1, -2),
##    (2, -3),
##    (3, -5),
##    (3, -4),
##    (4, -5),
##    (5, -7),
##    (7, -9),
##    (9, -11),
##    (11, -12),
##    (11, -13),
##    (11, -16),
##]
##
##for p, q in pqs:
##    r = (1-p*q)/(p+q)
##    rr = p*q % (p+q)
##    print(p, q, r, rr)

import euler_tools

def proper_divisors(n):
    pds = []
    for i in range(n+1):
        pds.append([1])

    for m in range(2, n+1):
        k = 1
        while True:
            if k >= m:
                pds[k*m].append(m)
            k += 1
            if k*m > n:
                break

    return pds

def proper_divisors_2(n):
    pds = []
    for m in range(2, 1+int(n**0.5)):
        if n % m == 0:
            pds.append(m)
    return [1]+pds

def alexandrian_ints(ceiling):
    #primes = euler_tools.sieve(ceiling)
    a = []
    for n in range(1, ceiling):
        #with euler_tools.Watch(n):
        ms = proper_divisors_2(n**2+1)
        #ms = ms[:1+int(len(ms)/2)]
        #print(n, ms)
        for m
        in ms:
            p = n
            q = -(n+m)
            r = (1-p*q)/(p+q)
            a.append(p*q*r)
            #print(p*q*r, p*q+p*r+q*r, p, q, r, n, m)

            if len(a) >= 5*ceiling: #150000:
                return sorted(a)

N = 150000

##with euler_tools.Watch():
##    pds = proper_divisors(N)
##
##for i in range(N):
##    if pds[i] != proper_divisors_2(i):
##        print(i)

#for i, pd in enumerate(pds): print(i, pd)

with euler_tools.Watch():
    A = alexandrian_ints(N)
    
#print(A)
print(len(A))
print(int(A[N-1]))

        
