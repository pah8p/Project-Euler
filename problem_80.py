
import decimal
from decimal import Decimal


decimal.getcontext().prec = 200


def sum_digits(x, n):

    if float(x).is_integer():
        return 0
    
    shifted = int(x * 10**(n-1))
    digits = shifted % 10**(n)
    return sum([int(d) for d in str(digits)])

print(sum([sum_digits(Decimal(x).sqrt(), 100) for x in range(1, 101)]))

