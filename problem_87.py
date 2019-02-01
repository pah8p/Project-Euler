
import decimal
import euler_tools

euler_tools.write_primes(int(1e5))
PRIMES = euler_tools.read_primes()

def ppt(n):

    def powers(k):
        _powers = []
        for p in PRIMES:
            num = p**k
            if num < n:
                _powers.append(num)
            else:
                break
        return _powers

    squares = powers(2)
    cubes = powers(3)
    tesseracts = powers(4)

    ppts = []
    for square in squares:
        for cube in cubes:
            for tesseract in tesseracts:
                x = square + cube + tesseract
                if x < n:
                    ppts.append(x)

    return set(ppts)

ppts = ppt(50e6)

print(len(ppts))
#print(ppts)
                
