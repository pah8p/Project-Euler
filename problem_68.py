
import itertools

def three_gon():
    
    choices = [1, 2, 3, 4, 5, 6]
    all_guesses = itertools.permutations(choices, 4)
    solved = []
    _solved = []
    
    for g in all_guesses:
        a1 = g[0]
        a2 = g[1]
        a3 = g[2]
        b3 = g[3]
        b1 = a1+a2-b3
        c1 = a1+a3-b3

        unused = [x for x in choices if x not in g]

        if b1 in unused:
            unused.remove(b1)
            if c1 in unused:
                s = a1 + a2 + a3
                try:
                    assert(s == b1 + a3 + b3)
                    assert(s == c1 + b3 + a2)

                    res = [[a1, a2, a3], [b1, a3, b3], [c1, b3, a2]]

                    first = min(res, key=lambda x: x[0])
                    index = res.index(first)
                    res = res[index:] + res[:index]
                    if res not in _solved:
                        solved.append((s, list(itertools.chain(*res))))
                        _solved.append(res)
                    
                except AssertionError:
                    print('SUM ERROR')
                    pass

    for s in solved: print(s)
    print(max(s, key=lambda x: x[1]))
    return None

def five_gon():

    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    all_guesses = itertools.permutations(choices, 6)
    solved = []
    _solved = []

    for g in all_guesses:
        a1, a2, a3, b3, c3, d3 = g
        s = a1 + a2 + a3
        b1 = s - a3 - b3
        c1 = s - b3 - c3
        d1 = s - c3 - d3
        e1 = s - a2 - d3

        unused = [x for x in choices if x not in g]

        for y in [b1, c1, d1, e1]:
            if y in unused:
                unused.remove(y)

        if unused == []:
            res = [
                [a1, a2, a3],
                [b1, a3, b3],
                [c1, b3, c3],
                [d1, c3, d3],
                [e1, d3, a2],
            ]

            for i in range(len(res)-1):
                assert(sum(res[i])==sum(res[i+1]))

            first = min(res, key=lambda x: x[0])
            index = res.index(first)
            res = res[index:] + res[:index]
            if res not in _solved:
                solved.append((s, list(itertools.chain(*res))))
                _solved.append(res)
            
    for s in solved: print(s)
    #print(max(s, key=lambda x: x[1]))
    return None

five_gon()
