
A = 100
B = 100

results = []
for a in range(2, A+1):
    for b in range(2, B+1):
        results.append(a**b)

print(set(results))
print(len(set(results)))
