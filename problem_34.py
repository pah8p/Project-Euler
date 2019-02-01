

FACTORIAL = {}

def factorial(n):

    try:
        return FACTORIAL[n]
    except KeyError:
        if n == 1 or n == 0:
            f = 1
        else:
            f = n*factorial(n-1)

        FACTORIAL[n] = f
        return f

def sum_facts(n):
    return sum([factorial(int(m)) for m in str(n)])

def check(n):
    return n == sum_facts(n)

res = [n for n in range(1, int(1e6)) if check(n)]
print(res)
print(sum(res))
