import euler_tools

def pandigital_product(a, b):
    to_list = lambda n: [int(m) for m in str(n)]
    return [1, 2, 3, 4, 5, 6, 7, 8, 9] == sorted(
        to_list(a) + to_list(b) + to_list(a*b)
    )

print(pandigital_product(39, 186))

products = []
for n in range(1, 31622):
    if n % 1000 == 0:
        print(n)
    
    divisors = euler_tools.proper_divisors(n)
    for divisor in divisors:
        if pandigital_product(divisor, int(n/divisor)):
            products.append(n)

print(products)
print(sum(set(products)))


