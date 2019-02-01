

def brute_force(n):

    s = 0

    for i in range(1, n):

        if i % 3 == 0 or i % 5 == 0:

            s += i

    return s


print(brute_force(1000))
