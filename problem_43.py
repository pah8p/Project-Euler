

def multiples(n):
    _m = []
    i = 1
    x = 0
    while x < 1000:
        x = n*i
        if x < 1000:
            _m.append(x)
        i+=1
    return _m

def check(x, y):
    if x < 100:
        x = '0%s' % x
    if y < 100:
        y = '0%s' % y
    return str(x)[:2]==str(y)[1:]

last = lambda x: x % 10

nums = []
digits = [str(n) for n in range(10)]
for a in multiples(17):
    for b in multiples(13):
        if check(a,b):
            for c in multiples(11):
                if check(b,c):
                    for d in multiples(7):
                        if check(c,d):
                            for e in multiples(5):
                                if check(d,e):
                                    for f in multiples(3):
                                        if check(e,f):
                                            for g in multiples(2):
                                                if check(f,g):
                                                    
                                                    n = '%s%s%s%s%s%s%s' % (
                                                        g,
                                                        last(f),
                                                        last(e),
                                                        last(d),
                                                        last(c),
                                                        last(b),
                                                        last(a),
                                                    )
                                                    for m in range(10):
                                                        nn = '%s%s' % (m, n)

                                                        if nn == '1406357289':
                                                            print(list(sorted(set(nn)))== digits)
                                                        
                                                        if list(sorted(set(nn))) == digits:
                                                            nums.append(int(nn))

print(sum(nums))


print(list(sorted(set('1406357289'))))


                                                    
