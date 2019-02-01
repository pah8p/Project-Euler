
from decimal import Decimal
import decimal
import math

N = int(250)

decimal.getcontext().prec = N

def get_period(n):

    nn = n

    print(int(n**2))

    if float(n).is_integer():
        return [], 0, False

    integer = Decimal(math.floor(n))
    a = [int(integer)]
    remainder = n - integer
    n = 1/remainder

    i = 1

    while i < N:

        #print(n)
        
        integer = Decimal(math.floor(n))
        a.append(int(integer))
        
        if integer == 2*a[0]:

            #if (len(a)-1) % 2 == 1:
                #print(int(nn**2), a)

            
            return a, len(a)-1, ((len(a)-1)%2==1)

        remainder = n - integer
        n = 1/remainder

        i += 1

    print(nn**2)
    return (a, 0, False)

    #raise Exception('Maxed iterations %s' % nn**2)

#print(get_period(Decimal(991).sqrt()))


#print(Decimal(1000).sqrt())

print(sum([1 for i in range(2, 10001) if get_period(Decimal(i).sqrt())[2]]))
