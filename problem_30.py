
def sum_fifth(n):
    return sum([int(m)**5 for m in str(n)])

print(sum([n for n in range(2, 1000000) if n == sum_fifth(n)]))

#print(sum_fifth(1634))
#print(sum_fifth(8208))
#print(sum_fifth(9474))
