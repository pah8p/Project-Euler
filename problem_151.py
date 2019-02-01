

PREV_ENVELOPE = {
    0: {
        'A2': 1,
        'A3': 1,
        'A4': 1,
        'A5': 1,
    }
}

def prob(n):

    pe = PREV_ENVELOPE[n-1]

    d = sum(pe.values())

    p_A2 = pe['A2']/d
    p_A3 = pe['A3']/d
    p_A4 = pe['A4']/d
    p_A5 = pe['A5']/d

    n_A2 = p_A2*(pe['A2']-1) + pe['A2']*(p_A3 + p_A4 + p_A5)
    n_A3 = p_A2*(pe['A3']+1) + p_A3*(pe['A3']-1) + pe['A3']*(p_A4 + p_A5)
    n_A4 = (p_A2+p_A3)*(pe['A4']+1) + p_A4*(pe['A4']-1)+p_A5*pe['A4']
    n_A5 = (p_A2+p_A3+p_A4)*(pe['A5']+1)+p_A5*(pe['A5']-1)

    PREV_ENVELOPE[n] = {
        'A2': n_A2,
        'A3': n_A3,
        'A4': n_A4,
        'A5': n_A5,
    }

    return p_A5

for i in range(1, 16):
    prob(i)
    print(i, PREV_ENVELOPE[i-1])

#print(PREV_ENVELOPE)
    
    
##    try:
##        return ENVELOPE[n]['A5']
##    except KeyError:
##        if n == 1:
##            num_a5 = 1
##            tot_sheets = 4
##            envelope = {
##                'A2': 3/4,
##                'A3': 4/4,
##                'A4': 5/4,
##                'A5': 6/4,
##            }
##
##        else:
##            num_A5 = prob(n-1)['A5']
##            tot_sheets = sum(prob(n-1).values())
##
##
##
##
##            if you draw A2:
##                A2 = A2-1
##                A3 = A3+1
##                A4 = A4+1
##                A5 = A5+1
##
##            if you draw A3:
##                A2 = A2
##                A3 = A3-1
##                A4 = A4+1
##                A5 = A5+1
##
##            if you draw A4:
##                A2 = A2
##                A3 = A3
##                A4 = A4-1
##                A5 = AT+1
##
##            if you draw A5:
##                A2 = A2
##                A3 = A3
##                A4 = A4
##                A5 = A5-1
##    
##
##
##
##        ENVELOPE[n] = envelope
##        return ev
##
##
##            
##
##[A2, A3, A4, A5]
##
##evenvelop = {
##    'A2': 1,
##    'A3': 1,
##    'A4': 1,
##    'A5': 1,
##}
##
##p_A2 = 1/4:
##
##    A2 = (p_A2)*(e_A2-1)
##    A3 = (p_A2)*(e_A3+1)
##    A4 = (p
##
##
##
##
##if draw A2:
##    envelope = ['A3', 'A3', 'A4', 'A4', 'A5', 'A5']
##    envelope = {
##        'A2': 0,
##        'A3': 2,
##        'A4': 2,
##        'A5': 2,
##    }
##
##if draw A3:
##    ['A2', 'A3', 'A4', 'A5']
##    enveolpe = ['A2', 'A4', 'A4', 'A5', 'A5']
##    envelope = {
##        'A2': 1,
##        'A3': 0,
##        'A4': 2,
##        'A5': 2,
##    }
##
##if draw A4:
##    ['A2', 'A3', 'A5', 'A5']
##    envelope = {
##        'A2': 1,
##        'A3': 1,
##        'A4': 0,
##        'A5': 2,
##    }
##
##if draw A5:
##    envelope = {
##        'A2': 1,
##        'A3': 1,
##        'A4': 1,
##        'A5': 0
##    }
