

def flip(n):
    return int(str(n)[::-1])

def count(n):
    i = 1
    while True:
        m = n + flip(n)
        if m == flip(m):
            return True
        else:
            n = m
            i += 1
        if i > 50:
            return False

print(sum([1 for i in range(10000) if not count(i)]))
