

PAIRS = [
    (1, 10**19),
    (2, 10**17),
    (3, 10**15),
    (4, 10**13),
    (5, 10**11),
    (6, 10**9),
    (7, 10**7),
    (8, 10**5),
    (9, 10**3),
    (0, 10**1),
]

def sieve(pairs):

    n = 1
    x = pairs[0][0]
    
    for i in range(len(pairs)-1):
        a = pairs[i][0]
        n = n * pairs[i][1]
        

    





def number(digits):
    n = 0
    for i, digit in enumerate(digits):
        j = len(digits)-i-1
        n += digit * 10**j
    return n

def brute():
    raw = [
        1, None, 2, None, 3, None, 4, None, 5, None,
        6, None, 7, None, 8, None, 9, None, 0
    ]

    for a in range(0, 1):
        raw[1] = a
        for b in range(0, 10):
            raw[3] = b
            for c in range(0, 10):
                raw[5] = c
                for d in range(0, 10):
                    raw[7] = d
                    for e in range(0, 10):
                        raw[9] = e
                        for f in range(0, 10):
                            raw[11] = f
                            for g in range(0, 10):
                                raw[13] = g
                                for h in range(0, 10):
                                    raw[15] = h
                                    for i in range(0, 10):
                                        raw[17] = i
                                        n = number(raw)
                                        sqrt = n**0.5
                                        if sqrt.is_integer():
                                            return(sqrt)

import euler_tools

with euler_tools.Watch():
    print(brute())




print(number([1, 0, 1, 2]))

