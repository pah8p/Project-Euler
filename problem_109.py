
BOARD = {
    'S1': 1,
    'S2': 2,
    'S3': 3,
    'S4': 4,
    'S5': 5,
    'S6': 6,
    'S7': 7,
    'S8': 8,
    'S9': 9,
    'S10': 10,
    'S11': 11,
    'S12': 12,
    'S13': 13,
    'S14': 14,
    'S15': 15,
    'S16': 16,
    'S17': 17,
    'S18': 18,
    'S19': 19,
    'S20': 20,
    'D1': 2,
    'D2': 4,
    'D3': 6,
    'D4': 8,
    'D5': 10,
    'D6': 12,
    'D7': 14,
    'D8': 16,
    'D9': 18,
    'D10': 20,
    'D11': 22,
    'D12': 24,
    'D13': 26,
    'D14': 28,
    'D15': 30,
    'D16': 32,
    'D17': 34,
    'D18': 36,
    'D19': 38,
    'D20': 40,
    'T1': 3,
    'T2': 6,
    'T3': 9,
    'T4': 12,
    'T5': 15,
    'T6': 18,
    'T7': 21,
    'T8': 24,
    'T9': 27,
    'T10': 30,
    'T11': 33,
    'T12': 36,
    'T13': 39,
    'T14': 42,
    'T15': 45,
    'T16': 48,
    'T17': 51,
    'T18': 54,
    'T19': 57,
    'T20': 60,
    'SB': 25,
    'DB': 50,
}

WAYS = {}

def ways(target):

    try:
        return WAYS[target]

    except KeyError:

        if target == 0:
            r = []

        else:

            s = []
            for box, value in BOARD.items():
                remainder = target - value

                if remainder == 0:
                    s.append([box])
                elif remainder > 0:
                    subways = ways(remainder)
                    for subway in subways:
                        s.append([box] + subway)
                     
            r = s

        checkouts = []
        for _r in r:
            if len(_r) <= 3:
                if _r[-1][0] == 'D':
                    checkouts.append(tuple(sorted(_r[:-1]) + [_r[-1]]))


        checkouts = [list(c) for c in list(set(checkouts))]

        WAYS[target] = checkouts

        return sorted(checkouts, key=lambda x: len(x))

##six = ways(6)
##
##print(len(six))
##for x in six: print(x)


print(sum([len(ways(i)) for i in range(1, 100)]))









