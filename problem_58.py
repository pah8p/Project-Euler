
def is_prime(n):
    if n == 1:
        return False

    for m in range(2, int(n**0.5)+1):
        if n % m == 0:
            return False

    return True

def prime_diags(threshold):

    numerator = 0
    denominator = 1

    i = 1

    above_threshold = True
    while above_threshold:

        denominator += 4

        for j in [-1, 0, 1]:

            val = 4*i**2 + 2*j*i + 1
            
            if is_prime(val):
                numerator += 1

        above_threshold = (numerator/denominator > threshold)

        print(i, 2*i+1, numerator, denominator, numerator/denominator)

        i += 1

    return 2*(i-1) + 1

print(prime_diags(0.10))
