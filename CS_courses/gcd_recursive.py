"""The greatest common divisor of two positive integers is the largest integer
that divides each of them without remainder. A clever mathematical
trick (due to Euclid) makes it easy to find greatest common divisors.
Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)"""

def gcdRecur(a, b):
    '''subtract multiples of smaller num from larger num until remainder is < smaller num/
    #make smaller num new large num, and remainder new smaller num, and repeat
    #subtract multiples of remainder from smaller num until remainder is < remainder'''

    #if modulo operation successful, found GCD
    if b == 0:
        return a

    #Otherwise, make old small into new big, and new small the remainder of big mod small
    else:
        return gcdRecur(b, a % b)

print(gcdRecur(25, 15))
