


TEST = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

def load_matrix():
    file = 'p081_matrix.txt'
    with open(file, 'r') as f:
        raw_matrix = f.readlines()

    matrix = []
    for row in raw_matrix:
        matrix.append([int(x) for x in row[:-1].split(',')])

    return matrix

def sum_matrix(m):
    for r, row in enumerate(m):
        for c, col in enumerate(row):

            if r == 0:
                if c != 0:
                    m[r][c] += m[r][c-1]

            elif c == 0:
                if r != 0:
                    m[r][c] += m[r-1][c]

            else:
                m[r][c] += min(m[r-1][c], m[r][c-1])

    #for r in m: print(r)
    #print(m[0])
    return m[-1][-1]

print(sum_matrix(load_matrix()))

#print(load_matrix()[0])
