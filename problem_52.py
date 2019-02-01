


def key(n):
    return sorted(str(n))

def check_multiples(n):
    key_1 = key(n)
    for j in range(2, 7):
        if key_1 != key(n*j):
            return False
    return True

def check_base(power):
    for i in range(power, int(power*10/6)):
        if check_multiples(i):
            return i
    return None

print(check_base(int(1e2)))
