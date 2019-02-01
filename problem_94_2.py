import euler_tools
import collections

PDS = {}

def prime_divisors(n):
    try:
        return PDS[n]
    except KeyError:
        #with euler_tools.Watch('PRIME DIVISORS %s' % n):
        pds = euler_tools.prime_divisors(n)
        PDS[n] = pds
        return pds

CP = {}

def coprime(n, m):
    try:
        return CP[(n, m)]
    except KeyError:
        n_divisors = prime_divisors(n)
        m_divisors = prime_divisors(m)
        common_divisors = list(set(n_divisors) & set(m_divisors))
        CP[(n, m)] = not common_divisors
        return not common_divisors        

def pythag_triples(m_max, p_max):
    triples = 0
    m = 2
    max_p = 0
    seen = collections.defaultdict(lambda: False)
    while max_p < p_max:
    #for m in range(2, m_max):
        if m % 500 == 0: print(m, max_p/p_max)
        for n in range(1, m):
            if ((m+n)%2==1):

                _a = m**2-n**2
                _b = 2*m*n
                a, b = min(_a, _b), max(_a, _b)
                c = m**2+n**2
                k = abs(c-2*a)

                y = 2*a/k
                x = c/k
                p = 2*x+y
                area = a*b/(k**2)

                if c == 1032607092:
                    print(m, n)
                    return False

                max_p = max(p, max_p)

                if p > p_max:
                    break
                    print('hit p_max %s' % p)

                if x.is_integer() and y.is_integer() and p < p_max and not seen[(x,y)]:
                    print(a, b, c, x, y, p, area)
                    triples += p
                    seen[(x, y)] = True
                else:
                    triples += 0

            else:
                triples += 0
        #print(max_p, max_p/p_max)
        m += 1

    return triples

N = 5
P = 1e6

#triples = pythag_triples(N, P)

#print(triples)

print(coprime(516309057, 894260792))
print(coprime(516309057, 1032607092))
print(coprime(894260792, 1032607092))

print(euler_tools.prime_divisors(516309057))
print(euler_tools.prime_divisors(894260792))
print(euler_tools.prime_divisors(1032607092))
              
