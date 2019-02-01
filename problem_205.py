from collections import defaultdict

TOT_P_ROLLS = 4**9
P_ROLLS = defaultdict(int)
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                for i in range(1, 5):
                                    P_ROLLS[a+b+c+d+e+f+g+h+i] += 1

TOT_C_ROLLS = 6**6
C_ROLLS = defaultdict(int)
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        C_ROLLS[a+b+c+d+e+f] += 1

p_win = 0
for p_k, p_v in P_ROLLS.items():
    p_win += p_v * sum([c_v for c_k, c_v in C_ROLLS.items() if c_k < p_k])

print(p_win)
print(p_win/TOT_P_ROLLS/TOT_C_ROLLS)

print(dict(P_ROLLS))
print(dict(C_ROLLS))
