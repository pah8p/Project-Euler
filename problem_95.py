
import euler_tools

##PDS = {}
##
##def proper_divisors(n):
##    try:
##        return PDS[n]
##
##    except KeyError:
##        pds = euler_tools.proper_divisors(n)
##        PDS[n] = pds
##        return pds

def divisors_to(n):

    d = []
    for i in range(n):
        d.append([])
        
    for i in range(1, int(n/2+1)):
        j = 2
        while i*j < n:            
            d[i*j].append(i)
            j += 1

    return d
    
    

def chain_length(n, divisors):
    
    i = 1
    _n = n
    while i < 100:

        try:
            n = sum(divisors[n])
        except IndexError:
            return -1

        print(i, n)

        if n == _n:
            return i
        elif n == 1:
            return -2
        else:
            i += 1

    return 0

def max_chain_to(n, divisors):
    _max = []
    for m in range(1, n+1):
        cl = chain_length(m, divisors)
        _max.append((cl, m))

    #print(_max)
    __max = max(_max, key=lambda x: x[0])

    return __max
        
#print(divisors_to(10**6))

N = 10**6

divisors = divisors_to(N)

print(chain_length(14316, divisors))

#cl, m = max_chain_to(N, divisors)

#print(cl, m, _min)

#print(chain_length(19994, divisors))
#print(chain_length(220))

#print(sum(divisors[41]), divisors[41])




