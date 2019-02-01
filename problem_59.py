
from operator import xor

def read_cipher():
    file = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p059_cipher.txt'
    with open(file, 'r') as f:
        raw_cipher = f.readlines()

    cipher = [int(x) for x in raw_cipher[0].split(',')]

    return cipher
    
def decrypt(cipher, key):
    key = key*400 + [key[0]]
    message = [chr(xor(c, k)) for c, k in zip(cipher, key)]
    return ''.join(message)

def decrypt_ascii(ciper, key):
    key = key*400 + [key[0]]
    message = [xor(c, k) for c, k in zip(cipher, key)]
    return sum(message)

def find_key(ciper):
    keys = []
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                keys.append([a, b, c])

    cribs = ['and', 'the', 'or', 'if']

    for key in keys:
        decrypted = decrypt(ciper, key)

        valid = True
        for crib in cribs:
            if crib not in decrypted:
                valid = False

        if valid:
            print(key)
        



cipher = read_cipher()
key = [103, 111, 100]

print(decrypt(cipher, key))

print(decrypt_ascii(cipher, key))

#find_key(cipher)
