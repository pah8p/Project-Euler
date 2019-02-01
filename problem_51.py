import euler_tools
import collections

euler_tools.write_primes(int(1e6))
primes = euler_tools.read_primes()

primes = [p for p in primes if p > 56993]

def count_digits(n):
    gt2 = False
    dupes = []
    count = collections.defaultdict(int)
    for m in str(n):
        count[m] += 1

    for k, v in count.items():
        if v >= 2:
            dupes.append(k)

    return dupes

def check_siblings(n, m):
    cnt = 0
    sibs = []
    for i in range(0, 10):

        _n = int(str(n).replace(str(m), str(i)))

        #print(_n)

        if _n not in primes:
            cnt += 1
        else:
            sibs.append(_n)
            
        if cnt > 2:
            return False, sibs

    return True, sibs

#print(check_siblings(56003, 0))

for p in primes:
    dupes = count_digits(p)
    for dupe in dupes:
        flag, sibs = check_siblings(p, dupe)
        if flag:
            print(sibs)
            break
        
    
