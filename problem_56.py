
sum_digits = lambda n: sum([int(m) for m in str(n)])


_max = 0
for a in range(1, 100):
    for b in range(1, 100):
        c = sum_digits(a**b)
        if c > _max:
            _max = c

print(_max)
