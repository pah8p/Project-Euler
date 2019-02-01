


def is_palindrome(s):
    _s = str(s)
    return _s == _s[::-1]

def int_to_bin(n):
    return bin(n)[2:]

print(int_to_bin(585))

N = 1000000

s = 0
for n in range(N):
    if is_palindrome(n):
        if is_palindrome(int_to_bin(n)):
            s += n

print(s)
