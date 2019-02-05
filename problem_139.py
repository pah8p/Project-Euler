import pell_equation
import euler_tools

pell_solutions = pell_equation.solve(2, 100)

tot = 0
for p in pell_solutions[1:]:

    n = p[1]

    a = (p[0] - 1) // 2
    b = (p[0]+1)//2
    c = p[1]

    f = p[0]**2-2*p[1]**2

    if f == -1:

        perim = a+b+c
        tot += int(1e8/perim)

        if perim < 1e8:
            print(p[0], n, a, b, c, a**2+b**2==c**2)

print(tot)