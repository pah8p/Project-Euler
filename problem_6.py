
N = 100

s = 0
ss = 0


for i in range(1, N+1):
    print(i)
    s += i
    ss += i**2
    
print(-ss + s**2)
