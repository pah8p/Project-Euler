import euler_tools
import itertools

WAYS = {}

PRIMES = euler_tools.read_primes()

def ways(target, index):
    ways = [1] + [0]*(target)
    for i in range(index):
        for j in range(PRIMES[i], target+1):
            ways[j] += ways[j-PRIMES[i]]
    return ways[target]

def _ways(target):
    for n, p in enumerate(PRIMES):
        if p >= target:
            v = n -1
            break
    return ways(target, v)

def first_ways(n):
    i = 10
    while True:
        w = _ways(i)
        if w > n:
            return w, i
        i += 1

        if i > 100:
            return None
        
with euler_tools.Watch():
    print(first_ways(5000))

print(ways(10, 200), PRIMES[-1])
