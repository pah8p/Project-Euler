
TEST = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

def load_matrix():
    file = 'p082_matrix.txt'
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

        if c == len(m)-1:
            mp = m[r][c]

        elif c == 0:
            mp = m[r][c] + min_path(m, r, c+1)

        else:

            col = [m[_r][c] for _r in range(len(m))]

            paths = []
            for _r in range(len(m)):

                if _r == r:
                    paths.append(min_path(m, _r, c+1))

                elif _r > r:
                    paths.append(min_path(m, _r, c+1) + sum(col[r+1:_r+1]))

                else:
                    paths.append(min_path(m, _r, c+1) + sum(col[_r:r]))

            mp = m[r][c] + min(paths)
                    
        MIN_PATH[(r, c)] = mp
        
        return mp

matrix = load_matrix()
#matrix = TEST


import euler_tools
with euler_tools.Watch():
    print(min([min_path(matrix, r, 0) for r in range(len(matrix))]))
