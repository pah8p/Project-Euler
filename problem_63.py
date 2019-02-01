
import math

def count(n):
    i = 1
    cnt = 0
    x = 0
    while x < n:
        x = math.log10(i**n)
        if x >= (n-1) and x < n:
            cnt += 1
        i += 1
    return cnt

cnt = 0
n = 1
res = 1
while res > 0:
    res = count(n)
    cnt += res
    n += 1

print(cnt)
