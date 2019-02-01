
import pell_equation

solutions = pell_equation.solve(5, 25)

ts = []
for s in solutions:
    b_up = (s[0]-2)*2/5
    b_dn = (s[0]+2)*2/5
    if b_up.is_integer():
        ts.append((b_up, s[1]))
    if b_dn.is_integer():
        ts.append((b_dn, s[1]))

for t in ts: print(t)

print(len(ts))
print(sum([t[1] for t in ts]))
