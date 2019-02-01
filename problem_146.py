
import euler_tools

def is_prime_sequence(n):
    n2 = n**2
    primes = [1, 3, 7, 9, 13, 27]
    for p in primes:
        if not euler_tools.is_prime(n2+p):
            return False
    return True

N = 1e2

with euler_tools.Watch():
    z = [n for n in range(1, int(N)) if is_prime_sequence(n)]
    print(z)
    print(sum(z))
