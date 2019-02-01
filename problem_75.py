
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

def coprime(n, m):
    n_divisors = prime_divisors(n)
    m_divisors = prime_divisors(m)
    common_divisors = list(set(n_divisors) & set(m_divisors))
    return not common_divisors

def pythag_triples(m_max):
    triples = []
    for m in range(2, m_max):
        #if m % 100 == 0: print(m)
        for n in range(1, m):
            #with euler_tools.Watch('Coprime %s %s' % (m, n)):
            if coprime(m, n):
                if (m+n) % 2 == 1:
                    triples.append(pythag_triple(m, n))
    return triples

def pythag_triple(x, y):
    return {
        'a': x**2-y**2,
        'b': 2*x*y,
        'c': x**2+y**2,
        'm': x,
        'n': y,
    }

def check_perimeters(triples):

    perims = collections.defaultdict(int)

    max_p = 0
    
    for t in triples:

        p = t['a'] + t['b'] + t['c']
        max_p = max(p, max_p)

        n = 1

        perim = p
        while perim <= 1500000:
            perim = p * n

            if perim <= 1500000:
                perims[perim] += 1

            #if n % 100 == 0:
                #print(t['a'], t['b'], t['c'], p, n)

            n += 1

    #print(perims[120])
    #print(max_p)
    singles = [k for k, v in perims.items() if v == 1]

    return sorted(singles)

triples = pythag_triples(5000)

#print(len(triples))

singles = check_perimeters(triples)

#print(singles[:100])
print(len(singles))

















    
