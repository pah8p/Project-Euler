
import euler_tools

def step(prev):
    s = []
    for p in prev:
        s.append(prev + [p + prev[-1]])
    return s

##x = step(n)
##print(x)
##
##for xx in x:
##    print(step(xx))

def target(n):

    targets = [None]*(n+1)
    targets[0] = 0
    targets[1] = 0
    targets[2] = 1
    
    paths = [[1, 2]]
    i = 1

    while True:
        i += 1
        _p = []
        for path in paths:
            for s in step(path):
                _p.append(s)
    
                try:
                    if not targets[s[-1]]:
                            targets[s[-1]] = i
                except IndexError:
                    pass
                
        paths = _p
        
        if i == 10:
            break

    return targets

with euler_tools.Watch():
    res = target(200)
for n, r in enumerate(res):
    print(n, r)

res[191]=11    
print(sum(res))









