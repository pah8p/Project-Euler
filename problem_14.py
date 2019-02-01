
CACHE = {}

def next_collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def len_collatz(n):
    orig_n = n
    count = 0
    while True:
        if n == 1:
            count += 1
            break

        elif n in CACHE:
            count += CACHE[n]
            break

        else:
            count += 1
            n = next_collatz(n)

    CACHE[orig_n] = count
    return count

for i in range(1, 1000001):
    len_collatz(i)

max_len = 0
max_start = 0
for k, v in CACHE.items():
    if v > max_len:
        max_start = k
        max_len = v
        
print(max_len)
print(max_start)
print(CACHE[max_start])
