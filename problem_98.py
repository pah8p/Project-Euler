import collections
import euler_tools

def load_words():
    file = 'p098_words.txt'
    with open(file, 'r') as f:
        words = f.read()
    return [word[1:-1] for word in words.split(',')]

def segment_words(words):
    _words = collections.defaultdict(list)
    for word in words:
        _words[len(word)].append(word)
    return _words

def anagram_words(segmented_words):
    _anagrams = []
    for length, words in segmented_words.items():

        for i in range(len(words)):
            for j in range(i+1, len(words)):

                if sorted(words[i]) == sorted(words[j]):

                    if words[i] != words[j][::-1]:

                        _anagrams.append(sorted([words[i], words[j]]))

    return _anagrams

def check_pair(w1, w2):
    sqs = []
    n = len(w1)
    m = int(10**((n-1)/2)) + 1
    m2 = 0
    while m2 < 10**n:

        m2 = m**2

        mapper = dict(zip(w1, str(m2)))
        test_square = int(''.join([mapper[c] for c in w2]))
        test_root = test_square**0.5

        if test_root.is_integer() and len(str(m2)) == len(set(str(m2))) and test_square > (10**(n-1)):
            sqs.append((m, w1, w2, m2, test_square, max(m2, test_square), test_root))
        
        m += 1

    return sorted(sqs, key = lambda x: x[5])

with euler_tools.Watch():

    words = anagram_words(segment_words(load_words()))

    for pair in words:
        cp = check_pair(*pair)
        for x in cp: print(x)





