import time
import euler_tools

ABUNDANT_N = {}

def is_abundant(n):
    try:
        return ABUNDANT_N[n]
    except KeyError:
        s = time.time()
        x = sum(euler_tools.proper_divisors(n)) > n
        ABUNDANT_N[n] = x
        #print ('%s took %s' % (n, time.time()-s))
        return x

print(is_abundant(12))

N = 28124

abundants = []
for n in range(1, N):
    if n % 1000 == 0:
        print(n)
    if is_abundant(n):
        for m in range(1, N-n):
            if is_abundant(m):
                abundants.append(n+m)

print(len(abundants))
abundants = list(set(abundants))
print(len(abundants))
print(sum(abundants))

non_abundants = [n for n in range(1, N) if n not in abundants]
#print(non_abundants)
print(sum(non_abundants))
