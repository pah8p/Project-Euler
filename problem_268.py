
from euler_tools import sieve

PRIMES = sieve(100)

print(PRIMES)

def divisible_by_four_primes(n):
    nums = []
    for i in range(len(PRIMES)):
        for j in range(i+1, len(PRIMES)):
            for k in range(j+1, len(PRIMES)):
                for m in range(k+1, len(PRIMES)):

                    q = 1
                    while True:
                        num = q*PRIMES[i]*PRIMES[j]*PRIMES[k]*PRIMES[m]

                        print(n/num)

                        if num < n:
                            nums.append(num)
                            q += 1
                        else:
                            break
                        
    return len(nums), nums


print(divisible_by_four_primes(10000000000000000))
                        
