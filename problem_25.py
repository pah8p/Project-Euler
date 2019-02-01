import math

FIB = {
    1: 1,
    2: 1,
}

def fib(n):
    try:
        return FIB[n]
    except KeyError:
        f = FIB[n-1] + FIB[n-2]
        FIB[n] = f
        return f    
##    if n == 1:
##        return 1
##    elif n == 2:
##        return 1
##    else:
##        return fib(n-1) + fib(n-2)

def log_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 0
    else:
        return math.log(fib(n-1), 10) + math.log(1+fib(n-2)/fib(n-1), 10)

i = 1
while True:
    lf = log_fib(i)
    if lf > 999:
        print(i)
        break
    
    i += 1
    
