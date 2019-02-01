import collections

def check_passcode(code, keys):
    for key in keys:
        p = [code.index(key[i]) for i in range(3)]

        if not ((p[0] < p[1]) and (p[1] < p[2])):
            print('Failed on:', code, key)
            return False
        
    return True

def rank_letters(keys):
    losers = []
    letters = []
    for key in keys:
        for i in range(len(key)):
            letters.append(key[i])
        for i in range(1, len(key)):
            losers.append(key[i])

    winners = []
    for letter in set(letters):
        if letter not in set(losers):
            winners.append(letter)
            
    assert len(winners) == 1

    return winners[0]

def remove_winners(keys, winner):
    fresh_keys = []
    for key in keys:
        fresh_key = key.replace(winner, '')
        if not fresh_key == '':
            fresh_keys.append(fresh_key)
    return fresh_keys

def find_code(keys):
    code = ''
    while len(keys) > 0:
        winner = rank_letters(keys)
        code = '%s%s' % (code, winner)
        keys = remove_winners(keys, winner)
    return code
            
        
    
    



    
##    letters = collections.defaultdict(dict)
##    for key in keys:
##        for i, letter in enumerate(key):
##            try:
##                letters[letter][i] += 1
##            except KeyError:
##                letters[letter][i] = 1
##    return letters
            
        
def read_keylog():
    with open('C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p079_keylog.txt', 'rb') as f:
        keylog = f.readlines()
    return [str(int(k)) for k in keylog]

keys = read_keylog()

#print(keys)
#print(keys[0][0])

print(find_code(keys))
print(check_passcode(find_code(keys), keys))
