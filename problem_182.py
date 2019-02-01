import collections

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

    print(len(es), len(ms), len(es)*len(ms))
    
    for e in es:
        for m in ms:
            if (m**e % n) == m:
                unconcealed_e[e] += 1

    print(unconcealed_e[181], n)
    return unconcealed_e, max(unconcealed_e.items(), key=lambda x: x[1])

print(rsa(1009, 3643))
