


int_to_list = lambda x: list(set([int(y) for y in str(x)]))

f = 1

for n in range(10, 100):
    
        for m in range(10, 100):

            if not n == m:

                if str(n)[0] == str(m)[-1]:

                    if (n/m) == int(str(n)[-1])/int(str(m)[0]):

                        print ('%s --- %s --- %s' % (n, m, n/m))

                        f *= (n/m
            

            #elif str(n)[-1] == str(m)[0]:




             #       print('%s --- %s' % (n, m))
