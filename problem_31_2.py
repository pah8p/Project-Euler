#        h  g  f  e   d   c   b    a
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

count = 0

def counts(amount, coin_value):
    count = 0
    for i in range(int(amount/coin_value) + 1):
        if amount == i * coin_value:
            count += 1
    return count

a_top = 1 + 1
for a in range(0, a_top):

    gap_b = 200 - 200*a
    b_top = int(gap_b/100) + 1

    for b in range(0, b_top):

        gap_c = gap_b - 100*b
        c_top = int(gap_c/50) + 1

        for c in range(0, c_top):

            gap_d = gap_c - 50*c
            d_top = int(gap_d/20) + 1

            for d in range(0, d_top):

                gap_e = gap_d - 20*d
                e_top = int(gap_e/10) + 1

                for e in range(0, e_top):

                    gap_f = gap_e - 10*e
                    f_top = int(gap_f/5) + 1

                    for f in range(0, f_top):

                        gap_g = gap_f - 5*f
                        g_top = int(gap_g/2) + 1

                        for g in range(0, g_top):

                            gap_h = gap_g - 2*g


                            count += counts(gap_h, 1)


print(count)

                                
def ways(target, index):
    ways = [1] + [0]*(target)
    for i in range(index):
        for j in range(COINS[i], target+1):
            ways[j] += ways[j-COINS[i]]
    return ways[target]

print(ways(200, 8))




    
