
import itertools

SQUARES = [
    (0, 1),
    (0, 4),
    (0, 9),
    (1, 6),
    (2, 5),
    (3, 6),
    (4, 9),
    (6, 4),
    (8, 1),
]

def check_die(n, d):
    if n == 6:
        return 6 in d or 9 in d
    if n == 9:
        return 6 in d or 9 in d
    else:
        return n in d

def check_dice_2(d1, d2):
    for sq in SQUARES:

        x, y = False, False
        
        if check_die(sq[0], d1) and check_die(sq[1], d2):
            x = True

        if check_die(sq[1], d1) and check_die(sq[0], d2):
            y = True

        if not (x or y):
            return False

    return True

def check_dice(d1, d2):
    for square in SQUARES:

        x, y = True, True
        
        if square[0] not in d1 or square[1] not in d2:
            x = False
        if square[1] not in d1 or square[0] not in d2:
            y = False

        if not x and not y:
            #print(False, square)
            return False
            
    return True

def get_dice():
    _dice = []
    dice = list(itertools.combinations(range(0, 10), 6))

    for d in dice:
        _d = list(d)
        if 6 in _d:
            _d.append(9)
            _d.append(66)
        if 9 in _d:
            _d.append(6)
            _d.append(99)
        _dice.append(tuple(sorted(tuple(set(_d)))))

    return list(set(_dice))

#print(len(get_dice()))

dice = get_dice()

s = 0
_s = 0
ss = []
for i in range(len(dice)):
    for j in range(i+1, len(dice)):

        x = check_dice(dice[i], dice[j])

        if x:
            s += 1
        else:
            _s += 1

print(s)
print(_s)





print(
    check_dice_2(
        [0, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 8, 9],
    )
)

