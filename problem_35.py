from problem_7 import sieve

def rotate(n):
    n_str = str(n)
    return int('%s%s' % (n_str[1:], n_str[0]))

primes = sieve(int(1e2))

CIRCULAR = {}

def circular(n):

    to_list = lambda n: [int(m) for m in str(n)]

    try:
        return CIRCULAR[n]

    except KeyError:

        print(n)

        if 2 in to_list(n):
            CIRCULAR[n] = False
            return False

        if 0 in to_list(n):
            CIRCULAR[n] = False
            return False

        if (n % 100) % 4 == 0:
            CIRCULAR[n] = False
            return False

        if 5 in to_list(n):
            CIRCULAR[n] = False
            return False

        if 8 in to_list(n):
            CIRCULAR[n] = False
            return False

        if 6 in to_list(n):
            CIRCULAR[n] = False
            return False

        if 4 in to_list(n):
            CIRCULAR[n] = False
            return False

        rotations = []
        for m in range(len(str(n))):
            n = rotate(n)
            rotations.append(n)

        _circular = True
        for rotation in rotations:
            if rotation not in primes:
                _circular = False

        for rotation in rotations:
            CIRCULAR[rotation] = _circular

        return _circular

print(len([p for p in primes if circular(p)]))


##circular = 0
##for prime in primes:
##    _circular = 0
##    _prime = prime
##    for i in range(len(str(prime))):
##        _prime = rotate(_prime)
##        if _prime in primes:
##            _circular += 1
##    if _circular == len(str(prime)):
##        circular += 1
##
##print(circular)
##        
