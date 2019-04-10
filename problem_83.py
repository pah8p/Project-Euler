
import euler_tools

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


#@euler_tools.Memoize
def enumerate_paths(r, c, dim, prev_step=None):

    if (r, c) in [(1, 0), (0, 1)]:
        return [(0, 0)]

    paths = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if prev_step:
        moves.pop(moves.index(prev_step))

    for move in moves:

        next_row = r+move[0]
        next_col = c+move[1]
        
        if 0 < next_row < dim:
            if 0 < next_col < dim:
    
                print(next_row, next_col)

                step = (-move[0], -move[1])
                path = [(next_row, next_col)] + enumerate_paths(next_row, next_col, dim, step)
                paths.append(path)

    return paths
        
matrix = load_matrix()
matrix = TEST

print(enumerate_paths(1, 1, 5))

#with euler_tools.Watch():
#    print(min_path(matrix, 0, 0))
