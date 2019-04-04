import euler_tools
import itertools
import functools
import pickle

@euler_tools.Memoize
def partitions(target, value):
        if value == 1:
            r = [[1]*target]

        else:

            s = []
            top = int(target/value) + 1
            for n in range(0, top):
                remainder = target - value*n
                subways = ways(remainder, value - 1)
                for subway in subways:
                    s.append(n*[value] + subway)
                     
            r = s

        return r

#@euler_tools.Memoize
#@functools.lru_cache(maxsize=1024)
def sums_products(target, value):
    
    '''(sum, product, size)'''
    if value == 1:
        return [(target, 1, target)]

    else:
        
        s = []
        top = int(target/value) + 1
        for n in range(0, top):
            remainder = target - value*n
            subways = sums_products(remainder, value - 1)
            #DEPS[(target, value)].append((remainder, value-1))
            for subway in subways:

                if subway[1] * value**n < 15e3:
                    s.append((
                        subway[0] + n*value,
                        subway[1] * value**n,
                        subway[2] + n,
                    ))

        return s

def sums_products_hd(target, value):
    file_name = 'p88_cache/%s_%s.pickle' % (target, value)
    try:
        with open(file_name, 'rb') as f:
            s = pickle.load(f)

    except FileNotFoundError:

        if value == 1:
            return [(target, 1, target)]

        else:
            
            s = []
            top = int(target/value) + 1
            for n in range(0, top):
                remainder = target - value*n
                subways = sums_products_hd(remainder, value - 1)
                for subway in subways:

                    if subway[1] * value**n < 10*target:
                        s.append((
                            subway[0] + n*value,
                            subway[1] * value**n,
                            subway[2] + n,
                        ))



        with open(file_name, 'wb') as f:
            pickle.dump(s, f)

    return s

def products_sums(n):
    primes = euler_tools.prime_divisors_2(n)
    print(primes)

def min_psm(k_max):

    ks = list(range(2, k_max+1))
    psms = []
    psm = {}
    n = 4
    while True:
        with euler_tools.Watch(n):
            sps = sums_products_hd(n, n)
        for sp in sps:
            if sp[2] > 1:
                if sp[0] == sp[1]:

                    psms.append(sp)
                    try:
                        if sp[0] < psm[sp[2]]:
                            psm[sp[2]] = sp[0]

                    except KeyError:
                        if sp[2] in ks:                        
                            ks.pop(ks.index(sp[2]))
                            psm[sp[2]] = sp[0]
                     
                   
        n += 1
        if n % 10 == 0: print(n, ks)
       
        if not ks:
            break

    import pandas
    df = pandas.DataFrame(psms)
    df.to_csv('product_sum.csv', index=False)


    return sum(set(psm.values()))



with euler_tools.Watch():
    #print(sums_products(4, 4))
    
    #for i in range(5):
    #    for j in range(1, 5):
    #        print(i, j, sums_products(i, j))
    
    #for k, v in DEPS.items():
    #        print(k, v)    

    #print(sums_products(6, 6))
    #print(sums_products(8, 8))
    #print(sums_products(12, 12))
    #print(sums_products(15, 15))
    #print(ways(50, 50))
    #print(sums_products(5, 5))
    #print(min_psm(50))
    #print(sums_products.cache_info())
    #print(sorted(COUNTS.items(), key=lambda x: x[1]))
    #for x in sums_products(15, 15): 
    #    if x[0] == x[1]: print(x)
    #print(sums_products_2(4))
    #print(sums_products_2(6))
    #print(sums_products_2(8))
    #print(sums_products_2(12))
    #print(sums_products_2(15))
    #print(sums_products_2(16))
    #print(list(set(itertools.chain(*[sums_products_2(n) for n in range(4, 12000)]))))
    
