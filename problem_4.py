

PALINDROMES = []

for i in range(100, 1000):
    for j in range(i, 1000):

        k = i * j

        if str(k) == str(k)[::-1]:

            PALINDROMES.append(k)

print(max(PALINDROMES))
