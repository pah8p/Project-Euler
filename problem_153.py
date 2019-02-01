
import euler_tools

class C(object):
    def __init__(self, r, i):
        self.r = r
        self.i = i
        if i == 0:
            self.norm = r
        else:
            self.norm = r**2+i**2

    def __repr__(self):
        return '%s + %si' % (self.r, self.i)

def complex_numbers(n):
    cns = []
    for m in range(0, 1):
        cns.append(C(n, m))
        if n != m:
            cns.append(C(m, n))
    return cns

def contribution(k, cn):
    
    if cn.i > 0:

        try:
            a = k*cn.norm/(cn.r+cn.i*cn.i/cn.r)
        except ZeroDivisionError:
            a = 0.0

        if a == cn.r:
            return 2*cn.r
        else:
            return 2*(cn.r+int(a))

    else:
        return cn.r

def sieve(i):
    
    _sieve = [0]*i
    
    for j in range(1, i+1):
        for cn in complex_numbers(j):

            k = 1
            while True:
                
                if k*cn.norm <= i:
                    _sieve[k*cn.norm-1] += contribution(k, cn)
                    k += 1
                    
                else:
                    break
                
    return _sieve

#print(complex_numbers(3))

#for i, j in enumerate(sieve(10)): print(i+1, j)

with euler_tools.Watch():
    print(sum(sieve(int(1e4))))
    
