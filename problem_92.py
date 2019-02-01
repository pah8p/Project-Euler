


HITS_89 = {}
HITS_1 = {}

next_num = lambda num: sum([int(n)**2 for n in str(num)])

def appender(a, b):
    for _a in a:
        b[_a] = True
    return b

def run_chain(n):
    
    all_n = [n]

    iters = 0
    while True:
        if n == 1:
            appender(all_n, HITS_1)
            break
        elif n == 89:
            appender(all_n, HITS_89)
            break

        try:
            _ = HITS_89[n]
            appender(all_n, HITS_89)
        except KeyError:
            pass

        try:
            _ = HITS_1[n]
            appender(all_n, HITS_1)
        except KeyError:
            pass
        
##        elif n in HITS_89:
##            appender(all_n, HITS_89)
##            print('%s 89 Hit %s' % (all_n[0], iters))
##            break
##        elif n in HITS_1:
##            appender(all_n, HITS_1)
##            break

        n = next_num(n)
        all_n.append(n)
        iters += 1

for n in range(1, 10000000):
    run_chain(n)

    
print(len(list(set(HITS_89))))
