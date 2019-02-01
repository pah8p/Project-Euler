
NAME_FILE = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p022_names.txt'

LETTERS = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}

with open (NAME_FILE, "r") as name_file:
    names = name_file.read()

names = names[1:-1]
names = names.split('","')
names.sort()

total_score = 0
for n, name in enumerate(names):
    name_score = 0
    for letter in name:
        try:
            name_score += LETTERS[letter]
        except KeyError:
            print(name)
            raise KeyError
    total_score += name_score*(n+1)

    if name == 'COLIN':
        print(name_score*(n+1))
        print(n)
        print(name_score)
    

print(total_score)




