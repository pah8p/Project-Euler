
def len_cycle(n):
    r = 1 % n
    i = 0
    seen = {}
    while True:
        #new_r = 10*old_r % n
        #m = int((10*old_r - new_r)/n)
        #old_r = new_r

        r = 10*r % n

        if r in seen:
            print(seen)
            return i - seen[r]
        else:
            seen[r] = i

        i += 1
        if i == 1000:
            return False

    return None

print(len_cycle(7))
print(1/83)

#z = (1/7) == invert(7)

#print(z)




def sig_digits(n):
    m = 1
    _n = n
    while True:
        if int(10**m * _n) == 0:
            n = 10**m * _n
        else:
            return n
        m += 1
    return None


print(len_cycle(993))

cycles = [(n, len_cycle(n)) for n in range(1, 1000) if len_cycle(n)]
for c in cycles: print(c)
print(max(cycles, key = lambda x: x[1]))

#
