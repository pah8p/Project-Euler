


MIN_PATH = {}

def min_path(m, r, c):

    edge = len(m)-1

    mp = m[r][c]

    if c == 0:

        if r != edge:
            mp += min(
                min_path(m, r+1, c),
                min_path(m, r, c+1),
            )
        else:
            mp += min_path(m, r, c+1)

    elif r == 0:

        if c != edge:
            mp += min(
                min_path(m, r+1, c),
                min_path(m, r, c+1),
            )
        else:
            mp += min_path(m, r+1, c)

    else:      
        
