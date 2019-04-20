import collections
import euler_tools

P = 1009
Q = 3643

def gcd(n, m):
    r = n % m
    while r > 0:
        n = m
        m = r
        r = n % m
    return m

def rsa(p, q):
    unconcealed_e = collections.defaultdict(int)
    n = p*q
    phi = (p-1)*(q-1)
    es = [e for e in range(1, phi) if gcd(e, phi) == 1]
    ms = range(n)
    #es = [181]
    #print(len(es), len(ms), len(es)*len(ms))
    
    for e in es:
        for m in ms:

            #print(m, e, m**(e-1) % n)

            if (m**e % n) == m:
                unconcealed_e[e] += 1

    #print(unconcealed_e[181], n)
    return unconcealed_e, max(unconcealed_e.items(), key=lambda x: x[1])


@euler_tools.memoize
def divisors(n):
    return euler_tools.all_divisors(n)


def element_order(x, group):

    if x % group == 0:
        return 0

    for i in divisors(group-1):
        if x**i % group == 1:
            return i


def get_order(m, g, orders):

    if m > g:
        return orders[g][m % g -1], orders
    else:
        order = element_order(m, g)
        try:
            orders[g][m-1] = order
        except KeyError:
            orders[g] = [None] * g
            orders[g][m-1] = order
        return order, orders

@euler_tools.memoize
def e_sieve(order, phi):

    if order == 0:
        return list(range(1, phi))

    else:
        es = []
        for i in range(1, int(phi/order)):
            es.append(i*order)

        return es

def count_bad_ems(m_es, e_cnts, es, phi):

    #print(len(m_es), len(es))

    bad_es = m_es #list(set(m_es) & set(es))
 
    for bad_e in bad_es:
        if gcd(bad_e, phi) == 1:
            e_cnts[bad_e] += 1
    return e_cnts

def unconcealed(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    es = [] #[e for e in range(1, phi) if gcd(e, phi) == 1]
    orders = {}

    e_cnts = [0] * phi

    for m in range(1, n):

        print(m)

        order = 1

        for g in [p, q]:

            #with euler_tools.Watch('Calculating order of %s in %s' % (m, g)):
            with euler_tools.Watch('Ordering'):
                _order, orders = get_order(m, g, orders)

            order *= _order

            #with euler_tools.Watch('Sieving'):
            #    g_es = e_sieve(order, phi)
                #print(len(g_es))
            #m_es.append(g_es)

        with euler_tools.Watch('Sieving'):
            m_es = e_sieve(order, phi)

        with euler_tools.Watch('Counting'):
            print(len(m_es))
            e_cnts = count_bad_ems(m_es, e_cnts, es, phi)
            #pass     
    return e_cnts


with euler_tools.Watch():
    u = unconcealed(3, 5)
    print(u)

#with euler_tools.Watch():
    #r = rsa(19, 37)[0]

#for nu, _u in enumerate(u):
#    print(nu, _u, r[nu+1])






















