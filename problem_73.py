import euler_tools

euler_tools.write_primes(12001)
PRIMES = sorted(euler_tools.read_primes())

def gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

def coprime_2(n, m):
    return gcd(n, m) == 1

def totients(n):
    t = list(range(1, n+1))
    for p in PRIMES:

        m = 1
        while m*p <= n:
            t[m*p-1] *= (1-1/p)
            m += 1

    return [int(_t) for _t in t]

CP = {}

def coprime(n, m):
    try:
        return CP[(n, m)]
    except KeyError:
        _coprime = True
        for p in PRIMES:

            if p > min(n, m):
                break
            
            if n % p == 0 and m % p == 0:
                _coprime = False
                break
    
        CP[(n, m)] = _coprime
        return _coprime

def fractions(n):
    fs = []
    for i in range(5, n+1):
        #print(i)
        for j in range(int(i/3), int(i/2)+1):
            if coprime_2(i, j):
                if (1/3 < j/i < 1/2):
                    #print(i, j, j/i)
                    fs.append((i, j, j/i))
    return fs


N = 1000

with euler_tools.Watch():
    f = fractions(N)
    print(len(f))
#print(f)
#print(len(f))


#print(sum(t))
#print(len(f)/sum(t))


