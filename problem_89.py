
ROMANS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def decimal_to_roman(n):

    orig_n = n
    roman = ''

    n_I = n % 5
    if n_I == 4:
        roman = '%s%s' % ('IV', roman)
    else:
        roman = '%s%s' % (''.join(['I']*n_I), roman)
    n -= n_I

    n_V = int((n%10)/5)
    roman = '%s%s' % (''.join(['V']*n_V), roman)
    n -= n_V*5

    n_X = int((n%50)/10)
    if n_X == 4:
        roman = '%s%s' % ('XL', roman)
    else:
        roman = '%s%s' % (''.join(['X']*n_X), roman)
    n -= n_X*10

    n_L = int((n % 100)/50)
    roman = '%s%s' % (''.join(['L']*n_L), roman)
    n -= n_L*50

    n_C = int((n % 500)/100)
    if n_C == 4:
        roman = '%s%s' % ('CD', roman)
    else:
        roman = '%s%s' % (''.join(['C']*n_C), roman)
    n -= n_C*100

    n_D = int((n % 1000)/500)
    roman = '%s%s' % (''.join(['D']*n_D), roman)
    n -= n_D * 500

    n_M = int(n / 1000)
    roman = '%s%s' % (''.join(['M']*n_M), roman)

    if 'VIV' in roman:
        roman = roman.replace('VIV', 'IX')

    if 'LXL' in roman:
        roman = roman.replace('LXL', 'XC')

    if 'DCD' in roman:
        roman = roman.replace('DCD', 'CM')

    return roman

def roman_to_decimal(r):
    raw_r = list(r)
    clean_r = []
    i = 0
    while i < len(raw_r):

        if i == len(raw_r) - 1:
            clean_r.append(ROMANS[raw_r[i]])
            i += 1
        
        elif ROMANS[raw_r[i]] >= ROMANS[raw_r[i+1]]:
            clean_r.append(ROMANS[raw_r[i]])
            i += 1
        elif ROMANS[raw_r[i]] < ROMANS[raw_r[i+1]]:
            clean_r.append(ROMANS[raw_r[i+1]] - ROMANS[raw_r[i]])
            i += 2

        if i >= len(raw_r):
            break
    
    return sum(clean_r)

def clean_romans():

    saved = 0
    
    file = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p089_roman.txt'
    with open(file, 'r') as f:
        romans = f.readlines()

    romans = [str(r.strip()) for r in romans]

    for roman in romans:
        cleaned = decimal_to_roman(roman_to_decimal(roman))
        saved += (len(roman)-len(cleaned))
        print(cleaned, roman)

    print(saved)
    return None

clean_romans()

#for i in range(1005): print(decimal_to_roman(i))
