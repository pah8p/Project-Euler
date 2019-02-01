from problem_7 import sieve

PRIMES = sieve(1000)
print(max(PRIMES))
def prime_formula(a, b):
    def _f(n):
        return n**2 + a*n + b
    return _f

N = 1000

COEFFICIENTS = {}

b_range = [p for p in PRIMES if p <= N]
for b in b_range:
##    print(b)
    a_range = [a for a in range(-N, N+1) if (1+a+b) in PRIMES]
##    print(a_range)
##    print(max(a_range))
    for a in a_range:

        formula = prime_formula(a, b)

        i = 0
        while True:
            if formula(i) in PRIMES:
                i += 1
            else:
                COEFFICIENTS[a*b] = i
                break

prod = 0
maximum = 0
for k, v in COEFFICIENTS.items():
    if v > maximum:
        prod = k
        maximum = v

print(COEFFICIENTS)
print(prod)
print(maximum)
