import euler_tools

def sieve(n):
    _sieve = [0]*(int(n**0.5)+1)
    for m in range(1, n):
        k = 1
        while True:

            sqr = (m*k)**0.5

            if sqr.is_integer() and m <= sqr:
                _sieve[int(sqr)-1] += 1
            
            k += 1
            if m*k >= n:
                break
    return _sieve


def is_prime(n):
    if n == 1:
        return False

    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False

    return True

def num_solutions(n):
    s = 0
    for x in range(n+1, 2*n+1):
        y = n*x/(x-n)
        if y.is_integer():
            s += 1
    return s

def num_solutions_2(n):

    if n == 1:
        return 1

    if is_prime(n):
        return 2

    n2 = n**2
    s = 2
    for m in range(2, n):
        if n2 % m == 0:
            s += 1
    return s


def more_than_N(N):
    n = 4
    while True:
        ns = num_solutions_2(n)
        #print (n, ns)
        if ns > 300: print(n, ns)
        if ns > N:
            print(n)
            break
        n += 1

#print(num_solutions_2(16))

with euler_tools.Watch():
    more_than_N(1000)




#with euler_tools.Watch():
#    s = sieve(20000000)

#print(max(s))
#print(1+s.index(max(s)))


#for i, ss in enumerate(s):
    
#    if ss > 99:
#        print(i+1, ss)

