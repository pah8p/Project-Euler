from problem_7 import sieve

PRIMES = [p for p in sieve(9999) if p > 999]

for p1 in PRIMES:
    for p2 in [p for p in PRIMES if p > p1]:
        if sorted(str(p1)) == sorted(str(p2)):
            for p3 in [p for p in PRIMES if p > p2]:
                if p2-p1==p3-p2:
                    if sorted(str(p2))==sorted(str(p3)):
                        print([p1, p2, p3])
