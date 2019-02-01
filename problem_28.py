
N = 501

cnt = 1
prev_low = 1
for i in range(1, N):
    low_corner = prev_low + 2 + 8*(i - 1)
    for j in range(4):
        x = low_corner + 2*i*j
        cnt += low_corner + 2*i*j
    prev_low = low_corner
        
print(cnt)
    
