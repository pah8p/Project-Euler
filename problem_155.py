
WAYS = {}

def ways(n):

    try:
        return WAYS[n]

    except KeyError:

        if n == 0 or n == 1:
            w = 1

        elif n == 2:
            w = 2

        else:
            w = 0
            for i in range(1, int(n/2)+1):
                w += 2*ways(i)*ways(n-i)

        WAYS[n] = w

        return w

for i in range(1, 6):
    print(i, ways(i))
