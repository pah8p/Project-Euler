
N = int(1e6)

def formula(j):
    return int((-(j+1)+((j+1)**2+N)**0.5)/2)

#for i in range(int(N/4)-1):
#    print(formula(i))

print(sum([formula(i) for i in range(int(N/4)-1)]))
