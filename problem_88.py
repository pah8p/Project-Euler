import euler_tools

@euler_tools.Memoize
def divisors(n):
    return euler_tools.proper_divisors(n) + [n]

@euler_tools.Memoize
def product_partitions(n):

    if n == 1:
        return []
    
    ds = divisors(n)
    ds.pop(0)

    if len(ds) == 1:
        return [ds]

    partitions = [[n]]
    
    for d in ds:
        sub_partitions = product_partitions(n//d)
        for sub_partition in sub_partitions:
            partitions.append(sorted([d] + sub_partition))

    return partitions

def products_sums(k_max):

    ps = {}
    ks = list(range(1, k_max+1))
    n = 4

    while True:

        partitions = product_partitions(n) 

        for partition in partitions:
            k = (n-sum(partition)) + len(partition)

            if k not in ps and k <= k_max:
                ps[k] = n
                ks.pop(ks.index(k))

        n += 1

        if not ks:
            break
    
    return sum(set(ps.values()))



with euler_tools.Watch():
    print(products_sums(12000))
    #print(product_partitions(36))

