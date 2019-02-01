

def ones_to_text(n):
    #print('one %s' % n)
    if n == 1:
        return 'ONE'
    elif n == 2:
        return 'TWO'
    elif n == 3:
        return 'THREE'
    elif n == 4:
        return 'FOUR'
    elif n == 5:
        return 'FIVE'
    elif n == 6:
        return 'SIX'
    elif n == 7:
        return 'SEVEN'
    elif n == 8:
        return 'EIGHT'
    elif n == 9:
        return 'NINE'
    elif n == 0:
        return ''
    else:
        raise Exception('Not a number below 10')

def tens_to_text(n, m):
    #print('ten %s' % n)
    if n == 1:
        return teens_to_text(m)
    elif n == 2:
        return 'TWENTY'
    elif n == 3:
        return 'THIRTY'
    elif n == 4:
        return 'FORTY'
    elif n == 5:
        return 'FIFTY'
    elif n == 6:
        return 'SIXTY'
    elif n == 7:
        return 'SEVENTY'
    elif n == 8:
        return 'EIGHTY'
    elif n == 9:
        return 'NINETY'
    elif n == 0:
        return ''

def teens_to_text(n):
    if n == 10:
        return 'TEN'
    elif n == 11:
        return 'ELEVEN'
    elif n == 12:
        return 'TWELVE'
    elif n == 13:
        return 'THIRTEEN'
    elif n == 14:
        return 'FOURTEEN'
    elif n == 15:
        return 'FIFTEEN'
    elif n == 16:
        return 'SIXTEEN'
    elif n == 17:
        return 'SEVENTEEN'
    elif n == 18:
        return 'EIGHTEEN'
    elif n == 19:
        return 'NINETEEN'
    else:
        return ''

def hundred_teens_to_text(n):
    return '%s%s' % (hundreds_to_text(hundreds_digit(n)), teens_to_text(n-100*hundreds_digit(n)))

def hundreds_to_text(n):
    #print('hun %s' % n)
    if n == 0:
        return ''
    return '%sHUNDRED' % ones_to_text(n)

def ones_digit(n):
    return n % 10

def tens_digit(n):
    return int((n % 100)/10)

def hundreds_digit(n):
    return int((n % 1000)/100)

def number_to_text(n):
    if n == 0:
        return 'ZERO'
    elif n == 10:
        return 'TEN'
    elif n in range(11, 20):
        return teens_to_text(n)
    elif n == 100:
        return 'ONEHUNDRED'
    elif n % 100 in range(10, 20):
        return hundred_teens_to_text(n)
    elif n == 1000:
        return 'ONETHOUSAND'

    return '%s%s%s' % (
        hundreds_to_text(hundreds_digit(n)),
        tens_to_text(tens_digit(n), n),
        ones_to_text(ones_digit(n)),
    )

print(number_to_text(342))
print(len(str(number_to_text(342)).strip()))

raws = [number_to_text(n) for n in range(1, 1001)]
for r in raws: print(r)
counts = [len(str(r).strip()) for r in raws]
print(sum(counts) + 99*9*3)
