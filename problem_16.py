

def two_to_bin(power):
    zeros = ['0']*power
    print(zeros)
    zeros_str = ''.join(zeros)
    return '1%s' % zeros_str

def two_to_int(power):
    return int(two_to_bin(power), 2)

dec = two_to_int(1000)

s = sum([int(x) for x in str(dec)])

print(s)
