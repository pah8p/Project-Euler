

'''1, 4, 7, 10, ...'''

FIB = {
    0: 1,
    1: 2,
}

def fib(n):
    try:
        return FIB[n]
    except KeyError:
        _fib = fib(n-1) + fib(n-2)
        FIB[n] = _fib
        return _fib

def fib_lt_4million():
    i = 0
    x = 0
    while x < 4000000:
        x = fib(i)
        i += 1
    return i

def sum_even_fibs(n):
    s = 0
    for j in range(n):
        if (j-1) % 3 == 0:
            s += fib(j)
    return s

print(fib_lt_4million())

print(sum_even_fibs(fib_lt_4million()))
