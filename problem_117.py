
WAYS = {}

def ways(length, tile_length):

    try:
        return WAYS[(length, tile_length)]

    except KeyError:

        s = 0

        for tile in range(tile_length, tile_length+3):
            _s = s
            left = 0
            while True:
                if left + tile <= length:
                    s += 1
                    if length - tile - left >= tile_length:
                        s += ways(length - tile - left, tile_length)
                    left += 1
                else:
                    break

            #print(tile, s-_s)

        WAYS[(length, tile_length)] = s
        
        return s

print(ways(5, 2))
#print(ways(5, 3))
#print(ways(5, 4))

print(ways(50, 2))

