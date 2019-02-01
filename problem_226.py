
import decimal

def _I(x):
    if 0 <= x <= 0.5:
        return x**2/2, 2*x, 1/4
    elif 0.5 < x < 1:
        return 1/2, 1-x, -1
    elif x == 1.0:
        return 1/2, x, 0

def I(x, accuracy):
    i = 0
    factor = 1
    for n in range(accuracy):
        contribution, x, _factor = _I(x)
        i += contribution*factor
        factor *= _factor
        #print(i, contribution, x, factor)
    return i
    
def s(x):
    residual = x - int(x)
    if residual > 0.5:
        return int(x) + 1 - x
    else:
        return x - int(x)

def _b(x):
    if 2*x > 1:
        xx = 2*x-1
    else:
        xx = 2*x
    return decimal.Decimal(s(x)), xx, decimal.Decimal(1/2)

def blancmange(x, accuracy):
    b = 0
    factor = 1
    for n in range(accuracy):
        contribution, x, _factor = _b(x)
        b += contribution*factor
        factor *= _factor
    return b

def blancmange2(x):
    b = 0
    for n in range(0, 100):
        t = 2**n
        b += s(t*x)/t
        #print(x, n, t, s(t*x), s(t*x)/t)
    return b

def circle(x):
    a = decimal.Decimal(1/16) - (x - decimal.Decimal(0.25))**2
    return decimal.Decimal(1/2)-a.sqrt()
    
    #return 1/2-(1/16-(x-1/4)**2)**0.5

def intersect():
    guess = decimal.Decimal(.0790)
    n = 10**6
    x = []
    while guess < .08:
        guess += decimal.Decimal(1/n)
        #print(guess)
        x.append((guess, abs(circle(guess)-blancmange(guess, 1000))))
    return min(x, key=lambda z: z[1])

#print(blancmange(1/3))

#print(circle(1/2))

x = intersect()
#x = (decimal.Decimal(0.07890778799995585), )

print(x)

print(blancmange(x[0], 1000))
#print(blancmange2(x[0]))

#print(I(1/3, 8))
#print(I(1/3, 108))

#print(I(x[0], 8))
#print(I(x[0], 500))
#print(I(1/2, 108) - I(x[0], 500))
print(circle(x[0]))
#print(blancmange(x[0], 100))




