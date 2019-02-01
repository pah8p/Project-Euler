
WAYS = {}

def ways(length, tile_length):

    try:
        return WAYS[(length, tile_length)]

    except KeyError:

        s = 0

        for tile in range(tile_length, length+1):
            _s = s
            left = 0
            while True:
                if left + tile <= length:
                    s += 1
                    if length - tile - left - 1 >= 3:
                        s += ways(length - tile - left - 1, tile_length)
                    left += 1
                else:
                    break

            #print(tile, s-_s)

        WAYS[(length, tile_length)] = s
        
        return s

def over_N(tile_length, threshold):
    n = 1
    while True:
        _ways = 1+ways(n, tile_length)
        if _ways > threshold:
            return n
        else:
            n += 1

        if n % 100 == 0:
            print(n)

print(over_N(50, 1000000))

print(ways(167, 50)+1)
#print(ways(3))
#print(ways(7))
#print(ways(8))
#print(ways(50, 3)+1)
#print(ways(30, 3)+1)
