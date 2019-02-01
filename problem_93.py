import itertools

OPS = ['+']*3 + ['-']*3 + ['*']*3 + ['/']*3
OPERATIONS = list(set(itertools.permutations(OPS, 3)))
print(len(OPERATIONS))
#for o in sorted(OPERATIONS): print(o)

def values_by_set(s):

    combos = list(itertools.permutations(s))
    #print(len(combos))
    exps = []
    n = []
    
    for c in combos:
        for o in OPERATIONS:
    
            try:
                exp = '(((%s%s%s)%s%s)%s%s)' % (c[0], o[0], c[1], o[1], c[2], o[2], c[3])
                val = float(eval(exp))

                if val.is_integer() and val > 0:
                    n.append(int(val))
                    #if val == 1: print(exp)
                    exps.append((n, exp))

                    if c == (1,2,3,4): print(val, exp)
                    
            except ZeroDivisionError:
                pass

    #print(len(exps))
    return sorted(list(set(n)))

def max_consecutive(x):
    try:
##        for y in range(len(x)):
##            if x[y]+1 != x[y+1]:
##                return x[y]
##        return x[-1]
        for y in range(len(x)):
            #print(y, (y+1)*(y+2)/2, x[:y+1])
            if sum(x[:y+1]) != (y+1)*(y+2)/2:
                return y
        return x[-1]
    except IndexError:
        print(x, y)
        return 100


all_ints = list(itertools.combinations(range(1, 10), 4))

print(len(all_ints))


res = []
for ints in all_ints:
    vals = values_by_set(ints)
    res.append((max_consecutive(vals), ints, vals))

for r in sorted(res, key=lambda x: x[0]): print(r[0], r[1], r[2])


print(max(res, key=lambda x: x[0]))

#print(max_consecutive([1, 2, 3, 4, 5, 6, 8]))

#print(values_by_set([1,2,3,4]))
#print(max_consecutive(values_by_set([1,2,3,4])))
#print(max_consecutive(values_by_set([4,3,2,1])))
    
