import collections
import itertools
import copy

def sums():
    sums = {i: collections.defaultdict(list) for i in range(1, 5)}
    for a in range(0, 10):
        sums[1][a].append([a])
        for b in range(0, 10):
            sums[2][a+b].append((a, b))
            for c in range(0, 10):
                sums[3][a+b+c].append((a, b, c))
                for d in range(0, 10):
                    sums[4][a+b+c+d].append((a, b, c, d))
    return sums

def empty_list(l):
    try:
        sum(l)
        return False
    except TypeError:
        return True

SUMS = sums()

GRIDS = []

def copier(grid):
    _grid = []
    for r in grid:
        __grid = []
        for c in r:
            __grid.append(c)
        _grid.append(__grid)
    return _grid

def build_grid(target, grid, row_or_col='r', index=0):

    _grid = copier(grid)

    #print(target, grid, row_or_col, index)

    if row_or_col=='r':
        size = sum(1 if not isinstance(v, int) else 0 for v in grid[index])
    elif row_or_col=='c':
        size = sum(1 if not isinstance(v[index], int) else 0 for v in grid)

    if index == 3:
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == None:
                    _grid[r][c] = target

        if check_grid(_grid):
            print(grid)
            GRIDS.append(hash(_grid))

        return _grid
    
    try:
        target_vectors = SUMS[size][target]
    except KeyError:
        print('KeyError', size, target)

    if not target_vectors:
        return _grid

    for vector in target_vectors:

        if row_or_col == 'r':
            empty_cols = [n for n, val in enumerate(grid[index]) if not isinstance(val, int)]
            for v, col in zip(vector, empty_cols):
                _grid[index][col] = v

            for n in range(len(grid)):
                col = [row[n] for row in grid]
                if empty_list(col):
                    col_total = sum(v if v else 0 for v in col)
                    __grid = build_grid(target-col_total, _grid, row_or_col='c', index=n)

        elif row_or_col == 'c':
            empty_rows = [n for n, val in enumerate(grid) if not isinstance(val[index], int)]

            for v, row in zip(vector, empty_rows):
                _grid[row][index] = v

            for n in range(len(grid)):
                row = grid[n]
                if empty_list(row):
                    row_total = sum(v if v else 0 for v in row)
                    __grid = build_grid(target-row_total, _grid, row_or_col='r', index=n)

    return __grid


def hash(grid):
    h = []
    for row in grid:
        for col in row:
            h.append(str(col))
    return int(''.join(h))


def _check_grid(grid):
    x = sum(grid[0])

    for n in range(4):
        assert sum(grid[n]) == x
        assert sum([r[n] for r in grid]) == x
        for c in range(4):
            assert isinstance(grid[n][c], int)

    assert grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3] == x
    assert grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0] == x

def check_grid(grid):
    try:
        _check_grid(grid)
        return True
    except AssertionError:
        return False

g = [
    [6, 3, 3, 0],
    [5, 0, 4, 3],
    [0, 7, 1, 4],
    [1, 2, 4, 5],
]


#print(check_grid(g))
#print(hash(g))

grid = [[None]*4, [None]*4, [None]*4, [None]*4]



print(build_grid(5, grid))
print(len(GRIDS))

