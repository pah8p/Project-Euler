import itertools

OPS = ['+']*3 + ['-']*3 + ['*']*3 + ['/']*3
OPERATIONS = list(set(itertools.permutations(OPS, 3)))
#print(len(OPERATIONS))
#for o in sorted(OPERATIONS): print(o)

def values_by_set(s):

    combos = list(itertools.permutations(s))
    n = []
    
    for c in combos:
        for o in OPERATIONS:
    
            try:
                exp = '((%s%s%s)%s%s)%s%s' % (c[0], o[0], c[1], o[1], c[2], o[2], c[3])
                val = float(eval(exp))

                if val.is_integer() and val > 0:
                    n.append(int(val))

 #                   if val == 8: print(val, exp)
                   
            except ZeroDivisionError:
                pass
   
    return sorted(list(set(n)))

def max_consecutive(x):
    for n in range(len(x)-1):
        if x[n+1] != 1 + x[n]:
            return x[n]
    return x[-1]

all_ints = list(itertools.combinations(range(0, 10), 4))

#print(len(all_ints))
#all_ints = [[1,2,3,4]]

res = []
for ints in all_ints:
    #print(ints)
    vals = values_by_set(ints)
    res.append((max_consecutive(vals), ints, vals))

for r in sorted(res, key=lambda x: x[0]): print(r[0], r[1])


print(max(res, key=lambda x: x[0]))

print(max_consecutive([1, 2, 3, 4, 5, 6, 7, 8]))

#print(values_by_set([1,2,3,4]))
#print(max_consecutive(values_by_set([1,2,3,4])))
#print(max_consecutive(values_by_set([4,3,2,1])))
#print(max_consecutive(values_by_set([6,5,2,1])))
