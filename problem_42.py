import math

triangle = lambda n: n*(n+1)/2

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

letter_value = lambda x: 1 + ALPHABET.index(x)

word_value = lambda w: sum([letter_value(x) for x in w])

def is_triangle(x):
    pos = (-1+math.sqrt(1+8*x))/2
    return pos==int(pos)

def is_triangle_word(x):
    return is_triangle(word_value(x))

with open('C:/Users/Pete/Desktop/p042_words.txt', 'r') as f:
    words = f.read()

words = words.split(',')

triangles = [word for word in words if is_triangle_word(word)]

print(len(triangles))
