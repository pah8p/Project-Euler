
f = ''.join([str(i) for i in range(1, 1000000)])


n = 1
for i in [1, 1e2, 1e3, 1e4, 1e5, 1e6]:
    n *= int(f[int(i)-1])
print(n)


#print(f[0]*f[9]*f[99]*f[999]*f[9999]*f[99999]*f[999999])
