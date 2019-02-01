
N = {}


def ways_to_bottom(row, col):

    try:
        return N[(row, col)]

    except KeyError:
    
        if row == 0 or col == 0:
            x = 1
        else:
            x = ways_to_bottom(row, col-1) + ways_to_bottom(row-1, col)

        N[(row, col)] = x

        return x

print(ways_to_bottom(2, 2))
print(ways_to_bottom(3, 3))
print(ways_to_bottom(20, 20))
