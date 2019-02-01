
import itertools

N = 4

PROBS = [1/(n+1) for n in range(1, N+1)]


def prob_blues(n):

    discs = range(N)

    all_blues = itertools.combinations(discs, n)

    probs = 0
    for blues in all_blues:
        
        reds = [red for red in discs if red not in blues]

        prob = 1
        for blue in blues:
            prob *= PROBS[blue]

        for red in reds:
            prob *= (1-PROBS[red])

        probs += prob

#    print(n, probs)

    return probs

def allocation():
    prob = sum(prob_blues(i) for i in range(int(N/2)+1, N+1))
    return prob, 1/prob

#print(allocation())

_F = {}

def F(n, b):

    try:
        return _F[(n, b)]

    except KeyError:

        p_b = (1/(n+1))
        p_r = 1-p_b


        #print(n, p_b, p_r)

        if n == 1:
            f = p_b
            
        else:
            f = p_b*F(n-1, b-1) + p_r*F(n-1, b)

            


        _F[(n, b)] = f

        return f

print(prob_blues(4))
print(F(4, 3))
print(F(4, 4))

print(_F)









        
