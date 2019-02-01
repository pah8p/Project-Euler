
TEST = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

def load_matrix():
    file = 'p083_matrix.txt'
    with open(file, 'r') as f:
        raw_matrix = f.readlines()

    matrix = []
    for row in raw_matrix:
        matrix.append([int(x) for x in row[:-1].split(',')])

    return matrix

MIN_PATH = {}

def min_path(m, r, c):
    
    try:
        
        return MIN_PATH[(r, c)]

    except KeyError:

        if c == len(m)-1 and r == len(m)-1:
            mp = m[r][c]

        else:

            col = [m[_r][c] for _r in range(len(m))]
            row = m[r]

            paths = []

            for _r in range(len(m)):

                if c == len(m)-1:
                    min_neighboor_neighboors = min_path(m, _r, c-1)
                elif c == 0:
                    min_neighboor_neighboors = min_path(m, _r, c+1)
                else:
                    min_neighboor_neighboors = min(
                        min_path(m, _r, c-1),
                        min_path(m, _r, c+1),
                    )

                ## UP
                if _r > r:
                    sum_neighboors = sum(col[r+1:_r+1])

                ## DOWN
                elif _r < r:
                    sum_neighboors = sum(col[_r:r])
    
            for _c in range(len(m)):

                if r == len(m) - 1:
                    min_neighboor_neighboors = min_path(m, r-1, _c)
                elif r == 0:
                    min_neighboor_neighboors = min_path(m, r+1, _c)
                else:
                    min_neighboor_neighboors = min(
                        min_path(m, r-1, _c),
                        min_path(m, r+1, _c),
                    )

                ## RIGHT
                if _c > c:
                    sum_neighboors = sum(row[c+1:_c+1])

                ## LEFT
                elif _c < c:
                    sum_neighboors = sum(row[_c:c])

            paths.append(sum_neighboors + min_neighboor_neighboors)

            mp = m[r][c] + min(paths)
                    
        MIN_PATH[(r, c)] = mp
        
        return mp

def orders(n):
    order = []
    for i in range(n):
        _order = []
        for j in range(0, i+1):
            _order.append((i-j, j))
        order.append(_order)

    for i in range(n, 1, -1):
        _order = []
        for j in range(1, i):
            print(i, j, n-j, j)
            _order.append((n-j, j))
        order.append(_order)
        
    return order

def min_path_2(m):
    kids = {}
    for r in range(len(m)):
        for c in range(len(m)):

            if r == len(m)-1:
                kids[(r, c)] = [(r, c+1)]
            elif c == len(m)-1:
                kids[(r, c)] == [(r+1, c)]
            else:
                kids[(r, c)] = [(r, c+1), (r+1, c)]

    order = []
    for i in range(2*len(m)-1):
        _order = []
        for a in range(i):
            for b in range(i):
                _order.append((a, b))
        order.append(_order)

            
    
    dim = len(m)-1
    r, c = dim, dim

    while r >= 0 and c >= 0:

        m[r-1][c] += m[r][c]
        m[r][c-1] += m[r][c]

        r += -1
        c += -1


matrix = load_matrix()
matrix = TEST

print(orders(4))

import euler_tools
#with euler_tools.Watch():
#    print(min_path(matrix, 0, 0))
