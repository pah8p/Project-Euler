import euler_tools
import math



#A*10**2+B*10**1+C*10**0

##def forward(power):
##
##    for a in range(10):
##        A = a*10**2
##        for b in range(10):
##            B = b*10**1
##            for c in range(10):
##                C = c*10**0
##                print(A+B+C)

NUMBERS = {}


def numbers(for_power, back_power):

    try:
        return NUMBERS[(for_power, back_power)]

    except KeyError:
    
        nums = []

        if for_power < 0:
            return [(0, 0)]

        for i in range(10):
            f = i*10**for_power
            b = i*10**back_power
            for _f, _b in numbers(for_power-1, back_power+1):
                nums.append((f+_f, b+_b))
                #print(f+_f, b+_b)

        NUMBERS[(for_power, back_power)] = nums

        return nums


def backward(for_power, back_power):
    nums = []

    if back_power > for_power:
        return [0]

    for i in range(10):
        n = i*10**back_power
        for j in backward(for_power, back_power+1):
            nums.append(n+j)

    return nums

def forward(power):
    nums = []
    
    if power < 0:
        return [0]
    
    for i in range(10):
        n = i*10**power
        for j in forward(power-1):
            nums.append(n+j)

    return nums


def reverse(n):
    return int(str(n)[::-1])

with euler_tools.Watch():
##    for i in forward(1):
##        print(i)

##    for i in backward(1, 0):
##        print(i)

    numbers(8,0)

    for i in numbers(1, 0):
        print(i, i[0]==reverse(i[1]))
